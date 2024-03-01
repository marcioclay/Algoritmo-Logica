"""
Descrição:

O script abaixo verifica se um número digitado pelo usuário está entre 1 e 100, se é par ou ímpar e, por fim, se é múltiplo de 3. 
Se o número estiver entre 1 e 100, o script imprime uma mensagem informando que o número está dentro da faixa. Se o número for par, 
o script imprime uma mensagem informando que o número é par. Se o número for ímpar e múltiplo de 3, o script imprime uma mensagem 
informando que o número é ímpar e múltiplo de 3. Caso contrário, o script imprime uma mensagem informando que o número não atende aos
critérios.

"""


numero = int(input("Digite um número: "))

if 1 <= numero <= 100:
  if numero % 2 == 0:
    print(f"O número {numero} é par e está dentro da faixa.")
  else:
    if numero % 3 == 0:
      print(f"O número {numero} é ímpar, múltiplo de 3 e está dentro da faixa.")
    else:
      print(f"O número {numero} é ímpar e está dentro da faixa.")
else:
  print(f"O número {numero} está fora da faixa.")


"""
Explicação:

A primeira instrução if verifica se o número está entre 1 e 100.
Se o número estiver dentro da faixa, a segunda instrução if verifica se o número é par.
Se o número for par, o bloco de código dentro do if é executado.
Se o número for ímpar, a instrução else verifica se o número é múltiplo de 3.
Se o número for múltiplo de 3, o bloco de código dentro do if dentro do else é executado.
Se o número não for par nem múltiplo de 3, o bloco de código dentro do else dentro do else é executado.
Se o número não estiver entre 1 e 100, o bloco de código dentro do else da primeira instrução if é executado.
"""
