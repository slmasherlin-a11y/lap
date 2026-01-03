# utils.py

def format_desimal(angka, jumlah_koma):
    """
    Mengatur jumlah angka di belakang koma
    """
    format_string = "{:." + str(jumlah_koma) + "f}"
    return format_string.format(angka)