class QuickFind():
    def __init__(self, elementsSize):
        super().__init__()
        self.elementsSize = elementsSize
        self.elements = [*self.populate()]

    def populate(self):
        for x in range(self.elementsSize):
            yield x

    def union(self, q, p):
        oldIndex = self.elements[q]
        newIndex = self.elements[p]

        for index, x in enumerate(self.elements):
            if x == oldIndex:
                self.elements[index] = newIndex

    def connected(self, q, p):
        if self.elements[q] == self.elements[p]:
            return True
        return False


quick = QuickFind(10)
print(quick.elements)
quick.union(1, 9)
print(quick.connected(1, 9))
print(quick.elements)
quick.union(5, 9)
print(quick.connected(5, 9))
print(quick.elements)
