import math


class Line():
    def __init__(self, cor1, cor2):
        super().__init__()
        self.cor1 = cor1
        self.cor2 = cor2

    # ? squareroot((x1-x2)^2 +(y1-y2)^2)
    def distance(self):
        return math.sqrt((self.cor1[1]-self.cor1[0]) ** 2 + (self.cor2[1]-self.cor2[0])**2)

    def slope(self):
        return (self.cor1[1]-self.cor1[0])/(self.cor2[1]-self.cor2[0])


cokeLine = Line(cor1=[10, 20], cor2=[100, 200])
print(cokeLine.distance())
print(cokeLine.slope())


class Cylinder():
    def __init__(self, height=1, radius=1):
        super().__init__()
        self.height = height
        self.radius = radius
    
    def volume(self):
        
