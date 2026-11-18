import sqlite3
import tkinter as tk
from contextlib import contextmanager
from tkinter import ttk, messagebox

DB_NAME = "mahasiswa.db"
DAFTAR_PRODI = [
    "Informatika",
    "Sistem Informasi",
    "Manajemen",
    "Akuntansi"
]


# ==========================================
# 1. KONEKSI DATABASE
# ==========================================

@contextmanager
def koneksi():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ==========================================
# 2. MEMBUAT DAN MEMPERBARUI TABEL
# ==========================================

def buat_tabel():
    with koneksi() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS mahasiswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                nim TEXT NOT NULL UNIQUE,
                prodi TEXT NOT NULL,
                alamat TEXT,
                angkatan INTEGER
            )
        """)

        # Memeriksa apakah database lama sudah memiliki kolom angkatan
        kolom = [
            row[1]
            for row in conn.execute(
                "PRAGMA table_info(mahasiswa)"
            ).fetchall()
        ]

        if "angkatan" not in kolom:
            conn.execute(
                "ALTER TABLE mahasiswa ADD COLUMN angkatan INTEGER"
            )


buat_tabel()


# ==========================================
# 3. JENDELA DAN FORMULIR
# ==========================================

root = tk.Tk()
root.title("Aplikasi Data Mahasiswa")
root.geometry("1000x650")

form = ttk.LabelFrame(
    root,
    text="Formulir Mahasiswa",
    padding=12
)
form.pack(fill="x", padx=15, pady=12)

ttk.Label(form, text="Nama").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
entry_nama = ttk.Entry(form, width=30)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form, text="NIM").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
entry_nim = ttk.Entry(form, width=30)
entry_nim.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form, text="Program Studi").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
combo_prodi = ttk.Combobox(
    form,
    values=DAFTAR_PRODI,
    state="readonly",
    width=27
)
combo_prodi.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form, text="Alamat").grid(
    row=1, column=2, padx=5, pady=5, sticky="w"
)
entry_alamat = ttk.Entry(form, width=30)
entry_alamat.grid(row=1, column=3, padx=5, pady=5)

ttk.Label(form, text="Angkatan").grid(
    row=2, column=0, padx=5, pady=5, sticky="w"
)
entry_angkatan = ttk.Entry(form, width=30)
entry_angkatan.grid(row=2, column=1, padx=5, pady=5)


# ==========================================
# 4. FITUR PENCARIAN
# ==========================================

frame_cari = ttk.LabelFrame(
    root,
    text="Pencarian Mahasiswa",
    padding=10
)
frame_cari.pack(fill="x", padx=15, pady=5)

ttk.Label(
    frame_cari,
    text="Cari Nama atau NIM:"
).pack(side="left", padx=5)

entry_cari = ttk.Entry(frame_cari, width=35)
entry_cari.pack(side="left", padx=5)


# ==========================================
# 5. TABEL TAMPILAN
# ==========================================

kolom = (
    "id",
    "nama",
    "nim",
    "prodi",
    "alamat",
    "angkatan"
)

tabel = ttk.Treeview(
    root,
    columns=kolom,
    show="headings"
)

daftar_judul = [
    ("id", "ID"),
    ("nama", "Nama"),
    ("nim", "NIM"),
    ("prodi", "Program Studi"),
    ("alamat", "Alamat"),
    ("angkatan", "Angkatan")
]

for key, judul in daftar_judul:
    tabel.heading(
        key,
        text=judul,
        anchor="w"
    )

# Mengatur lebar dan posisi isi setiap kolom
tabel.column("id", width=60, anchor="w")
tabel.column("nama", width=150, anchor="w")
tabel.column("nim", width=150, anchor="w")
tabel.column("prodi", width=180, anchor="w")
tabel.column("alamat", width=180, anchor="w")
tabel.column("angkatan", width=100, anchor="w")

tabel.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=8
)


# ==========================================
# 6. MENAMPILKAN DATA
# ==========================================

def tampilkan_data(kata_kunci=""):
    for item in tabel.get_children():
        tabel.delete(item)

    with koneksi() as conn:
        if kata_kunci:
            rows = conn.execute(
                """
                SELECT id, nama, nim, prodi, alamat, angkatan
                FROM mahasiswa
                WHERE nama LIKE ? OR nim LIKE ?
                ORDER BY id DESC
                """,
                (
                    f"%{kata_kunci}%",
                    f"%{kata_kunci}%"
                )
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT id, nama, nim, prodi, alamat, angkatan
                FROM mahasiswa
                ORDER BY id DESC
                """
            ).fetchall()

    for row in rows:
        data = list(row)
        data[5] = data[5] if data[5] is not None else ""
        tabel.insert("", tk.END, values=data)


# ==========================================
# 7. FUNGSI PENCARIAN
# ==========================================

def cari_data():
    kata_kunci = entry_cari.get().strip()
    tampilkan_data(kata_kunci)


def reset_pencarian():
    entry_cari.delete(0, tk.END)
    tampilkan_data()


# ==========================================
# 8. MEMBERSIHKAN FORMULIR
# ==========================================

def bersihkan_form():
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)
    combo_prodi.set("")
    entry_alamat.delete(0, tk.END)
    entry_angkatan.delete(0, tk.END)
    entry_nama.focus_set()


# ==========================================
# 9. MENYIMPAN DATA
# ==========================================

def simpan_data():
    nama = entry_nama.get().strip()
    nim = entry_nim.get().strip()
    prodi = combo_prodi.get().strip()
    alamat = entry_alamat.get().strip()
    angkatan_text = entry_angkatan.get().strip()

    if not nama or not nim or not prodi:
        messagebox.showwarning(
            "Validasi",
            "Nama, NIM, dan Program Studi wajib diisi."
        )
        return

    if angkatan_text and not angkatan_text.isdigit():
        messagebox.showwarning(
            "Validasi",
            "Angkatan harus berupa angka."
        )
        return

    angkatan = int(angkatan_text) if angkatan_text else None

    try:
        with koneksi() as conn:
            conn.execute(
                """
                INSERT INTO mahasiswa
                (nama, nim, prodi, alamat, angkatan)
                VALUES (?, ?, ?, ?, ?)
                """,
                (nama, nim, prodi, alamat, angkatan)
            )

        messagebox.showinfo(
            "Berhasil",
            "Data berhasil disimpan."
        )

        tampilkan_data(entry_cari.get().strip())
        bersihkan_form()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "NIM Duplikat",
            "NIM sudah terdaftar."
        )

    except sqlite3.Error as error:
        messagebox.showerror(
            "Kesalahan Database",
            str(error)
        )


# ==========================================
# 10. MENGHAPUS DATA
# ==========================================

def hapus_data():
    pilihan = tabel.selection()

    if not pilihan:
        messagebox.showwarning(
            "Pilih Data",
            "Pilih baris yang akan dihapus."
        )
        return

    data = tabel.item(pilihan[0], "values")
    record_id = int(data[0])

    if not messagebox.askyesno(
        "Konfirmasi",
        f"Hapus data {data[1]}?"
    ):
        return

    with koneksi() as conn:
        conn.execute(
            "DELETE FROM mahasiswa WHERE id = ?",
            (record_id,)
        )

    tampilkan_data(entry_cari.get().strip())
    bersihkan_form()


# ==========================================
# 11. MEMUAT DATA TERPILIH KE FORM
# ==========================================

def isi_form_dari_tabel(event=None):
    pilihan = tabel.selection()

    if not pilihan:
        return

    record_id = int(
        tabel.item(pilihan[0], "values")[0]
    )

    with koneksi() as conn:
        row = conn.execute(
            """
            SELECT nama, nim, prodi, alamat, angkatan
            FROM mahasiswa
            WHERE id = ?
            """,
            (record_id,)
        ).fetchone()

    if row is None:
        return

    bersihkan_form()

    entry_nama.insert(0, row[0])
    entry_nim.insert(0, row[1])
    combo_prodi.set(row[2])
    entry_alamat.insert(0, row[3] or "")

    if row[4] is not None:
        entry_angkatan.insert(0, str(row[4]))


# ==========================================
# 12. MENGUBAH DATA
# ==========================================

def ubah_data():
    pilihan = tabel.selection()

    if not pilihan:
        messagebox.showwarning(
            "Pilih Data",
            "Pilih data yang akan diubah."
        )
        return

    record_id = int(
        tabel.item(pilihan[0], "values")[0]
    )

    nama = entry_nama.get().strip()
    nim = entry_nim.get().strip()
    prodi = combo_prodi.get().strip()
    alamat = entry_alamat.get().strip()
    angkatan_text = entry_angkatan.get().strip()

    if not nama or not nim or not prodi:
        messagebox.showwarning(
            "Validasi",
            "Nama, NIM, dan Program Studi wajib diisi."
        )
        return

    if angkatan_text and not angkatan_text.isdigit():
        messagebox.showwarning(
            "Validasi",
            "Angkatan harus berupa angka."
        )
        return

    angkatan = int(angkatan_text) if angkatan_text else None

    try:
        with koneksi() as conn:
            conn.execute(
                """
                UPDATE mahasiswa
                SET nama = ?, nim = ?, prodi = ?,
                    alamat = ?, angkatan = ?
                WHERE id = ?
                """,
                (
                    nama,
                    nim,
                    prodi,
                    alamat,
                    angkatan,
                    record_id
                )
            )

        tampilkan_data(entry_cari.get().strip())
        bersihkan_form()

        messagebox.showinfo(
            "Berhasil",
            "Data berhasil diperbarui."
        )

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "NIM Duplikat",
            "NIM sudah digunakan data lain."
        )

    except sqlite3.Error as error:
        messagebox.showerror(
            "Kesalahan Database",
            str(error)
        )


# ==========================================
# 13. MENGHUBUNGKAN TABEL DENGAN FORM
# ==========================================

tabel.bind(
    "<<TreeviewSelect>>",
    isi_form_dari_tabel
)


# ==========================================
# 14. TOMBOL APLIKASI
# ==========================================

baris_tombol = ttk.Frame(root)
baris_tombol.pack(
    fill="x",
    padx=15,
    pady=5
)

ttk.Button(
    frame_cari,
    text="Cari",
    command=cari_data
).pack(side="left", padx=5)

ttk.Button(
    frame_cari,
    text="Reset Pencarian",
    command=reset_pencarian
).pack(side="left", padx=5)

ttk.Button(
    baris_tombol,
    text="Simpan Data",
    command=simpan_data
).pack(side="left", padx=4)

ttk.Button(
    baris_tombol,
    text="Ubah Data",
    command=ubah_data
).pack(side="left", padx=4)

ttk.Button(
    baris_tombol,
    text="Refresh",
    command=reset_pencarian
).pack(side="left", padx=4)

ttk.Button(
    baris_tombol,
    text="Bersihkan Form",
    command=bersihkan_form
).pack(side="left", padx=4)

ttk.Button(
    baris_tombol,
    text="Hapus Data Terpilih",
    command=hapus_data
).pack(side="right", padx=4)


# ==========================================
# 15. MENJALANKAN APLIKASI
# ==========================================

tampilkan_data()
root.mainloop()