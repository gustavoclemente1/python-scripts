# Baralho de 52 cartas que retorna uma carta aleatóriamente.

from random import shuffle

class Baralho:
        
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2,','3','4','5','6','7','8','9','10','J','Q','K','A'}

    def __init__(self):
        self.baralho = []
        for naipe in Baralho.naipes:
            for valor in Baralho.valores:
                self.baralho.append((naipe, valor))
        
    def distribuiCarta(self):
        carta = self.baralho.pop()
        print(carta)
        return carta
    
    def mistura(self):
        shuffle(self.baralho)
           
baralho = Baralho()
baralho.distribuiCarta()
baralho.mistura()

