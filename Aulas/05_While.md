# Repetições While em Python
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



###Exemplos com While e If, While e For:

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

Este código é equivalente ao exemplo de while e for.
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
