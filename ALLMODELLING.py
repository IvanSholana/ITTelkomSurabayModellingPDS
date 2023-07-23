import random


class Mahasiswa:
    def __init__(self, id, prodi, angkatan):
        self.id = id
        self.prodi = prodi
        self.angkatan = angkatan


class Prodi:
    def __init__(self, namaProdi):
        self.mahasiswa = []
        self.nama_prodi = namaProdi
        self.angkatan = []
        self.kelas = []

    def tambah_kelas(self, nama_kelas):
        self.kelas.append(nama_kelas)

    def tambah_angkatan(self, tahunAngkatan):
        self.angkatan.append(tahunAngkatan)

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa.append(mahasiswa)


class Kelas:
    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas
        self.mahasiswa = []

    def tambahMahasiswa(namaMahasiswa):
        self.mahasiswa.append(namaMahasiswa)


prodi = [
    Prodi("Informatika"),
    Prodi("Sistem Informasi"),
    Prodi("Teknologi Indormasi"),
    Prodi("Rekayasa Perangkat Lunak"),
    Prodi("Sains Data"),
]

a = 0
angkatan = 2021
for i in range(30):
    for x in range(random.randint(1, 100)):
        if random.random() < 0.2:
            prodiID = random.randint(0, 4)
            a += 1
            prodi[prodiID].tambah_mahasiswa(
                Mahasiswa(a, prodi[prodiID].nama_prodi, angkatan)
            )
    angkatan += 1
