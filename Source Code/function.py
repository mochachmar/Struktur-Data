# def LuasSegiempat(panjang, lebar):
#     panjang = panjang + 1
#     print("Panjang dalam fungsi : ", panjang)
#     return panjang * lebar

# panjang = int(input())
# lebar = int(input())
# print("Panjang : ", panjang)
# luas1 = LuasSegiempat(panjang, lebar)
# print("Panjang setelah keluar dari fungsi : ", panjang)
# panjang = int(input())
# lebar = int(input())
# luas2 = LuasSegiempat(panjang, lebar)
# print(luas1 + luas2)

# ==============================================================

def LuasSegiempat(panjang, lebar):
    return panjang * lebar


def main():
    panjang = int(input())
    lebar = int(input())
    print("Panjang : ", panjang)
    luas1 = LuasSegiempat(panjang, lebar)
    panjang = int(input())
    lebar = int(input())
    luas2 = LuasSegiempat(panjang, lebar)
    print(luas1 + luas2)


main()
