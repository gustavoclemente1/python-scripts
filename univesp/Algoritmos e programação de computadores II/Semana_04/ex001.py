# Excício sobre pilhas para a conversão de um número decimal para binário
#Pilhas: O último a entrar é sempre o primeiro a ser removido.

class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        #Insere um elemento
        self.data.append(x)

    def pop(self):
        #Retira o último elemento
        if len(self.data) > 0:
            return self.data.pop(-1)
                      
    def top(self):
        #Acessa o último elemento
        if len(self.data) > 0:
            return self.data[-1]
        
    def empty(self):
        #Verifica se a lista está vazia ou não retornando um valor booleano
        return not len(self.data) > 0

    
p = Pilha()
num = 13
while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    print(p.pop())


