"""
O script abaixo verifica se um número digitado pelo usuário está entre 1 e 10, entre 11 e 20, ou se é maior que 20.
Se o número estiver entre 1 e 10, o script imprime uma mensagem informando que o número é menor que 10. 
Se o número estiver entre 11 e 20, o script imprime uma mensagem informando que o número está entre 11 e 20. 
Caso contrário, o script imprime uma mensagem informando que o número é maior que 20.
"""


numero = int(input("Digite um número: "))

if numero <= 10:
  print(f"O número {numero} é menor que 10.")
elif numero <= 20:
  print(f"O número {numero} está entre 11 e 20.")
else:
  print(f"O número {numero} é maior que 20.")
