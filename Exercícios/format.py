"""O script abaixo utiliza a função format() para formatar uma string com o nome e a idade de uma pessoa.
A string é formatada de forma que os valores do nome e da idade sejam substituídos pelos valores reais."""

nome = "João"
idade = 20

# Usando a função format() para formatar a string
mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)

# Imprimindo a string formatada
print(mensagem)

"""
Explicação:

A função format() é chamada com a string a ser formatada como argumento.
Dentro da string, os marcadores de posição {} são usados para indicar onde os valores serão inseridos.
Os valores a serem inseridos são passados para a função format() como argumentos após a string.
A função format() retorna a string formatada com os valores inseridos.
"""
n_float=10.23456
s_str="Jose"
n_int=5
print("o numero é {:.2f}".format(n_float))
print("o numero é {}".format(s_str))
print("o numero é {}".format(n_int))
