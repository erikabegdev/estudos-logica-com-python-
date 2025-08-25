# Desafio: Simular saque em caixa eletrônico
valor = int(input("Digite o valor do saque: R$ "))
notas = [100, 50, 20, 10, 5, 2]
for nota in notas:
    qtd, valor = divmod(valor, nota)
    if qtd:
        print(f"{qtd} nota(s) de R$ {nota}")
if valor > 0:
    print("Valor não pode ser sacado em notas disponíveis.")