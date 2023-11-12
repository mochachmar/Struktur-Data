# Implementasi ADT Larik memakai python list
# Larik.py == @Moch_Achmar
print("222362 Moch Achmar K")


class Larik:
    def __init__(self, size):
        self._size = size
        self._elements = []
        for i in range(size):
            self._elements.append(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(
            self), "Index larik sudah diluar batas!"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(
            self), "Indeks larik sudah diluar batas!"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def fromList(self, l):
        n = self._size
        m = len(l)
        if (m > n):
            self.__init__(m)
        i = 0
        for x in l:
            self._elements[i] = x
            i += 1

    def fromString(self, Str):
        n = self._size
        m = len(Str)
        if (m > n):
            self.__init__(m)
        for i in range(m):
            self._elements[i] = ord(Str[i])

    def isiLarik(self):
        n = self._size
        for i in range(n):
            print('Indeks ', i)
            self._elements[i] = int(input(' : '))

    def cariX(self, x):
        n = self._size
        ketemu = False
        for i in range(n):
            if (x == self._elements[i]):
                print('Ketemu pada index : ', i)
                ketemu = True
        if (not ketemu):
            print(x, ' Tidak ada dalam larik!')

    def hapusX(self, x):
        n = self._size
        ketemu = False
        for i in range(n):
            if (x == self._elements[i]):
                print('Ketemu pada index : ', i)
                ketemu = True
                print('Sudah dihapus!')
                self._elements[i] = None
        if (not ketemu):
            print(x, ' Tidak ada dalam array! ')

    def bacaLarik(self):
        r = input('0-Semua-data   1-hanya-satu-data : ')
        r = int(r)
        if r < 1:
            for x in self._elements:
                print(x)
        else:
            i = int(input('index : '))
            print(self._elements[i])

    def cacah(self, x):
        ccah = 0
        for n in self._elements:
            if n == x:
                ccah += 1
        return ccah

    class _ArrayIterator:
        def __init__(self, theArray):
            self._arrayRef = theArray
            self._curNdx = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._curNdx < len(self._arrayRef):
                entry = self._arrayRef[self._curNdx]
                self._curNdx += 1
                return entry
            else:
                raise StopIteration


class Larik2D:
    def __init__(self, numRows, numCols):
        self._theRows = Larik(numRows)
        for i in range(numRows):
            self._theRows[i] = Larik(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Array subscipt out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows(
        ) and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

    def isi2D(self):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                print('index [%d, %d]: ' % (i, j))
                self[i, j] = int(input(' : '))

    def dispArr2D(self):
        for i in range(self.numRows()):
            myRow = []
            for j in range(self.numCols()):
                myRow.append(self[i, j])
            print(myRow)


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
            print(myRow)

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

        if (not found):
            print("Data itu tidak ada dalam Matriks!")
