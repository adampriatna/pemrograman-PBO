import os

# 1. Menampilkan lokasi folder aktif saat ini
print("--- 1. Lokasi Folder Aktif ---")
print("Lokasi saat ini:", os.getcwd())

# 2. Melihat isi folder saat ini
print("\n--- 2. Isi Folder Saat Ini ---")
print(os.listdir())

# 3. Membuat folder baru (misal: 'data' dan 'docs')
print("\n--- 3. Membuat Folder Baru ---")
if not os.path.exists("data"):
    os.mkdir("data")
    print("Folder 'data' berhasil dibuat.")

if not os.path.exists("docs"):
    os.mkdir("docs")
    print("Folder 'docs' berhasil dibuat.")

# 4. Mengubah nama folder
print("\n--- 4. Mengubah Nama Folder ---")
if os.path.exists("docs"):
    os.rename("docs", "documents")
    print("Folder 'docs' diubah namanya menjadi 'documents'.")

# 5. Menghapus file/folder (contoh menghapus folder 'documents')
print("\n--- 5. Menghapus Folder ---")
if os.path.exists("documents"):
    os.rmdir("documents")
    print("Folder 'documents' berhasil dihapus.")
