# A função enumerate() em Python é uma função embutida que permite iterar sobre uma sequência (como uma lista, tupla ou string) enquanto acompanha o índice de cada elemento. 
# Ela retorna um objeto enumerado que gera pares de índice e valor, tornando mais fácil acessar tanto o índice quanto o valor de cada elemento durante a iteração.

Sintaxe:

```
enumerate(iterável, início=0)
iterável: A sequência que você deseja iterar (lista, tupla, string, etc.).
início (opcional): O valor inicial do contador (o padrão é 0).
```
Exemplos:

## 1. Iterando sobre uma lista com índices:

```
frutas = ['maçã', 'banana', 'laranja']

for indice, fruta in enumerate(frutas):
    print(f'Índice: {indice}, Fruta: {fruta}')
Saída:

Índice: 0, Fruta: maçã
Índice: 1, Fruta: banana
Índice: 2, Fruta: laranja
```

### Neste exemplo, enumerate() retorna um objeto enumerado que gera pares de índice e valor para cada elemento da lista frutas. O loop for desempacota cada par em indice e fruta, permitindo que você acesse ambos.

## 2. Iterando com um índice inicial diferente:

```
frutas = ['maçã', 'banana', 'laranja']

for indice, fruta in enumerate(frutas, início=1):
    print(f'Índice: {indice}, Fruta: {fruta}')
Saída:

Índice: 1, Fruta: maçã
Índice: 2, Fruta: banana
Índice: 3, Fruta: laranja
```
Neste exemplo, o parâmetro início=1 faz com que o contador comece em 1 em vez de 0.

## 3. Iterando sobre uma string com índices:

```
texto = 'Python'

for indice, caractere in enumerate(texto):
    print(f'Índice: {indice}, Caractere: {caractere}')
Saída:

Índice: 0, Caractere: P
Índice: 1, Caractere: y
Índice: 2, Caractere: t
Índice: 3, Caractere: h
Índice: 4, Caractere: o
Índice: 5, Caractere: n
```
Neste exemplo, enumerate() itera sobre a string texto e retorna os índices e caracteres correspondentes.

Casos de uso comuns:

Acessar o índice e o valor de elementos em uma lista ou tupla simultaneamente.
Criar um dicionário onde as chaves são os índices e os valores são os elementos da lista.
Iterar sobre uma lista e modificar elementos com base em seus índices.
