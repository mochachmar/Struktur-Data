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


class Student(Person):
    def __init__(self, nama="no name", umur=0):
        super().__init__(nama="no name", umur=umur)
        self.__id = id

    def perkenalkan_diri(self):
        return "Saya adalah seorang murid. Nama saya " + self.get_nama()


class Teacher(Person):
    def __init__(self, nama="no name", umur=0):
        super().__init__(nama=nama, umur=umur)


def main():
    s = Student("Dodi", 12)
    t = Teacher()
    print(s.perkenalkan_diri())
    print(t.perkenalkan_diri())


main()
