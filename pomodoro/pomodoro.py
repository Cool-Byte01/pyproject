#!/usr/bin/env python3
import time
from os import system


def menu():
    # fungsi menu untuk menampilkan fitur yang tersedia.

    print("""
    Selamat Datang!
    ------- MENU -------
    1. Belajar (25 menit)
    2. Istirahat Pendek (5 menit)
    3. Istirahat Panjang (15 menit)
    4. Keluar
    --------------------
    """)


def clear_screen():
    system("clear")


def timer(durasi: int | float):
    """
    fungsi timer untuk menghitung waktu belajar,
    istirahat pendek dan panjang. kemudian memungculkan
    notifikasi ketikawaktu selesai.
    """

    while durasi > 0:
        menit, detik = divmod(durasi, 60)
        print(f"Waktu Tersisa: {menit:02d}:{detik:02d}", end="\r")

        time.sleep(1)
        durasi -= 1
    system("~/pyroject/notif.sh")  # execute shell script


def main():
    # fungsi main adalah fungsi utama untuk menjalankan program.

    while True:
        clear_screen()
        menu()

        try:
            pilih = int(input("Masukkan Pilihan (1-4): "))

            if pilih == 1:
                clear_screen()
                print("\nWaktu Belajar Dimulai!")
                timer(25 * 60)

            elif pilih == 2:
                clear_screen()
                print("\nWaktu Istirahat Pendek Dimulai!")
                timer(5 * 60)

            elif pilih == 3:
                clear_screen()
                print("\nWaktu Istirahat Panjang Dimulai!")
                timer(15 * 60)

            elif pilih == 4:
                print("\nKeluar dari program.")
                clear_screen()
                break

            else:
                print("\nPastikan anda memasukkan angka dari 1 - 4!")
                input("Tekan enter untuk melanjutkan -> ")

        except ValueError:
            print("\nPastikan anda memasukkan angka dari 1 - 4!")
            input("Tekan enter untuk melanjutkan -> ")


if __name__ == "__main__":
    main()
