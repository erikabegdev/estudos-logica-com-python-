# Desafio: Cadastro de usuários em JSON
import json

usuarios = []
while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Digite a idade: "))
    usuarios.append({"nome": nome, "idade": idade})

with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)

print("Usuários salvos em usuarios.json")