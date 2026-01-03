import fungsi

print("=== PROGRAM VOLUME BANGUN RUANG ===")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")
print("4. Kerucut")
print("5. Bola")
print("6. Prisma Segitiga")
print("7. Limas Segiempat")
print("8. Prisma Segiempat")
print("9. Limas Segitiga")
print("10. Setengah Bola")

pilih = int(input("Pilih bangun ruang (1-10): "))

if pilih == 1:
    s = float(input("Sisi: "))
    hasil = fungsi.volume_kubus(s)

elif pilih == 2:
    p = float(input("Panjang: "))
    l = float(input("Lebar: "))
    t = float(input("Tinggi: "))
    hasil = fungsi.volume_balok(p, l, t)

elif pilih == 3:
    r = float(input("Jari-jari: "))
    t = float(input("Tinggi: "))
    hasil = fungsi.volume_tabung(r, t)

elif pilih == 4:
    r = float(input("Jari-jari: "))
    t = float(input("Tinggi: "))
    hasil = fungsi.volume_kerucut(r, t)

elif pilih == 5:
    r = float(input("Jari-jari: "))
    hasil = fungsi.volume_bola(r)

elif pilih == 6:
    luas_alas = float(input("Luas alas segitiga: "))
    t = float(input("Tinggi prisma: "))
    hasil = fungsi.volume_prisma_segitiga(luas_alas, t)

elif pilih == 7:
    luas_alas = float(input("Luas alas segiempat: "))
    t = float(input("Tinggi limas: "))
    hasil = fungsi.volume_limas_segiempat(luas_alas, t)

elif pilih == 8:
    p = float(input("Panjang: "))
    l = float(input("Lebar: "))
    t = float(input("Tinggi: "))
    hasil = fungsi.volume_prisma_segiempat(p, l, t)

elif pilih == 9:
    luas_alas = float(input("Luas alas segitiga: "))
    t = float(input("Tinggi limas: "))
    hasil = fungsi.volume_limas_segitiga(luas_alas, t)

elif pilih == 10:
    r = float(input("Jari-jari: "))
    hasil = fungsi.volume_setengah_bola(r)

else:
    hasil = None
    print("Pilihan tidak valid!")

if hasil is not None:
    print("Volume =", hasil)