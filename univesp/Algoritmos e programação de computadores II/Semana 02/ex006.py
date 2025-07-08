#Exercício sobre classes que identifica uma espécie animal e sua liguagem.

class Animal:
    def __init__(self, espécie = 0, linguagem = 0):
        self.esp = espécie
        self.ling = linguagem

    def setEspécie(self, espécie = ''):
        self.esp = espécie
        
    def setLinguagem(self, linguagem = ''):
        self.ling = linguagem

    def fala(self):
        if self.esp == 0 and self.ling == 0:
            print('Eu sou um animal e sei emitir sons') 

        elif self.ling == 0:
            print(f'Eu sou um {self.esp} e sei emitir sons')

        else:    
            print(f'Eu sou um {self.esp} e sei {self.ling}')
        

snoopy = Animal('canário', 'cantar') 
snoopy.fala()