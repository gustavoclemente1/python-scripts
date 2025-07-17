#Exercício de implementação de classes com um retângulo


class Retângulo:
    def __init__(self, largura, comprimento):
        self.lar = largura
        self.com = comprimento

    def Perimetro(self):
        self.per = (self.lar + self.com) * 2
        print(f'O perímetro é: {self.per}')

    def Area(self):
        self.area = self.lar * self.com
        print(f'A área é: {self.area}')




retângulo = Retângulo(3,4)
retângulo.Perimetro()
retângulo.Area()