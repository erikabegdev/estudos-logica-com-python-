# Desafio: Verificar se uma palavra/frase é palíndromo
texto = input("Digite uma palavra ou frase: ").replace(" ", "").lower()
if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")