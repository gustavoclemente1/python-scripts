class Animal:
    def setEspécie(self, espécie):
        self.esp = espécie
        
    def setLinguagem(self, linguagem):
        self.ling = linguagem

    def fala():
        print(f'Eu sou um {} e sei {}'.format(self.esp, self.ling))

snoopy = Animal() 
snoopy.setEspécie('cão')       
snoopy.setLinguagem('latir')
snoopy.fala()