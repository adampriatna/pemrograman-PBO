# 1. CLASS PETUGAS (Perpustakaan)
class Petugas:
    def __init__(self, nama, id_petugas):
        self.nama = nama
        self.id_petugas = id_petugas
    def proses_peminjaman(self):
        print("nama petugas       : ", self.nama)
        print("id petugas         : ", self.id_petugas)

p1 = Petugas("Budi", "P001")
p1.proses_peminjaman()


# 2. CLASS TRANSAKSI PINJAM (Perpustakaan)
class TransaksiPinjam:

    def __init__(self, id_transaksi, tanggal_pinjam):
        self.id_transaksi = id_transaksi
        self.tanggal_pinjam = tanggal_pinjam
    def hitung_denda(self):
        print("id transaksi       : ", self.id_transaksi)
        print("tanggal peminjaman : ", self.tanggal_pinjam)

t1 = TransaksiPinjam("TRX99", "15-09-2026")
t1.hitung_denda()


# 3. CLASS BARANG (Kasir)
class Barang:

    def __init__(self, nama_barang, harga):
        self.nama_barang = nama_barang
        self.harga = harga
    def tampilkan_detail(self):
        print("nama barang        : ", self.nama_barang)
        print("harga barang       : ", self.harga)

b1 = Barang("Kopi", 15000)
b1.tampilkan_detail()


# 4. CLASS PELANGGAN (Kasir)
class Pelanggan:

    def __init__(self, nama, poin_member):
        self.nama = nama
        self.poin_member = poin_member
    def tambah_poin(self):
        print("nama penlanggan    : ", self.nama)
        print("poin memeber       : ", self.poin_member)

pel1 = Pelanggan("aisyah", 150)
pel1.tambah_poin()


# 5. CLASS DOSEN (Sistem Kelas)
class Dosen:

    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
    def input_nilai(self):
        print("nama dosen         : ", self.nama)
        print("nip                : ", self.nip)

d1 = Dosen("Dr. sayyid", "19850101")
d1.input_nilai()
