from mahasiswa import Mahasiswa

print("=====================================================")
print("======== Program menghitung nilai mahasiswa =========")
print("========== CREATED BY 222362 MOCH ACHMAR ============")
print("=====================================================")

mahasiswa = Mahasiswa(input("Masukkan NIM: "),
                      input("Masukkan Nama Mahasiswa: "))

while True:
    mahasiswa.hitung_nilai()

    ulang = input("Apakah ingin menginput ulang? (Y/T) atau (y/t): ")
    if ulang.lower() != "y":
        break
