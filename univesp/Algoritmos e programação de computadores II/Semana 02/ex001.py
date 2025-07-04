class Point:
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

ponto = Point()
ponto.setx(4)
ponto.sety(2)
print(ponto)
