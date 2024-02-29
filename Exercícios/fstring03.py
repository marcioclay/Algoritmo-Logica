# Definindo os números float
numero_1 = 4.58832424234
numero_2 = 87.234
numero_3 = 23.44555

# Formatando com f-strings e limitando casas decimais
numero_1_formatado = f"{numero_1:.3f}"
numero_2_formatado = f"{numero_2:.2f}"
numero_3_formatado = f"{numero_3:.1f}"

# Imprimindo os resultados
print(f"Número 1 com 3 casas decimais: {numero_1_formatado}")
print(f"Número 2 com 2 casas decimais: {numero_2_formatado}")
print(f"Número 3 com 1 casa decimal: {numero_3_formatado}")

"""
Explicação:

A notação :.3f dentro da f-string limita o número de casas decimais do numero_1 para 3.
O mesmo é feito para numero_2 com :.2f e numero_3 com :.1f.
As variáveis formatadas são impressas com suas respectivas descrições.
"""
