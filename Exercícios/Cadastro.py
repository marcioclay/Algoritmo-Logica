alunos = []

def menu():
    print("1-Incluir", "2-Excluir", "3-Atualizar", "4-Listar", "5-Sair")
    opcao = int(input("Selecione opção: "))
    while opcao != 5:

        if opcao == 1:
            nome = input("Digite nome do aluno: ")
            alunos.append(nome)
            print(alunos)
        elif opcao == 2:
            nome = input("Digite nome do aluno que deseja excluir: ")
            alunos.remove(nome)
        elif opcao == 3:
            print(alunos)
            nomeexcluir = input("Qual nome deseja remover? ")
            posicao=alunos.index(nomeexcluir)
            alunos.pop(posicao)
            nome = input("Qual alteração deseja fazer? ")
            alunos.insert(posicao,nome)

        elif opcao == 4:
            print(alunos)

        listas = ["1-Incluir", "2-Excluir", "3-Atualizar", "4-Listar", "5-Sair"]
        opcao = int(input(f'{listas}\nSelecione opção: '))



menu()
    
