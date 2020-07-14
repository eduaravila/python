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

    def open(self, row, col):
        value = row+col
        self.elements[row][col] = value


perc = Percolation(10, 10)
print(perc.elements)
