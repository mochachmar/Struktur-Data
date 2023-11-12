from abc import ABCMeta, abstractmethod


class BangunDatar(metaclass=ABCMeta):
    @abstractmethod
    def get_luas(self):
        "return luas bangun datar"

    def __str__(self):
        return "Luas bangun ini adalah " + str(self.get_luas())


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.__alas, self.__tinggi = alas, tinggi

    def get_luas(self):
        return 0.5 * self.__alas * self.__tinggi


def main():
    s = Segitiga(5, 3)
    print(str(s))


main()
