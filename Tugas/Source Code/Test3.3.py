# Implementasi kelas Matriks Larik2D
# Matriks.py == @Moch_Achmar
from Test3 import Larik2D


class Matriks:
    def __init__(self, numRows, numCols):
        self._theGrid = Larik2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def tranpose(self):
        bar = self.numRows()
        kol = self.numCols()
        temp = Matriks(kol, bar)
        for i in range(bar):
            for j in range(kol):
                temp[j, i] = self[i, j]
        return temp

    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols(
        ) == self.numCols(), "Matrix sizes not compatible for the add operation."
        newMatriks = Matriks(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatriks[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatriks

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numRows(
        ) == self.numCols(), "Matrix sizes not compatible for the add operation."
        newMatriks = Matriks(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatriks[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatriks

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(
        ), "Matrix sizes not compatible for the multiplication."
        newMatriks = Matriks(self.numRows(), rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                newMatriks[r, c] = 0
                for k in range(rhsMatrix.numRows()):
                    newMatriks[r, c] += self[r, k] * rhsMatrix[k, c]
        return newMatriks

    def dispMatriks(self):
        for i in range(self.numRows()):
            myRow = []
            for j in range(self.numCols()):
                myRow.append(self[i, j])
            print((myRow))

    def isiMatriks(self):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print('index [%d, %d]: ' % (i, j))
                self[i, j] = int(input(' : '))

    def Hapus(self, x):
        found = False
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if self[i, j] == x:
                    print("Data ada di baris:", i, ", kolom:", j)
                    self[i, j] = ""
                    found = True
                    print("Setelah dihapus: ")
                    for i in range(self.numRows()):
                        myRow = []
                        for j in range(self.numCols()):
                            myRow.append(self[i, j])
                        print(myRow)

        if not found:
            print("Data itu tidak ada dalam Matriks!")
