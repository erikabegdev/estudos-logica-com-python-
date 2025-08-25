# Desafio: Jogo da Forca
import random

palavras = ["python", "programacao", "desafio", "computador"]
palavra = random.choice(palavras)
tentativas = 6
acertos = ["_"] * len(palavra)

print("Jogo da Forca!")

while tentativas > 0 and "_" in acertos:
    print(" ".join(acertos))
    letra = input("Digite uma letra: ").lower()
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                acertos[i] = letra
    else:
        tentativas -= 1
        print(f"Errou! Você ainda tem {tentativas} tentativas.")
        
if "_" not in acertos:
    print("Parabéns! Você acertou:", palavra)
else:
    print("Game Over! A palavra era:", palavra)