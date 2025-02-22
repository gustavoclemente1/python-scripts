# Lê 4 notas de um aluno e calcula sua média final. Se for maior ou igual 5, o aluno foi aprovado. Se for menor, o aluno é reprovado.

def returnMedia(array):
    media = sum(array) / len(array) 

    return media

arrayNotas = []
aux = 0

while (aux < 4): 
    nota = input(f'Digite a nota {aux + 1} :')
    arrayNotas.append(float(nota))
    aux += 1

notaFinal = returnMedia(arrayNotas)

print('Sua nota foi:',notaFinal)

if (notaFinal >= 5):
    print('Você foi aprovado!')
else:
    print ('Você foi reprovado!')
