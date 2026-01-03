# utils.py

def hitung_total_barang(jumlah_barang):
    total = 0
    for i in range(1, jumlah_barang + 1):
        harga = float(input(f"  Masukkan harga barang ke-{i}: Rp "))
        total += harga
    return total