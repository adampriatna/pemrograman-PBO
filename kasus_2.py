class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def tampilkan_data(self):
        print("Nama       :", self.nama)
        print("Merk       :", self.merk)
        print("Tahun      :", self.tahun)
        print("Kecepatan  :", self.kecepatan, "km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Jumlah Kursi:", self.jumlah_kursi)


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def tampilkan_data(self):
        super().tampilkan_data()
        print("Tipe Motor :", self.tipe_motor)


# Membuat objek
mobil = Mobil("Avanza", "Toyota", 2022, 180, 7)
motor = Motor("Vario", "Honda", 2023, 120, "Matic")

# Menampilkan data
print("=== DATA MOBIL ===")
mobil.tampilkan_data()

print("\n=== DATA MOTOR ===")
motor.tampilkan_data()