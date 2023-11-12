def Hapus(brs, kol, x, matrix):
    if brs >= len(matrix) or kol >= len(matrix[0]):
        print("Error: Index out of range")
        return matrix
    if matrix[brs][kol] == x:
        matrix[brs].pop(kol)
        print("Data", x, "berhasil dihapus dari baris", brs, "dan kolom", kol)
    else:
        print("Data", x, "tidak ditemukan di baris", brs, "dan kolom", kol)
    return matrix






























def Main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matriks awal:")
    for row in matrix:
        print(row)
    brs = 2
    kol = 1
    x = 8
    matrix = Hapus(brs, kol, x, matrix)
    print("Matriks setelah menghapus", x,
          "dari baris", brs, "dan kolom", kol, ":")
    for row in matrix:
        print(row)


Main()























