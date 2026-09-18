x = None
nomes = []

while x != 5:
    print("""
    #####################
    # 1. Incluir 👍     #
    # 2. Excluir 🤦‍♀️    #
    # 3. Listar ✔       #
    # 4. Atualizar 😎   #
    # 5. Sair 😜        #
    #####################
    """)

    x = int(input("Digite a opção: "))

    if x == 1:
        nome = input("Digite seu nome: ")
        nomes.append(nome)
    elif x == 2:
        nome = input("Digite o nome para excluir: ")
        if nome in nomes:
            nomes.remove(nome)
            print(f"{nome} removido!")
        else:
            print("Nome não encontrado.")

    elif x == 3:
        print("Nomes na lista:", nomes)
    elif x == 4:
        antigo = input("Digite o nome que deseja atualizar: ")
        if antigo in nomes:
            novo = input("Digite o novo nome: ")
            indice = nomes.index(antigo)
            nomes[indice] = novo
            print("Nome atualizado!")
        else:
            print("Nome não encontrado.")

    elif x == 5:
        print("Saindo do programa... Até mais!")
    else:
        print("Opção inválida! Tente novamente.")

print("\nLista final de nomes:", nomes)
