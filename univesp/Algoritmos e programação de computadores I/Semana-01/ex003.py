print('Primeira nota:')
n1 = input()
print('Segunda nota:')
n2 = input()
print('Terceira nota:')
n3 = input()
print ('Quarta nota:')
n4 = input()

md = (n1+n2+n3+n4)/4

print ('Sua média foi de:', md)

if md >= 5: 
    print('Você foi aprovado')
else:
    print('Você não foi aprovado')    
