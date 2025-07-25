#Exercício de busca binária em uma lista ordenada.

def busca(list, target, i, j):
    if i == j:  #Caso básico. Quando target não está na lista.  
        return -1
    
    mid = (i+j) // 2 # Índice da mediana da lista

    if list[mid] == target:  #Alvo encontrado na metade da lista
        return mid
    if target < list[mid]:    #Busca à esquerda da lista
        return busca(list, target, i, mid)
    else:
        return busca(list, target, mid+1, j)  #Busca à direita da lista
    

lista = [2, 5, 11, 13, 16, 24, 28, 41, 42, 43, 45, 57, 72, 73, 89, 90, 99]
target = 45
print(busca(lista, target, 0, len(lista)))



