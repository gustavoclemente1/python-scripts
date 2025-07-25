#Exercício de busca de duplicatas

def duplicata1(list):
    for item in list:
        if list.count(item) > 1:
            return True
        
    return False

def duplicata2(list):
    list.sort()

    for index in range(1, len(list)):
        if list[index] == list[index-1]:
            return True
    return False

lista = [2, 5, 11, 13, 16, 24, 28, 41, 42, 43, 45, 57, 72, 73, 89, 90, 99]
print(duplicata2(lista))