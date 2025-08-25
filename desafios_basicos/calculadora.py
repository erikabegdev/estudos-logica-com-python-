# Desafio: Calculadora simples
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"{a} + {b} = {a+b}")
elif op == "-":
    print(f"{a} - {b} = {a-b}")
elif op == "*":
    print(f"{a} * {b} = {a*b}")
elif op == "/":
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    else:
        print("Erro: divisão por zero!")
else:
    print("Operação inválida!")