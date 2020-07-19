class Percolation():
    def __init__(self, rows, cols, n=1):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.elements = [*self.percolation()]
        self.n = n

    def percolation(self):
        elementsRow = []
        for index, row in enumerate(range(self.rows)):
            for col in range(self.cols):
                elementsRow.append(None)
            yield elementsRow
            elementsRow = []

    def isOpen(self, row, col):

        if row <= 0 or col <= 0:
            if row <= 0:
                row = 1
            if col <= 0:
                col = 1

        if self.elements[row-1][col-1] == 1:
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

    def isConnected(self, row, col, counter=0):

        while self.isBottom(row) == False or self.isOpen(row+1, col+1) == False or counter <= len(self.elements):
            counter += 1
            if self.checkLimit(row, col+1) and self.elements[row][col+1] == 1:
                # return self.isConnected(row, col+1, True, counter+1)
                col += 1
                continue
            elif self.checkLimit(row+1, col) and self.elements[row+1][col] == 1:
                # return self.isConnected(row+1, col, True, counter+1)
                row += 1
                continue
            elif self.checkLimit(row, col-1) and self.elements[row][col-1] == 1:
                # return self.isConnected(row, col-1, True, counter+1)
                col -= 1
                continue
            else:
                print(col, row, self.isBottom(row),
                      self.isOpen(row+1, col+1), "cPunter", counter)

                if self.isBottom(row) == True and self.isOpen(row+1, col+1) == True and counter >= len(self.elements):
                    return True
                else:
                    return False
        print("end", col, row, self.isBottom(row),
              self.isOpen(row+1, col+1), "cPunter", counter)
        # else:
        #     # print("final", self.isOpen(row+1, col+1),
        #     #       self.isBottom(row), col, row)
        #     if self.isBottom(row) == True and self.isOpen(row+1, col+1) == True and counter >= len(self.elements):
        #         return True
        #     else:
        #         return False

    def open(self, row, col):
        if row <= 0 or col <= 0:
            raise ValueError("Values must be > 0")
        self.elements[row-1][col-1] = 1

    def percolates(self):
        percolate = False
        for index, row in enumerate(self.elements):
            for indexCol, col in enumerate(row):
                if self.isConnected(index, indexCol):
                    percolate = True
        return percolate


per = Percolation(10, 10)

per.open(1, 1)
per.open(2, 1)
per.open(3, 1)
per.open(4, 1)
per.open(5, 1)
per.open(6, 1)
per.open(7, 1)
per.open(8, 1)
per.open(9, 1)
per.open(10, 1)

per.printBoard()
print(per.percolates())
