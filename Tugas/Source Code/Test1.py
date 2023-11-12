# List.py == @Moch_Achmar
print("222362 Moch Achmar K")
list_data = input(
    "Masukkan nilai list dengan pemisah koma lalu spasi : ").split(', ')
print("List yang dimasukkan : ", list_data)

jumlah_data_list = sum(map(int, list_data))
print("Hasil penjumlahan seluruh data dalam list : ", jumlah_data_list)

rata_rata_list_data = jumlah_data_list/len(list_data)
print("Nilai rata-rata dari isi list : ", rata_rata_list_data)

set_list_data = set(list_data)
print("Set yang dibuat dari list : ", set_list_data)

tuple_list_data = tuple(set_list_data)
print("Tuple yang dibuat dari set list : ", tuple_list_data)
