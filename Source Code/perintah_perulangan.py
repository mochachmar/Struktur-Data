# x = 0
# x = x + int(input())
# x = x + int(input())
# x = x + int(input())
# x = x + int(input())
# x = x + int(input())
# x = x / 5
# print("Rata-rata : ", x)

# ==============================================================

# total = 0
# for x in range(1, 6):
#     print("Masukkan bilangan ke : ", x)
#     total = total + int(input())
# total = total / 5
# print("Rata-rata : ", total)

# ==============================================================

n = int(input("Menghitung rata-rata berapa buah bilangan? "))
total = 0
counter = 1
while (counter <= n):
    print("Masukkan bilangan ke : ", counter)
    total = total + int(input())
    counter = counter + 1
total = total / 5
print("Rata-rata : ", total)
