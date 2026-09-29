class Mahasiswa:
    def __init__(self, nama, nim, jurusan, nilai):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = nilai

    def cek_status(self):
        if self.nilai >= 75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def tampilkan_data(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        print("Nilai   :", self.nilai)
        print("Status  :", self.cek_status())
        print("-" * 30)


# Membuat minimal 3 objek mahasiswa
mahasiswa1 = Mahasiswa("Andi", "12345", "Teknik Informatika", 85)
mahasiswa2 = Mahasiswa("Budi", "12346", "Teknik Informatika", 70)
mahasiswa3 = Mahasiswa("Citra", "12347", "Teknik Informatika", 90)

# Menampilkan data mahasiswa
mahasiswa1.tampilkan_data()
mahasiswa2.tampilkan_data()
mahasiswa3.tampilkan_data()