# Desafio: Sequência de Fibonacci
n = int(input("Quantos termos da sequência de Fibonacci deseja? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b