# Exercício sobre recursividade usando um número de múltiplos dígitos

def vertical(n):
    if n < 10:
        print(n)
    else:
        vertical(n // 10)
        #  Remove o último dígito de n usando o operador de divisão inteira (//)
        print(n % 10)
        #Obtem-se o último dígito usando o operador de módulo (%)

def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        reverse(n // 10)

def cheers(n):
    if n <= 0:
        print('Hurrah')
    else:
       print('Hip', end=' ')
       # o parâmetro end define o caractere ou string que será usado ao final da impressão, invez do padrão, que é a quebra de linha \n. No caso, foi utilizado um espaço. Assim, todas  as impressões ficam na mesma linha.
       cheers(n - 1)

def fatorial(n):
    if n in [0,1]:
        return 1
    else:
        res =  fatorial(n-1) * n
        print(res)
        return res
               
fatorial(5)

