# class Person:
#     nama = ""


# def myFunction(person, bilangan):
#     person = Person()
#     person.nama = "Dodi"
#     bilangan = 3
#     print(person.nama)
#     print(bilangan)


# def main():
#     p = Person()
#     p.nama = "Joko"
#     b = 12
#     myFunction(p, b)
#     print(p.nama)
#     print(b)


# main()

# ==============================================================

class Person:
    nama = ""


def myFunction(a=1, b=2, c=3):
    print(a, b, c)


def main():
    myFunction(b=11, c=6, a=7)


main()
