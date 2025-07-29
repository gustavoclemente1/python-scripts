# Exercício fundamental sobre filas
# Fila: O primeiro a entrar é sempre o primeiro a ser removido da fila

class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    

p = Fila()
p.inserir(1)
p.inserir(2)
p.inserir(3)
