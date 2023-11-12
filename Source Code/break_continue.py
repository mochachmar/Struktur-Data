# def MyMethod(number1 = 10, number2 = 5, number3 = 30):
#     print(number1)
#     print(number2)
#     print(number3)

# def main():
#     MyMethod(1, 2)

# main()

# def MyMethod(number1 = 10, number2 = 20, number3 = 30):
#     for x in range(number1, number2 + 1):
#         if(x == number3):
#             break
#         print(x)

# def main():
#     MyMethod(1, 10, 5)

# main()

# ==========================================================

def MyMethod(number1=10, number2=20, number3=30):
    for x in range(number1, number2 + 1):
        if (x < number3):
            continue
        print(x)


def main():
    MyMethod(1, 10, 5)


main()
