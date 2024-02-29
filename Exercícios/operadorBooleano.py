# 1. Operador OR

# Verifica se ao menos um dos valores é True
valor1 = True
valor2 = False

resultado = valor1 or valor2  # True

print(f"valor1 or valor2: {resultado}")

# Verifica se todos os valores são False
valor3 = False
valor4 = False

resultado = valor3 or valor4  # False

print(f"valor3 or valor4: {resultado}")

"""Explicação:

O operador or retorna True se pelo menos um dos valores for True.
Se todos os valores forem False, o resultado será False. """ 

# 2. Operador AND (E) 

# Verifica se todos os valores são True
valor1 = True
valor2 = True

resultado = valor1 and valor2  # True

print(f"valor1 and valor2: {resultado}")

# Verifica se ao menos um valor é False
valor3 = True
valor4 = False

resultado = valor3 and valor4  # False

print(f"valor3 and valor4: {resultado}")

""" Explicação:

O operador and retorna True somente se todos os valores forem True.
Se pelo menos um valor for False, o resultado será False. """

# 3. Operador not (NÃO):

Python
valor1 = True
valor2 = False

# Inverte o valor lógico
resultado1 = not valor1  # False
resultado2 = not valor2  # True

print(f"not valor1: {resultado1}")
print(f"not valor2: {resultado2}")

"""
Explicação:

O operador not inverte o valor lógico de um único valor.
Se o valor for True, ele se torna False.
Se o valor for False, ele se torna True. """








