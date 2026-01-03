# main.py

from utils import hitung_pajak

print("=== Program Pajak Belanja ===")

total_belanja = float(input("Masukkan total belanja (Rp): "))

pajak, jumlah_pajak, total_bayar = hitung_pajak(total_belanja)

print("\n--- Rincian Pembayaran ---")
print(f"Total Belanja : Rp {total_belanja:,.0f}")
print(f"Pajak         : {int(pajak * 100)}%")
print(f"Jumlah Pajak  : Rp {jumlah_pajak:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")