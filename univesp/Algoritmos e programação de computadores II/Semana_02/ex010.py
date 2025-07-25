#Variação do ex007 com a implementação da função __repr__ e ==

from random import shuffle

class Baralho:
        
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self):
        self.baralho = []
        for naipe in Baralho.naipes:
            for valor in Baralho.valores:
                self.baralho.append((valor, naipe))
        
    def distribuiCarta(self):
        self.carta = self.baralho.pop(0)
         
    def mistura(self):
        shuffle(self.baralho)
           
    def __repr__(self):
        return 'Carta '+str(self.carta)

           
carta = Baralho()
carta.distribuiCarta()
print(carta)
print(carta == carta)
carta.mistura()
