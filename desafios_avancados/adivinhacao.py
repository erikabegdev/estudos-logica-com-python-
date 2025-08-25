# Desafio: Jogo de adivinhação
import random
numero_secreto = random.randint(1, 20)
tentativas = 0

print("Adivinhe o número entre 1 e 20!")

while True:
    chute = int(input("Seu palpite: "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Acertou em {tentativas} tentativas! O número era {numero_secreto}.")
        break
    elif chute < numero_secreto:
        print("Muito baixo, tente novamente.")
    else:
        print("Muito alto, tente novamente.")