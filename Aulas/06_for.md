# Repetição For em Python

A repetição for é uma estrutura de controle que permite executar um bloco de código para cada elemento de uma sequência.

## Como funciona:

Declaração da variável de controle: Uma variável é declarada para iterar sobre a sequência.
Sequência: Uma sequência de valores é fornecida, como uma lista, string ou tupla.
Bloco de código: O código dentro do bloco for é executado para cada elemento da sequência.
Situações de uso:

Percorrer uma lista: Imprimir cada elemento de uma lista, calcular a soma dos elementos de uma lista, etc.
Iterar sobre uma string: Extrair caracteres de uma string, contar o número de vogais em uma string, etc.
Executar um código um número determinado de vezes: Gerar uma sequência de números, imprimir uma mensagem n vezes, etc.
Exemplos:

#### Exemplo 1: Percorrer uma lista

```
lista_frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in lista_frutas:
  print(f"Eu gosto de comer {fruta}.")
```

#### Explicação:

O loop for itera sobre a lista lista_frutas.
A variável fruta é utilizada para armazenar cada elemento da lista durante a iteração.
O código dentro do bloco for é executado para cada elemento da lista, imprimindo uma mensagem com o nome da fruta.
Exemplo 2: For com While e If

```
numero = 1

while numero <= 10:
  for i in range(2, numero):
    if numero % i == 0:
      break
  else:
    print(f"{numero} é primo.")
  numero += 1
```

#### Explicação:

Este código verifica se um número é primo.
O loop while itera de 1 a 10.
O loop for itera de 2 ao número atual.
Se o número for divisível por qualquer número entre 2 e ele mesmo, não é primo.
Se o número não for divisível por nenhum número entre 2 e ele mesmo, é primo.

Conclusão:

A repetição for é uma ferramenta poderosa para iterar sobre sequências e executar um bloco de código para cada elemento.
