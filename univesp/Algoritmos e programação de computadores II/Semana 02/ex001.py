class Point:
    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def get(self):
        return (self.x, self.y)

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

ponto = Point()
ponto.setx(4)
ponto.sety(2)
ponto.move(1, 2)
print(ponto.get())


