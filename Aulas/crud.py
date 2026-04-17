# Dicionário para armazenar os dados
# Exemplo: chave = nome | valor = nota
alunos = {}

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar (Criar)")
    print("2 - Listar (Ler)")
    print("3 - Atualizar (Atualizar)")
    print("4 - Excluir (Deletar)")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # CREATE
    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota: "))

        alunos[nome] = nota
        print(f"Aluno '{nome}' cadastrado com sucesso.")

    # READ
    elif opcao == "2":
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\nLista de alunos:")
            for nome, nota in alunos.items():
                print(f"{nome} -> {nota}")

    # UPDATE
    elif opcao == "3":
        nome = input("Digite o nome do aluno que deseja atualizar: ")

        if nome in alunos:
            nova_nota = float(input("Digite a nova nota: "))
            alunos[nome] = nova_nota
            print(f"Nota do aluno '{nome}' atualizada.")
        else:
            print("Aluno não encontrado.")

    # DELETE
    elif opcao == "4":
        nome = input("Digite o nome do aluno que deseja excluir: ")

        if nome in alunos:
            del alunos[nome]
            print(f"Aluno '{nome}' removido com sucesso.")
        else:
            print("Aluno não encontrado.")

    # SAIR
    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
