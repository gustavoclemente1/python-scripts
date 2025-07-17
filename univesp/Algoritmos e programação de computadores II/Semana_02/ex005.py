# Exercício de classes sobre jogo de cartas

class Card:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def getRank(self):
        print(self.valor)
    
    def getSuit(self):
        print(self.naipe)
    

carta = Card('3', '\u2660')
carta.getRank()
carta.getSuit()
    