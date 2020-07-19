class Percolation():
    def __init__(self, rows, cols):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.elements = [*self.percolation()]

    def percolation(self):
        elementsRow = []
        for index, row in enumerate(range(self.rows)):
            for col in range(self.cols):
                elementsRow.append(None)
            yield elementsRow
            elementsRow = []

    def isOpen(self, row, col):
        if row <= 0 or col <= 0:
            raise ValueError("Values must be > 0")

        if self.elements[row-1][col-1] == 1:
            print("Open", row-1, col-1)
            return True
        else:
            return False

    def isFull(self, row, col):
        if self.elements[row][col] == None:
            return True
        else:
            return False

    def numberOfOpenSites(self):
        total = 0
        for row in self.elements:
            for col in self.elements[row]:
                if col == 1:
                    total += 1
        return total

    def checkLimit(self, row, col):
        rowLimit = len(self.elements)
        colLimit = len(self.elements[0])
        if row < rowLimit and col < colLimit:
            return True
        else:
            return False

    def isBottom(self, row):
        print("Row", row, len(self.elements), row+1)
        rowLimit = len(self.elements[0])
        if row+1 == rowLimit:
            return True
        else:
            return False

    def printBoard(self):
        for index, row in enumerate(self.elements):
            print("\n")
            for col in self.elements[index]:
                print(f" {col} ", end="")

    def isConnected(self, row, col, connected, counter):

        if(connected):

            if self.checkLimit(row, col+1) and self.elements[row][col+1] == 1:
                return self.isConnected(row, col+1, True, counter+1)
            elif self.checkLimit(row+1, col) and self.elements[row+1][col] == 1:
                return self.isConnected(row+1, col, True, counter+1)
            elif self.checkLimit(row, col-1) and self.elements[row][col-1] == 1:
                return self.isConnected(row, col-1, True, counter+1)
            else:
                return self.isConnected(row, col, False, counter)
        else:
            print("final", self.isOpen(row+1, col+1),
                  self.isBottom(row), col, row)
            if self.isBottom(row) == True and self.isOpen(row+1, col+1) == True and counter >= len(self.elements):
                return True
            else:
                return False

    def open(self, row, col):
        if row <= 0 or col <= 0:
            raise ValueError("Values must be > 0")
        self.elements[row-1][col-1] = 1

    def percolates(self):
        percolate = False
        for index, row in enumerate(self.elements):
            for indexCol, col in enumerate(row):
                if self.isConnected(index, indexCol, True, 0):
                    percolate = True
        return percolate


perc = Percolation(10, 10)
perc.open(1, 1)
perc.open(2, 1)
perc.open(3, 1)
perc.open(4, 1)
perc.open(5, 1)
perc.open(6, 1)
perc.open(7, 1)
perc.open(8, 1)
perc.open(9, 1)
perc.open(10, 2)

perc.printBoard()

print("Connected=", perc.percolates())
