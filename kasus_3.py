class Pegawai:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek


class ProjectManager(Pegawai, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def tampilkan_data(self):
        print("ID Pegawai :", self.id_pegawai)
        print("Nama       :", self.nama)
        print("Gaji       :", self.gaji)
        print("Nama Proyek:", self.nama_proyek)


# Membuat objek Project Manager
pm = ProjectManager(
    "PM001",
    "Muhammad Adam ",
    8000000,
    "Sistem Informasi Akademik"
)

print("=== DATA PROJECT MANAGER ===")
pm.tampilkan_data()