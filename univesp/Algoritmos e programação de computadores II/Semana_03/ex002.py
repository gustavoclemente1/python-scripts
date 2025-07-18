# Exercício de Fibonacci com função recursiva

def Fib_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
       
    return Fib_rec(n - 1) + Fib_rec(n - 2)

def Fib_it(n):
    res = n
    a,b = 0, 1

    for C in range(3, n+1):
        res = a + b
        a, b = b, res

    return res

print(Fib_it(5))
print(Fib_rec(5))

