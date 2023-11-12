import math


def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)


while True:
    print("Program menghitung luas segitiga dan luas lingkaran")
    print("=====================================================")
    print("========== CREATED BY 222362 MOCH ACHMAR ==========")
    print("=====================================================")
    alas = float(input("Masukkan nilai alas segitiga : "))
    tinggi = float(input("Masukkan nilai tinggi segitiga : "))
    jari_jari = float(input("Masukkan jari-jari lingkaran : "))

    print("Luas segitiga = ", luas_segitiga(alas, tinggi))
    print("Luas lingkaran = ", luas_lingkaran(jari_jari))

    ulangi = input("Apakah ingin menghitung lagi? (Y/N) ")
    if ulangi.lower() not in ["y", "yes"]:
        break

print("Makasih sudah memakai program ini!")
