# Desenvolver os diagramas de blocos e as codificações em português estruturado
# usando laço incondicional (para) do seguinte problema: Construir um programa
# que apresente a soma dos cem primeiros números
# naturais (1 + 2 + 3 +...+ 98 + 99 + 100).

soma100 = 0

for i in range (101):

    print (f'soma: {soma100}, index: {i}')
    soma100 += i

print(soma100)