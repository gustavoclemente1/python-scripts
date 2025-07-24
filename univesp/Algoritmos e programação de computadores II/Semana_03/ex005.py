#Exercício de potenciação usando recursividade


def potenciação(base,exp): #exp(expoente)
    res = 1

    for i in range (exp):
        res *= base 

    return res

def potenciação_r(base, exp): #potenciação recursiva
    

    if exp == 0:
        return 1

    tmp = potenciação_r(base, exp//2)  

    if exp % 2 == 0:
        return tmp * tmp
    else:
        return base * tmp * tmp

print(potenciação_r(2,4))


    