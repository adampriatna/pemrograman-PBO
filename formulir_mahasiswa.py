import tkinter as tk
from tkinter import ttk, messagebox

# Membuat jendela utama
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("500x540")
root.configure(bg="#EAF2F8")
root.resizable(False, False)

# Pengaturan warna
warna_bg = "#EAF2F8"
warna_judul = "#154360"
warna_simpan = "#2874A6"
warna_reset = "#D4AC0D"
warna_keluar = "#C0392B"

# Judul aplikasi
judul = tk.Label(
    root,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 15, "bold"),
    bg=warna_bg,
    fg=warna_judul
)
judul.grid(row=0, column=0, columnspan=2, pady=20)

# Frame formulir
form = tk.Frame(root, bg=warna_bg)
form.grid(row=1, column=0, columnspan=2, padx=25, sticky="w")

# Input Nama
tk.Label(
    form,
    text="Nama",
    bg=warna_bg,
    font=("Arial", 10)
).grid(row=0, column=0, sticky="w", pady=8)

nama = tk.Entry(form, width=32, font=("Arial", 10))
nama.grid(row=0, column=1, padx=10, pady=8)

# Input NIM
tk.Label(
    form,
    text="NIM",
    bg=warna_bg,
    font=("Arial", 10)
).grid(row=1, column=0, sticky="w", pady=8)

nim = tk.Entry(form, width=32, font=("Arial", 10))
nim.grid(row=1, column=1, padx=10, pady=8)

# Pilihan Program Studi
tk.Label(
    form,
    text="Program Studi",
    bg=warna_bg,
    font=("Arial", 10)
).grid(row=2, column=0, sticky="w", pady=8)

prodi = ttk.Combobox(
    form,
    values=["Informatika", "Manajemen", "Akuntansi"],
    state="readonly",
    width=29,
    font=("Arial", 10)
)
prodi.grid(row=2, column=1, padx=10, pady=8)

# Input Alamat menggunakan Text
tk.Label(
    form,
    text="Alamat",
    bg=warna_bg,
    font=("Arial", 10)
).grid(row=3, column=0, sticky="nw", pady=8)

alamat = tk.Text(
    form,
    width=24,
    height=4,
    font=("Arial", 10)
)
alamat.grid(row=3, column=1, padx=10, pady=8, sticky="w")

# Label untuk menampilkan hasil
hasil = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="white",
    fg=warna_judul,
    justify="left",
    anchor="w",
    width=48,
    height=6,
    relief="groove",
    padx=8,
    pady=5
)
hasil.grid(
    row=2,
    column=0,
    columnspan=2,
    padx=20,
    pady=12
)

# Fungsi Simpan
def simpan():
    nama_input = nama.get().strip()
    nim_input = nim.get().strip()
    prodi_input = prodi.get()
    alamat_input = alamat.get("1.0", tk.END).strip()

    # Validasi Nama dan NIM
    if not nama_input or not nim_input:
        messagebox.showwarning(
            "Peringatan",
            "Nama dan NIM tidak boleh kosong!"
        )
        return

    if not prodi_input:
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih Program Studi!"
        )
        return

    # Menampilkan hasil input
    hasil.config(
        text=(
            f"Nama           : {nama_input}\n"
            f"NIM              : {nim_input}\n"
            f"Program Studi : {prodi_input}\n"
            f"Alamat          : {alamat_input or '-'}"
        )
    )

# Fungsi Reset
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="")

# Fungsi Keluar
def keluar():
    konfirmasi = messagebox.askyesno(
        "Konfirmasi",
        "Apakah Anda yakin ingin keluar?"
    )

    if konfirmasi:
        root.destroy()

# Frame tombol
tombol = tk.Frame(root, bg=warna_bg)
tombol.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)

# Tombol Simpan
tk.Button(
    tombol,
    text="Simpan",
    command=simpan,
    bg=warna_simpan,
    fg="white",
    width=10,
    font=("Arial", 10, "bold")
).grid(row=0, column=0, padx=5)

# Tombol Reset
tk.Button(
    tombol,
    text="Reset",
    command=reset,
    bg=warna_reset,
    fg="white",
    width=10,
    font=("Arial", 10, "bold")
).grid(row=0, column=1, padx=5)

# Tombol Keluar
tk.Button(
    tombol,
    text="Keluar",
    command=keluar,
    bg=warna_keluar,
    fg="white",
    width=10,
    font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=5)

# Menjalankan aplikasi
root.mainloop()