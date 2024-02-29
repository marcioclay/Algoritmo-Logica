"""
Criar uma calculadora simples em Python que utilize os operadores aritméticos para realizar operações básicas: soma, subtração, multiplicação e divisão.
Instruções:
Crie um script Python que solicite ao usuário dois números e um operador.
Utilize os operadores aritméticos +, -, *, / para realizar a operação desejada.
Imprima o resultado da operação, informando os números e o operador utilizado.
"""
numero_1 = 4
numero_2 = 2

# Operações aritméticas
soma = numero_1 + numero_2
diferenca = numero_1 - numero_2
produto = numero_1 * numero_2
quociente = numero_1 / numero_2
resto = (numero_1 % numero_2)
divisao_inteira = numero_1 // numero_2

# Imprimindo resultados
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
print(f"Divisão inteira: {divisao_inteira}")

