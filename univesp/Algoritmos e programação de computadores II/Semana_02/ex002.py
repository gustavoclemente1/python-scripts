#Exercício de exemplo de herança em python
#sal: salário
#f1: funcionário 1

class Funcionario:
    def __init__(self, nome:str, data:str, sal:float):
        self.nome = nome
        self.data = data
        self.sal = sal

    def bonus(self):
        if self.sal <= 1500:
            self.sal += 0.2*self.sal

    def __repr__(self):
        return 'Nome:'+ str(self.nome) + ' Data:' + str(self.data) + ' Salário:' + str(self.sal)
    

class Gerente(Funcionario):

    # Só é necessário sobrescrever o __init__ se você quiser adicionar ou modificar parâmetros ou comportamentos específicos para a classe derivada.

    def bonus(self):
        if self.sal >= 2000:
            self.sal += 0.2*self.sal 
        
gerente1 = (Gerente('Maria', 22051998, 2300)) 
gerente1.bonus()
print(gerente1)
f1 = Funcionario("João", 10062025, 1400)
f1.bonus()
print(f1)