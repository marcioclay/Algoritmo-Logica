"""Criar um algoritmo em Python que utiliza operadores relacionais para comparar valores e tomar decisões.
Instruções:
Crie um script Python que solicite ao usuário dois números inteiros.
Utilize os operadores relacionais ==, !=, <, >, <=, >= para comparar os números digitados.
Imprima mensagens informando o resultado da comparação, utilizando linguagem clara e concisa."""

# Solicitando os números ao usuário
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

# Comparando os números com operadores relacionais
igual = numero_1 == numero_2
diferente = numero_1 != numero_2
menor = numero_1 < numero_2
maior = numero_1 > numero_2
menor_igual = numero_1 <= numero_2
maior_igual = numero_1 >= numero_2

# Imprimindo os resultados das comparações
print(f"\n{numero_1} é igual a {numero_2}? {igual}")
print(f"{numero_1} é diferente de {numero_2}? {diferente}")
print(f"{numero_1} é menor que {numero_2}? {menor}")
print(f"{numero_1} é maior que {numero_2}? {maior}")
print(f"{numero_1} é menor ou igual a {numero_2}? {menor_igual}")
print(f"{numero_1} é maior ou igual a {numero_2}? {maior_igual}")
