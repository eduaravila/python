from percolation import Percolation
import random

import sys
sys.setrecursionlimit(100000000)


class PercolationStats():
    def __init__(self, n, trials):
        super().__init__()
        self.n = n
        self.trials = trials
        self.thresholds = [*self.percolationStats()]

    def percolationStats(self):
        for board in range(self.trials):
            percolation = Percolation(self.n, self.n, board)
            print(percolation.n)
            while 1:
                percolation.open(self.randomField(), self.randomField())
                if percolation.percolates():
                    print("Percolates")
                    threshold = percolation.numberOfOpenSites() / (self.n*self.n)
                    yield threshold
                    break

    def randomField(self):
        number = random.randint(1, self.n)
        if number <= 0:
            return 1
        else:
            return number


stats = PercolationStats(20, 100)

print("stats", stats.trials)
