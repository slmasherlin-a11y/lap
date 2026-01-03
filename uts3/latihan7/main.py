# main.py

from utils import format_desimal

print("=== Program Angka Desimal ===")

angka = float(input("Masukkan angka desimal: "))
jumlah_koma = int(input("Masukkan jumlah angka di belakang koma: "))

hasil = format_desimal(angka, jumlah_koma)

print("\n--- Hasil ---")
print(f"Angka awal           : {angka}")
print(f"Jumlah koma dipilih  : {jumlah_koma}")
print(f"Hasil format desimal : {hasil}")