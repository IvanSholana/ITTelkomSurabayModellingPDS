import random
import pandas as pd

class Universitas:
    total_mahasiswa = 0
    anggaran = 0

    def __init__(self, nama_kampus, prodi):
        self.nama = nama_kampus
        self.prodi = prodi

    def hitung_dosen_kampus(self):
        total = 0
        for program_studi in self.prodi:
            total += program_studi.dosen
        return total
    
    def mahasiswa_lulus(self):
        for program_studi in self.prodi:
            program_studi.angkatan.pop(0)

class Prodi:
    def __init__(self, nama, ukt, kode):
        self.nama = nama
        self.kode = kode
        self.ukt = ukt
        self.angkatan = []
        self.dosen = 0

    def tambah_angkatan_prodi(self, angkatan):
        self.angkatan.append(angkatan)

    def hitung_mahasiswa_prodi(self):
        total = 0
        for tiap_angkatan in self.angkatan:
            total += tiap_angkatan.hitung_mahasiswa_angkatan()
        return total

class Angkatan:
    def __init__(self, tahun):
        self.tahun = tahun
        self.mahasiswa = []
        self.kelas = []

    def tambah_mahasiswa_angkatan(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

    def hitung_mahasiswa_angkatan(self):
        return len(self.mahasiswa)
    
class Mahasiswa:
    def __init__(self,NIM):
        self.NIM = NIM
        
class Kelas:
    def __init__(self,nama_kelas):
        self.nama_kelas = nama_kelas
        self.mahasiswa = []
    def tambah_mahasiswa_kelas(self,mahasiswa):
        self.mahasiswa.append(mahasiswa)
    def hitung_mahasiswa_kelas(self):
        return len(self.mahasiswa)
    
    
prodi = [Prodi("Informatika",7000000,"IF"),
         Prodi("Sistem Informasi",8000000,"SI"),
         Prodi("Teknologi Indormasi",8000000,"TI"),
         Prodi("Rekayasa Perangkat Lunak",8500000,"RPL"),
         Prodi("Sains Data",7000000,"DS")]

TelkomMadura = Universitas("Telkom Madura",prodi)

def proses_mendaftar(NIM,tahun_angkatan):
    # MEMILIH PRODI
    prodi_terpilih = random.randint(0,4)
    mahasiswa_baru = Mahasiswa(NIM)
    prodi[prodi_terpilih].angkatan[tahun_angkatan].mahasiswa.append(mahasiswa_baru)
    
    # PEMBAYARAN
    BiayaUP3 = 8000000
    BiayaSDP = 12150000
    BiayaUKT = prodi[prodi_terpilih].ukt
    Total = BiayaSDP + BiayaUKT + BiayaUP3
    return Total

def membuat_kelas(angkatan):
    for program_studi in prodi:
        total_mahasiswa = program_studi.angkatan[angkatan].hitung_mahasiswa_angkatan()
        total_kelas = total_mahasiswa // 30
        kode_kelas = 0
        for _ in range(total_kelas):
            program_studi.angkatan[angkatan].kelas.append(Kelas(f"{program_studi.kode}-{angkatan}-{kode_kelas + 1}")) # menambahkan kelas baru
            for mahasiswa in program_studi.angkatan[angkatan].mahasiswa: # looping ke mahasiswa di angkatan tertentu
                program_studi.angkatan[angkatan].kelas[kode_kelas].mahasiswa.append(mahasiswa) # menambahkan mahasiswa ke kelas
                if program_studi.angkatan[angkatan].kelas[kode_kelas].hitung_mahasiswa_kelas() == 30: # jika mahasiswa per kelas sudah 30 maka break dan buat kelas baru
                    break
            kode_kelas += 1
            
        if total_mahasiswa - total_mahasiswa * 30 != 0:
            sisa_mahasiswa = total_mahasiswa - total_mahasiswa * 30 
            for sisa in range(total_mahasiswa-sisa_mahasiswa,total_mahasiswa): # looping dari mahasiswa yang belum dapat kelas
                program_studi.angkatan[angkatan].kelas.append(Kelas(f"{program_studi.kode}-{angkatan}-{kode_kelas + 1}")) # menambahkan kelas baru
                program_studi.angkatan[angkatan].kelas[kode_kelas].mahasiswa.append(program_studi.angkatan[angkatan].mahasiswa[sisa]) # menambahkan mahasiswa sisa ke kelas baru
                if program_studi.angkatan[angkatan].kelas[kode_kelas].hitung_mahasiswa_kelas() == 30: # jika mahasiswa per kelas sudah 30 maka break dan buat kelas baru
                    break
            kode_kelas += 1
        # KEBUTUHAN DOSEN
        hitung_kebutuhan_dosen(program_studi)
        
def hitung_kebutuhan_dosen(program_studi):
    total_mahasiswa = program_studi.hitung_mahasiswa_prodi()
    kebutuhan_dosen = total_mahasiswa // 60
    program_studi.dosen = kebutuhan_dosen
    
def pengeluaran_kampus(bulan):
    gajiDosen = 7000000 * TelkomMadura.hitung_dosen_kampus()
    pengeluaran = 0.7 * TelkomMadura.anggaran / 12  + gajiDosen
    if bulan == 12:
        pengeluaran += 200000000
    return pengeluaran

def hitung_mahasiswa(tahun_angkatan):
    total = 0
    for program_studi in prodi:
        total += program_studi.angkatan[tahun_angkatan].hitung_mahasiswa_angkatan()
    return total

def lihat_kelas():
    for program_studi in prodi:
        for angkatan in program_studi.angkatan:
            print(f"{program_studi.nama} ({angkatan.tahun}) :")
            for kelas in angkatan.kelas:
                print(f"{kelas.nama_kelas} : {[mahasiswa.NIM for mahasiswa in kelas.mahasiswa]}")
        print("\n")
        
def bayar_ukt(self):
    pemasukan = 0
    for program_studi in prodi:
        pemasukan += program_studi.ukt * program_studi.hitung_mahasiswa_prodi()
    return pemasukan

def rekap_mahasiswa_prodi(tahun):
    mahasiswa = []
    for program_studi in prodi:
        mahasiswa.append(program_studi.angkatan[tahun].hitung_mahasiswa_angkatan())
    return mahasiswa

def simulasi_kampus(tahun_start,tahun_terakhir):
    angkatan = tahun_start
    growth_factor = 1.02 # kenaikan atau penurunan mahasiswa calon pendaftar
    mahasiswa = random.randint(1,100) # kemungkinan mahasiswa calon pendaftar
    nim = 1 # NIM atau ID mahasiswa
    cashflow = []
    data_mahasiswa = []
    # SIMULASI
    for tahun in range(tahun_terakhir - tahun_start): 
        # Membuat Angkatan Baru di Tiap Prodi
        for program_studi in prodi:
            program_studi.tambah_angkatan_prodi(Angkatan(tahun))
        for bulan in range(1,13):
            pemasukan = 0
            if(bulan == 2 or bulan == 9):
                pemasukan += bayar_ukt(prodi)
            # PENDAFTARAN   
            for _ in range(30): 
                if random.random() < 0.5: # Kemungkinan kenaikan calon pendaftar
                    mahasiswa +=  int(mahasiswa * random.uniform(0.05, 0.5) * growth_factor)
                else:
                    mahasiswa -= int(mahasiswa * random.uniform(0.05, 0.5) * growth_factor)
                # Mahasiswa Mendaftar
                for _ in range(mahasiswa):
                    if random.random() < 0.5:
                        pemasukan += proses_mendaftar(nim,tahun)
                        nim += 1
                    if hitung_mahasiswa(tahun) == 600:
                        break
            
            # PEMASUKAN TIAP BULAN
            TelkomMadura.anggaran += pemasukan
        
            # PENGELUARAN TIAP BULAN
            pengeluaran = pengeluaran_kampus(bulan)
            TelkomMadura.anggaran -= pengeluaran
            cashflow.append([angkatan,bulan,pemasukan,pengeluaran,TelkomMadura.anggaran])
        
        # PEMBAGIAN KELAS
        membuat_kelas(tahun)
        angkatan += 1
        data_mahasiswa.append(rekap_mahasiswa_prodi(tahun))
        
    return [cashflow,data_mahasiswa]

result = simulasi_kampus(2021,2025)
result[1]