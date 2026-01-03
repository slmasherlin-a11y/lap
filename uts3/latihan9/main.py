# main.py

from utils import hitung_rata_rata

print("=== Program Nilai Mahasiswa ===")

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

daftar_nilai = []

for i in range(jumlah_mahasiswa):
    nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
    daftar_nilai.append(nilai)

total_nilai, rata_rata = hitung_rata_rata(daftar_nilai)

print("\n--- Hasil Perhitungan ---")
print(f"Jumlah Mahasiswa : {jumlah_mahasiswa}")
print(f"Total Nilai      : {total_nilai}")
print(f"Nilai Rata-rata  : {rata_rata:.2f}")