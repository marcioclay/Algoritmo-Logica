# Repetições While e Do While em Python
## Introdução

As repetições while e do while são estruturas de controle que permitem executar um bloco de código enquanto uma condição específica for verdadeira. No entanto, existem diferenças importantes entre elas:

### While:

Verifica a condição antes de executar o bloco de código.
Se a condição for falsa, o bloco de código não é executado.
É usado quando o número de iterações é desconhecido.
Exemplo:

```
numero = 1

while numero <= 5:
  print(numero)
  numero += 1
```

### Explicação:

#### While:
A variável numero é inicializada com o valor 1.
O loop while é executado enquanto numero for menor ou igual a 5.
Dentro do loop, o valor de numero é impresso e incrementado em 1.
O loop termina quando numero é igual a 6.

#### Do While:

Executa o bloco de código pelo menos uma vez.
Verifica a condição após executar o bloco de código.
É usado quando o número de iterações é desconhecido e queremos garantir que o bloco de código seja executado pelo menos uma vez.
Exemplo:

```
numero = 1

do:
  print(numero)
  numero += 1
while numero <= 5
```

### Explicação:

A variável numero é inicializada com o valor 1.
O loop do while é executado pelo menos uma vez.
Dentro do loop, o valor de numero é impresso e incrementado em 1.
A condição é verificada após a execução do bloco de código.
O loop termina quando numero é igual a 6.

###Exemplos com While e If, While e For, Do While com If e Do While com For:

### While e If:

```
numero = 1

while numero <= 5:
  if numero % 2 == 0:
    print(f"{numero} é par")
  else:
    print(f"{numero} é ímpar")
  numero += 1
```

#### Explicação:

Este código verifica se o número é par ou ímpar e imprime a mensagem adequada.
While e For:

```
lista_numeros = [1, 2, 3, 4, 5]

numero = 0

while numero < len(lista_numeros):
  print(lista_numeros[numero])
  numero += 1
```

#### Explicação:

Este código percorre uma lista e imprime cada elemento da lista.
Do While com If:

```
numero = 1

do:
  print(numero)
  numero += 1
while numero <= 5 and numero % 2 == 0
```

#### Explicação:

Este código imprime os números pares de 1 a 5.
Do While com For:

```
lista_numeros = [1, 2, 3, 4, 5]

numero = 0

do:
  print(lista_numeros[numero])
  numero += 1
while numero < len(lista_numeros)
```

#### Explicação:

Este código é equivalente ao exemplo de while e for.
