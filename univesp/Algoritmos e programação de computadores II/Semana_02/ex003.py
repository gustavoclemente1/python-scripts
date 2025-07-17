#Exercício de namespace e atributos de classe

class Teste:
    versão = 1.02


a = Teste()
b = Teste()

print(a.versão)
print(b.versão)
Teste.versão = 1.03
a.versão = 2.0
print(b.versão)
print(a.versão)