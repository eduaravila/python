class QuickUnion:

    def __init__(self):
        super().__init__()
        self.elements = [*self.populate()]

    def populate(self, n=10):
        for i in range(n):
            yield i

    def root(self, i):
        while i != self.elements[i]:
            i = self.elements[i]
        return i

    def union(self, a, b):
        aRoot = self.root(self.elements[a])
        bRoot = self.root(self.elements[b])
        self.elements[aRoot] = bRoot

    def areConnected(self, a, b):
        print(self.root(a),self.root(b))
        return self.root(a) == self.root(b)


quick = QuickUnion()
print(quick.elements)

quick.union(0, 9)
print(quick.areConnected(0, 9))
print(quick.elements)
