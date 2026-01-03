import fungsi

print("=== PROGRAM KELILING BANGUN DATAR ===")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")
print("5. Jajar Genjang")
print("6. Belah Ketupat")
print("7. Layang-layang")
print("8. Trapesium")
print("9. Setengah Lingkaran")
print("10. Segi Lima")
print("0. keluar")

pilih = int(input("Pilih bangun (1-10): "))

if pilih == 1:
    s = float(input("Sisi: "))
    hasil = fungsi.keliling_persegi(s)

elif pilih == 2:
    p = float(input("Panjang: "))
    l = float(input("Lebar: "))
    hasil = fungsi.keliling_persegi_panjang(p, l)

elif pilih == 3:
    a = float(input("Sisi a: "))
    b = float(input("Sisi b: "))
    c = float(input("Sisi c: "))
    hasil = fungsi.keliling_segitiga(a, b, c)

elif pilih == 4:
    r = float(input("Jari-jari: "))
    hasil = fungsi.keliling_lingkaran(r)

elif pilih == 5:
    a = float(input("Alas: "))
    b = float(input("Sisi miring: "))
    hasil = fungsi.keliling_jajar_genjang(a, b)

elif pilih == 6:
    s = float(input("Sisi: "))
    hasil = fungsi.keliling_belah_ketupat(s)

elif pilih == 7:
    a = float(input("Sisi a: "))
    b = float(input("Sisi b: "))
    hasil = fungsi.keliling_layang_layang(a, b)

elif pilih == 8:
    a = float(input("Sisi a: "))
    b = float(input("Sisi b: "))
    c = float(input("Sisi c: "))
    d = float(input("Sisi d: "))
    hasil = fungsi.keliling_trapesium(a, b, c, d)

elif pilih == 9:
    r = float(input("Jari-jari: "))
    hasil = fungsi.keliling_setengah_lingkaran(r)

elif pilih == 10:
    s = float(input("Sisi: "))
    hasil = fungsi.keliling_segi_lima(s)
elif pilih == 0:
    print("program selesai")

else:
    print("Pilihan tidak valid!")