#Exercício sobre padrões usando recursividade

def padrão(n):
    if n == 0:
        print(0, end=' ')
    else:
        padrão(n-1)
        print(n, end=' ')
        padrão(n-1)

def padrão2(n):
    if n == 0:
        print(' ')
    elif n == 1:
        print('*')
    else:
        padrão2(n-1)
        print(n * '*')
        padrão2(n-1)

padrão2(3) 