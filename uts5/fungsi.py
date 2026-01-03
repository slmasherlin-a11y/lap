import math

def volume_kubus(s):
    return s ** 3

def volume_balok(p, l, t):
    return p * l * t

def volume_tabung(r, t):
    return math.pi * r * r * t

def volume_kerucut(r, t):
    return (1/3) * math.pi * r * r * t

def volume_bola(r):
    return (4/3) * math.pi * r ** 3

def volume_prisma_segitiga(luas_alas, t):
    return luas_alas * t

def volume_limas_segiempat(luas_alas, t):
    return (1/3) * luas_alas * t

def volume_prisma_segiempat(p, l, t):
    return p * l * t

def volume_limas_segitiga(luas_alas, t):
    return (1/3) * luas_alas * t

def volume_setengah_bola(r):
    return (2/3) * math.pi * r ** 3