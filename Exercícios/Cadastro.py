alunos=[]
def menu():
    listas=["1-Incluir","2-Excluir","3-Atualizar","4-Listar", "5-Sair"]
    opcao=int(input(f'{listas}\nSelecione opção: '))
    while opcao!=5:

        if opcao==1:
            nome=input("Digite nome do aluno: ")
            alunos.append(nome)
            print(alunos)
        elif opcao==2:
            nome = input("Digite nome do aluno que deseja excluir: ")
            alunos.remove(nome)
        elif opcao == 3:
            print(alunos)
            nomealterar = input("Qual nome deseja remover? ")
            for x in alunos:
                if nomealterar==x:
                    posicao=0
                    nome = input("Qual alteração deseja fazer? ")
                    alunos[posicao] = nome
                    break
                else:
                    print("Nome não encontrado")
                posicao = posicao + 1
        elif opcao==4:
            print(alunos)

        listas = ["1-Incluir", "2-Excluir", "3-Atualizar", "4-Listar", "5-Sair"]
        opcao = int(input(f'{listas}\nSelecione opção: '))
menu()
    
