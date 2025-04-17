class Point:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y
    
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '()' + str(self.x) + ',' + str(self.y) + ')'

    # No exercício proposto da aula, o algoritmo terá que somar de ambas as formas abaixo:
    # x + y ==> (2,3) + (2,2) = (4,5) Soma-se x com x e y com y
    # x + 8 ==> (2,3) + 8 = (10,11) Soma-se 8 embos x e y

    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)
        
p = Point()

print (p)

