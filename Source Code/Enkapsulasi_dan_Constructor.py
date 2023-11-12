class Person:
    __umur = 0

    def __init__(self, name, umur):
        self.__name = name
        self.__set_umur(umur)

    def get_name(self):
        return self.__name

    def get_umur(self):
        return self.__umur

    def __set_umur(self, umur):
        self.__umur = umur if umur >= 0 else 0


def main():
    p = Person("Joni", -12)
    print(p.get_name())
    print(p.get_umur())


main()
