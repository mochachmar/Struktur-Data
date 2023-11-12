class Person:
    def __init__(self, nama="no name", umur=0):
        self.__umur = umur
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def perkenalkan_diri(self):
        return "Saya adalah " + self.__nama + ", berumur " + str(self.__umur) + " tahun."

    def __add__(self, other):
        n = Person(self.get_nama() + other.get_umur(),
                   self.get_umur() + other.get_umur())
        return n

    def __str__(self):
        return self.perkenalkan_diri()


def main():
    p = Person("Dodi", 12)
    y = Person("Bayu", 20)
    a = p + y
    print(a)


main()
