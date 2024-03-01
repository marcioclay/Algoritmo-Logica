
# Crie um programa que leia o nome completo de uma pessoa:
nome = str(input("Digite seu nome: \n")).strip()
# O strip() o método remove qualquer espaço em branco principal e posterior.

# O nome com todas as letras maiúsculas
print("Nome em maiúsculas: {}.".format(nome.upper()))
print(f"Nome em maiúsculas: {nome.upper()}.") #fstring

# O nome com todas minúsculas
print("Nome em minúsculas: {}.".format(nome.lower()))

# Quantas letras ao todo (sem considerar espaços)
print("Letras ao todo: {}.".format(len(nome) - nome.count(" ")))
print(f"Letras ao todo: {len(nome) - nome.count(' ')}") #fstring
# count - Retorna o número de vezes que o valor " " aparece na string:
# O len() função retorna o número de itens em um objeto.
# Quando o objeto é uma string, o len() função retorna o número de caracteres na string.

# Quantas letras tem o primeiro nome:
nome = nome.split() #Divida uma string em uma lista onde cada palavra é um item de lista:
print('O primeiro nome é "{}" e ele tem {} letras.'.format(nome[0], len(nome[0])))
print(f"O primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras.")
