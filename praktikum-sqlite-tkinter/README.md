Aplikasi Penyimpanan Data Mahasiswa
Aplikasi desktop sederhana untuk mengelola data mahasiswa menggunakan Python, Tkinter, dan SQLite. Aplikasi ini dibuat sebagai tugas praktikum Dasar SQLite dan Integrasi dengan Tkinter.

Teknologi yang Digunakan
- Python 3
- Tkinter
- SQLite
- DB Browser for SQLite

Fitur Aplikasi
- Menambahkan data mahasiswa.
- Menampilkan data mahasiswa dalam bentuk tabel.
- Mengubah data mahasiswa.
- Menghapus data mahasiswa.
- Mencari mahasiswa berdasarkan nama atau NIM.
- Memvalidasi data yang wajib diisi.
- Mencegah penggunaan NIM yang sama.
- Menyimpan data secara permanen menggunakan SQLite.
- Menambahkan informasi angkatan mahasiswa.

Struktur Data
Database: "mahasiswa.db"
Tabel: "mahasiswa"

Kolom yang digunakan:
Kolom| Keterangan
id| ID mahasiswa
nama| Nama mahasiswa
nim| Nomor Induk Mahasiswa
prodi| Program Studi
alamat| Alamat mahasiswa
angkatan| Tahun angkatan

Cara Menjalankan Aplikasi
1. Pastikan Python 3 sudah terpasang.
2. Buka folder proyek melalui VS Code atau terminal.
3. Jalankan perintah berikut:

python aplikasi_mahasiswa.py
4. Jendela aplikasi akan terbuka.
5. Masukkan data mahasiswa melalui formulir yang tersedia.

Database "mahasiswa.db" akan dibuat secara otomatis apabila belum tersedia.

Pengujian
Pengujian aplikasi dilakukan berdasarkan beberapa skenario, yaitu:

1. Menyimpan data mahasiswa.
2. Menguji formulir dengan masukan kosong.
3. Menguji NIM duplikat.
4. Menguji tombol Refresh.
5. Menguji fitur hapus data.
6. Menguji fitur ubah data.
7. Memastikan data tetap tersimpan setelah aplikasi dibuka kembali.
8. Memeriksa isi database melalui DB Browser for SQLite.

Pengembangan
Aplikasi dikembangkan dengan menambahkan fitur pencarian berdasarkan nama atau NIM serta kolom angkatan mahasiswa.

File Proyek
- "aplikasi_mahasiswa.py" — kode program aplikasi.
- "mahasiswa.db" — database penyimpanan data mahasiswa.
- "README.md" — dokumentasi proyek.

Penutup
Melalui praktikum ini, saya belajar menghubungkan Python Tkinter dengan SQLite untuk membuat aplikasi yang dapat menyimpan dan mengelola data mahasiswa. Saya juga mempelajari penggunaan perintah SQL seperti INSERT, SELECT, UPDATE, dan DELETE.


PERTANYAAN REFLEKSI

1. Jelaskan peran connect(), execute(), dan commit() dalam proses penyimpanan data pada aplikasi yang Anda buat.
Menurut saya, connect() berfungsi untuk menghubungkan aplikasi dengan database. execute() digunakan untuk menjalankan perintah seperti menyimpan, menampilkan, mengubah, dan menghapus data. Sedangkan commit() digunakan untuk menyimpan perubahan agar data benar-benar masuk ke database.

2. Bagian mana dari praktikum ini yang paling menantang bagi Anda? Bagaimana cara Anda mengatasinya?
Bagian yang paling sulit menurut saya adalah menghubungkan aplikasi Tkinter dengan database SQLite, terutama saat membuat fitur tambah, ubah, dan hapus data. Untuk mengatasinya, saya mencoba mengikuti langkah-langkah pada modul, memeriksa kembali kode, dan mencoba menjalankan aplikasinya sampai fitur-fiturnya bisa digunakan.

3. Jika aplikasi ini akan digunakan oleh bagian administrasi program studi, fitur atau perlindungan data apa yang menurut Anda perlu ditambahkan?
Menurut saya, aplikasi ini perlu ditambahkan fitur login agar data mahasiswa tidak bisa dibuka oleh sembarang orang. Selain itu, perlu ada fitur pencadangan data supaya data tetap aman jika terjadi masalah pada komputer. Fitur pencarian juga bisa dikembangkan agar petugas lebih mudah menemukan data mahasiswa.