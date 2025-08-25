# Desafio: Mini agenda com dicionário
agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
    elif opcao == "2":
        nome = input("Nome a remover: ")
        if nome in agenda:
            del agenda[nome]
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")