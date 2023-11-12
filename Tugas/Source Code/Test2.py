import math
# List.py == @Moch_Achmar
print("222362 Moch Achmar K")
list_data = []
print("Masukkan minimal 10 angka bulat secara acak : ")
for i in range(10):
    angka = int(input("Masukkan angka ke-{}: ".format(i+1)))
    list_data.append(angka)

print("List yang dimasukkan: ", list_data)

nilai_maksimum_list_data = max(list_data)
nilai_minimum_list_data = min(list_data)
print("Nilai maksimum: ", nilai_maksimum_list_data)
print("Nilai minimum: ", nilai_minimum_list_data)

nilai_rata_rata_list_data = sum(list_data) / len(list_data)
print("Nilai rata-rata: ", nilai_rata_rata_list_data)

nilai_varians_list_data = sum(
    [((x - nilai_rata_rata_list_data) ** 2) for x in list_data]) / len(list_data)
nilai_devisiasi_standar_list_data = math.sqrt(nilai_varians_list_data)
print("Nilai devisiasi standar: ", nilai_devisiasi_standar_list_data)
