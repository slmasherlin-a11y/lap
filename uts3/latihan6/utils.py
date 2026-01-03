# utils.py

def hitung_pajak(total_belanja):
    """
    Aturan pajak:
    - Pajak 10% dari total belanja
    """
    pajak = 0.10
    jumlah_pajak = total_belanja * pajak
    total_bayar = total_belanja + jumlah_pajak

    return pajak, jumlah_pajak, total_bayar