"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".
"""
pergunta1=int(input("Telefonou para a vítima? (0 - Não, 1 - Sim):  " ))
pergunta2=int(input("Esteve no local do crime? (0 - Não, 1 - Sim):  "))
pergunta3=int(input("Mora perto da vítima? (0 - Não, 1 - Sim):  "))
pergunta4=int(input("Devia para a vítima? (0 - Não, 1 - Sim): "))
pergunta5=int(input("Já trabalhou com a vítima? (0 - Não, 1 - Sim): " ))
respostas=pergunta1+pergunta2+pergunta3+pergunta4+pergunta5
if respostas==2:
    print("Elemento suspeito")
elif  4>=respostas>=3:
    print("Cúmplice")
elif respostas==5:
    print("Assassino")
else:
    print("Inocente")
