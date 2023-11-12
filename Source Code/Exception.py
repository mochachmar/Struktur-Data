def fungsi(bilangan):
    if bilangan < 0:
        raise ValueError("Harus positif cok!")
    return bilangan + 1


def main():
    x = int(input())
    try:
        hasil = fungsi(x)
        print(hasil)
    except:
        print("error euy!")
    finally:
        print("ini finally!")


main()
