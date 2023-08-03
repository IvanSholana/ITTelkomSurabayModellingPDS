import random


class Universitas:
    total_mahasiswa = 0
    anggaran = 0

    def __init__(self, nama_kampus, prodi):
        self.nama = nama_kampus
        self.prodi = prodi

    def hitung_dosen(self):
        total = 0
        for program_studi in self.prodi:
            total += program_studi.dosen
        return total


class Prodi:
    def __init__(self, nama, ukt, kode):
        self.nama = nama
        self.ukt = ukt
        self.kode = kode
        self.angkatan = []
        self.kelas = []
        self.dosen = 0

    def tambah_angkatan(self, angkatan):
        self.angkatan.append(angkatan)

    def hitung_mahasiswa(self):
        total = 0
        for tiap_angkatan in self.angkatan:
            total += tiap_angkatan.hitung_mahasiswa()
        return total


class Angkatan:
    def __init__(self, tahun):
        self.tahun = tahun
        self.mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

    def hitung_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, NIM):
        self.NIM = NIM


class Kelas:
    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas
        self.mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)

    def hitung_mahasiswa(self):
        return len(self.mahasiswa)


prodi = [
    Prodi("Informatika", 7000000, "IF"),
    Prodi("Sistem Informasi", 8000000, "SI"),
    Prodi("Teknologi Informasi", 8000000, "TI"),
    Prodi("Rekayasa Perangkat Lunak", 8500000, "RPL"),
    Prodi("Sains Data", 7000000, "DS"),
]

TelkomMadura = Universitas("Telkom Madura", prodi)


def proses_mendaftar(NIM, tahun_angkatan):
    # MEMILIH PRODI
    prodi_terpilih = random.randint(0, 4)
    mahasiswa_baru = Mahasiswa(NIM)
    prodi[prodi_terpilih].angkatan[tahun_angkatan].tambah_mahasiswa(mahasiswa_baru)

    # PEMBAYARAN
    BiayaUP3 = 8000000
    BiayaSDP = 12150000
    BiayaUKT = prodi[prodi_terpilih].ukt
    Total = BiayaSDP + BiayaUKT + BiayaUP3
    return Total


def hitung_kebutuhan_dosen(program_studi):
    total_mahasiswa = program_studi.hitung_mahasiswa()
    kebutuhan_dosen = total_mahasiswa // 60
    program_studi.dosen = kebutuhan_dosen


def pengeluaran_kampus(bulan):
    gajiDosen = 7000000 * TelkomMadura.hitung_dosen()
    pengeluaran = 0.7 * TelkomMadura.anggaran / 12 + gajiDosen
    if bulan == 12:
        pengeluaran += 2000000
    return pengeluaran


def membuat_kelas(prodi, angkatan):
    for program_studi in prodi:
        total_mahasiswa = program_studi.angkatan[angkatan].hitung_mahasiswa()
        total_kelas = total_mahasiswa // 30
        kode_kelas = 0
        for _ in range(total_kelas):
            program_studi.kelas.append(
                f"{program_studi.kode}-{angkatan}-{kode_kelas + 1}"
            )
            for mahasiswa in program_studi.angkatan[angkatan].mahasiswa:
                program_studi.kelas[kode_kelas].tambah_mahasiswa(mahasiswa)
                if program_studi.kelas[kode_kelas].hitung_mahasiswa() == 30:
                    break
            kode_kelas += 1

        if total_mahasiswa - total_mahasiswa * 30 != 0:
            sisa_mahasiswa = total_mahasiswa - total_mahasiswa // 30 * 30
            for sisa in range(total_mahasiswa - sisa_mahasiswa, total_mahasiswa):
                program_studi.kelas.append(
                    f"{program_studi.kode}-{angkatan}-{kode_kelas + 1}"
                )
                program_studi.kelas[kode_kelas].tambah_mahasiswa(
                    program_studi.angkatan[angkatan].mahasiswa[sisa]
                )
                if program_studi.kelas[kode_kelas].hitung_mahasiswa() == 30:
                    break
            kode_kelas += 1

        # KEBUTUHAN DOSEN
        hitung_kebutuhan_dosen(program_studi)

def hitung_mahasiswa(program_studi):
    total_mahasiswa = 0
    for angkatan in program_studi.angkatan:
        total_mahasiswa += angkatan.hitung_mahasiswa()
    return total_mahasiswa


def bayar_ukt(prodi):
    pemasukan = 0
    for program_studi in prodi:
        for angkatan in program_studi.angkatan:
            total_mahasiswa = angkatan.hitung_mahasiswa()
            pemasukan += total_mahasiswa * program_studi.ukt
    return pemasukan

def simulasi_kampus(tahun_start, tahun_terakhir):
    angkatan = tahun_start
    growth_factor = 1.02
    mahasiswa = random.randint(1, 100)
    nim = 1
    cashflow = []

    for tahun in range(tahun_start, tahun_terakhir + 1):
        # Membuat Angkatan Baru di Tiap Prodi
        for program_studi in prodi:
            program_studi.tambah_angkatan(Angkatan(tahun))

        for bulan in range(1, 13):
            pemasukan = 0
            if bulan == 2 or bulan == 9:
                pemasukan += bayar_ukt(prodi)

            # PENDAFTARAN
            for _ in range(30):
                if random.random() < 0.5:
                    mahasiswa += int(
                        mahasiswa * random.uniform(0.05, 0.5) * growth_factor
                    )
                else:
                    mahasiswa -= int(
                        mahasiswa * random.uniform(0.05, 0.5) * growth_factor
                    )

                # Mahasiswa Mendaftar
                for _ in range(mahasiswa):
                    if random.random() < 0.5:
                        prodi_terpilih = random.randint(0, len(prodi) - 1)
                        prodi[prodi_terpilih].angkatan[
                            tahun - tahun_start
                        ].tambah_mahasiswa(Mahasiswa(nim))
                        pemasukan += proses_mendaftar(nim, tahun - tahun_start)
                        nim += 1
                    if hitung_mahasiswa(prodi) == 600:
                        break

            # PENGELUARAN TIAP BULAN
            pengeluaran = pengeluaran_kampus(bulan)
            TelkomMadura.anggaran -= pengeluaran
            cashflow.append(
                [angkatan, bulan, pemasukan, pengeluaran, TelkomMadura.anggaran]
            )

        # PEMBAGIAN KELAS
        membuat_kelas(prodi, angkatan)
        angkatan += 1
    return cashflow


result = simulasi_kampus(2021, 2025)
print(result)





result = simulasi_kampus(2021, 2025)
print(result)
