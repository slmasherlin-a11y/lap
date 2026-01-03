# main.py

from utils import hitung_total_barang

print("=== Program Pembelian Barang Konsumen ===")

jumlah_konsumen = int(input("Masukkan jumlah konsumen: "))

total_semua_konsumen = 0

for k in range(1, jumlah_konsumen + 1):
    print(f"\nKonsumen ke-{k}")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

    total_konsumen = hitung_total_barang(jumlah_barang)
    total_semua_konsumen += total_konsumen

    print(f"Total belanja konsumen ke-{k}: Rp {total_konsumen:,.2f}")

print("\n=== Ringkasan ===")
print(f"Jumlah konsumen       : {jumlah_konsumen}")
print(f"Total seluruh belanja : Rp {total_semua_konsumen:,.2f}")