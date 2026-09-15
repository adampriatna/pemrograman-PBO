# BAGIAN A: MAHASISWA
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def tampilkan_info(self):
        print("nama mahasiswa : ", self.nama)
        print("nim            : ", self.nim)

mhs1 = Mahasiswa("Muhammad Adam", "2495114013")
mhs2 = Mahasiswa("Edho", "66528463")
mhs3 = Mahasiswa("Bagus", "2495114015")

mhs1.tampilkan_info()
mhs2.tampilkan_info()
mhs3.tampilkan_info()


# BAGIAN B: BUKU
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    def info_buku(self):
        print("judul buku     : ", self.judul)
        print("penulis        : ", self.penulis)

buku1 = Buku("Dunia Abadi", "Bonsai Heri")
buku2 = Buku("Laskar Pelangi", "Andrea Hirata")

buku1.info_buku()
buku2.info_buku()


# Pertanyaan: Apa perbedaan class dan object berdasarkan program yang dibuat?
#Jawaban:
#Class (Mahasiswa, Buku) adalah cetakan/blueprint yang menentukan atribut apa saja yang harus dimiliki dan fungsi apa yang bisa dijalankan.
#Object (mhs1, buku1, dll) adalah wujud nyata hasil cetakan tersebut yang sudah berisi data spesifik (seperti nama asli, NIM, atau judul buku).
