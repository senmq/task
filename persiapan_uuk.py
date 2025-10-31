# Nama: Rifky Adi Pranata
# Kelas: X PPLG

# [!] Tugas membuat CRUD menggunakan Python


# --------------------------------------------------
# Step 0: Import modules
# --------------------------------------------------
import os
import shutil
import time


# --------------------------------------------------
# Step 1: CRUD (Create, Read, Update, Delete)
# --------------------------------------------------
def create(data):
    nama: str = input("Masukkan nama : ")
    kelas: str = input("Masukkan kelas: ")
    umur: int = int(input("Masukkan umur : "))

    siswa_baru = {"nama": nama, "kelas": kelas, "umur": umur}
    data.append(siswa_baru)

    print("Data siswa berhasil ditambahkan.")


def read(data):
    if not data:
        print("Data tidak ditemukan.")
    else:
        print("Daftar Siswa:")
        print("-" * 30)
        for indeks, siswa in enumerate(data):
            print(f"[{indeks:02}] Nama : {siswa['nama']}")
            print(f"     Kelas: {siswa['kelas']}")
            print(f"     Umur : {siswa['umur']}\n")


def update(data):
    if not data:
        read(data)
    else:
        read(data)

        pilihan: int = int(input("Pilih indeks data yang ingin diubah: "))

        if pilihan >= 0 and pilihan < len(data):
            nama_baru: str = input("Masukkan nama baru : ")
            kelas_baru: str = input("Masukkan kelas baru: ")
            umur_baru: int = int(input("Masukkan umur baru : "))

            data[pilihan] = {"nama": nama_baru, "kelas": kelas_baru, "umur": umur_baru}
            print("Data siswa berhasil diubah.")
        else:
            print("Nomor indeks tidak valid.")


def delete(data):
    if not data:
        read(data)
    else:
        read(data)

        pilihan: int = int(input("Pilih indeks data yang ingin dihapus: "))

        if pilihan >= 0 and pilihan < len(data):
            konfirmasi = input(
                "Apakah anda yakin ingin menghapus data tersebut? (y/n): "
            )
            if konfirmasi.lower() == "y":
                del data[pilihan]
                print("Data siswa berhasil dihapus.")
        else:
            print("Nomor indeks tidak valid.")


# --------------------------------------------------
# Step 2: Main menu
# --------------------------------------------------
def menu():
    siswa = []
    terminal_width = shutil.get_terminal_size().columns

    MENU_OPTIONS = {
        1: ("Read", read),
        2: ("Create", create),
        3: ("Update", update),
        4: ("Delete", delete),
        5: ("Exit", None),
    }

    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")

            print("=" * terminal_width)
            print(
                "|" + "SISWA SMK TI AIRLANGGA (CRUD)".center(terminal_width - 2) + "|"
            )
            print("=" * terminal_width)
            print("Menu utama:")
            print("-" * 30)

            for key, (label, _) in MENU_OPTIONS.items():
                print(f"[{key}] {label}")

            print("-" * 30)

            pilihan: int = int(input("Masukkan pilihan [1-5]: "))

            os.system("cls" if os.name == "nt" else "clear")

            label, fungsi = MENU_OPTIONS[pilihan]
            if pilihan == 5:
                print("Keluar dari program...")
                time.sleep(0.5)
                break
            else:
                print("Inisialisasi fungsi...")
                time.sleep(0.5)
                fungsi(siswa)

            input("Tekan Enter untuk kembali ke menu...")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input("Tekan Enter untuk kembali ke menu...")


# --------------------------------------------------
# Step 3: Run the code
# --------------------------------------------------
if __name__ == "__main__":
    menu()
