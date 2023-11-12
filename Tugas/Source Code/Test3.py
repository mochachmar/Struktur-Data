# Implementasi kelas Larik2D, memakai larik dari larik
# Larik2D.py == @Moch_Achmar
from Test import Larik
 

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
