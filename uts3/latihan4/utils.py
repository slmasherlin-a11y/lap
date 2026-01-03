def hitung_diskon(total_belanja):
    """
    Aturan diskon:
    - Belanja >= 500000 → diskon 20%
    - Belanja >= 300000 → diskon 15%
    - Belanja >= 100000 → diskon 10%
    - Selain itu → tidak ada diskon
    """
    if total_belanja >= 500000:
        diskon = 0.20
    elif total_belanja >= 300000:
        diskon = 0.15
    elif total_belanja >= 100000:
        diskon = 0.10
    else:
        diskon = 0

    potongan = total_belanja * diskon
    total_bayar = total_belanja - potongan

    return diskon, potongan, total_bayar