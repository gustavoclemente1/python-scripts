#Exercício de classe contêiner Queue

class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self, item):
        #insere item no final da fila
        print(item)
        return (self.q.append(item))

    def dequeue(self, item):
        #remove e retorna item na frente da fila
        print(f'Item removido:', item)
        return self.q.pop(0)
    
    def isEmpty(self):
        print(f'Tamanho da lista Queue:',len(self.q))
        return print(f'Lista vazia:',(len(self.q) == 0))

fruta = Queue()
fruta.enqueue('maça')
fruta.enqueue('banana')
fruta.enqueue('coco')
fruta.dequeue('maça')
fruta.dequeue('banana')
fruta.dequeue('coco')
fruta.isEmpty()

