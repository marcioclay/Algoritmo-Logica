
#Desenvolver um algoritmo em Python que utiliza a função input() para coletar dados do usuário e realizar cálculos simples.

# Solicitando os números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Realizando os cálculos
soma = numero1 + numero2
diferenca = numero1 - numero2
produto = numero1 * numero2
quociente = numero1 / numero2

# Imprimindo os resultados
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
print(f"Quociente: {quociente}")

"""
Explicação:

A função input() é utilizada para solicitar ao usuário que digite um valor.
A função int() converte a string digitada pelo usuário para um número inteiro.
Os operadores +, -, * e / são utilizados para realizar os cálculos matemáticos.
A função print() é utilizada para exibir os resultados na tela.
"""
