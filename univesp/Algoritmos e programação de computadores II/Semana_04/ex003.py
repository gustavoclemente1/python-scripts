#Programa para inserção e remoção de pessoas em duas filas classificadas como normal e priooritária.

class Fila():
    def __init__(self):
        self.normal = []
        self.prioritaria = []

    def inserir(self, nome, idade):
        if idade <= 60:
            #Insere uma pessoa na fila normal
            self.normal.append(idade) 
            print(f'{nome} de {idade} anos foi adicionado(a) para a fila normal. Lista atual: {self.normal}')            
        else:
           #Insere uma pessoa na fila prioritária
           self.prioritaria.append(idade)
           print(f'{nome} de {idade} anos foi adicionado(a) para a fila prioritária. Lista atual: {self.prioritaria}')

    def remover(self):
        #Para cada duas prioritárias removidas, uma normal também é
        while self.normal and self.prioritaria != []:
            self.prioritaria.pop(0)
            self.prioritaria.pop(0)           
            self.normal.pop(0)
            
        print(self.normal)
        print(self.prioritaria)

            
                
p = Fila()
p.inserir('Juca', 43)
p.inserir('Maria', 69)
p.inserir('Marcelo', 44)
p.inserir('João', 87)
p.inserir('Antonio', 78)
p.inserir('Severina', 75)
p.remover()



        