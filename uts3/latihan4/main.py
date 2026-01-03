# main.py

from utils import hitung_diskon

print("=== Program Diskon Belanja ===")

total_belanja = float(input("Masukkan total belanja (Rp): "))

diskon, potongan, total_bayar = hitung_diskon(total_belanja)

print("\n--- Rincian Belanja ---")
print(f"Total Belanja : Rp {total_belanja:,.0f}")
print(f"Diskon        : {int(diskon * 100)}%")
print(f"Potongan      : Rp {potongan:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")