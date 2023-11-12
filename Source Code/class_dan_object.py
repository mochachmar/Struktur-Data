class Segiempat:
    panjang = 0
    lebar = 0

    def hitungLuas(self):
        return self.panjang * self.lebar


def main():
    s = Segiempat()
    s.panjang = int(input())
    s.lebar = int(input())
    luas = s.hitungLuas()
    print(luas)


main()
