class Baralho:
    def Baralho():
        naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
        valores = {'2,','3','4','5','6','7','8','9','10','J','Q','K','A'}

        for naipe in naipes:
            for valor in valores:
                print(naipes + valores)


baralho = Baralho()
