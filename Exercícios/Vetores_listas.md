# 🐍 Exercícios de Python: Estrutura de Dados - Listas

Lista de exercícios pedagógicos desenvolvida para alunos iniciantes em programação Python.

### 📌 Pré-requisitos

* Operadores aritméticos, relacionais e lógicos.

* Manipulação básica de Strings e Listas.

* Estruturas condicionais (`if` / `else`) e laço de repetição básico (`for`).

* *Nota:* Esta lista **não** exige o uso de funções (`def`), laços `while` ou Programação Orientada a Objetos.

---

## 📋 Lista de Exercícios

### Exercício 1: Acessando elementos por índice

Crie uma lista contendo 4 frutas e exiba na tela apenas a primeira e a última fruta utilizando os índices.

```python
frutas = ["Maçã", "Banana", "Laranja", "Uva"]

print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])
```

**Resultado Esperado:**

```text
Primeira fruta: Maçã
Última fruta: Uva
```

---

### Exercício 2: Contando elementos (`len`)

Dada uma lista com números inteiros, utilize a função `len()` para descobrir a quantidade total de elementos e exiba a resposta.

```python
numeros = [15, 22, 30, 45, 50, 68, 71]

quantidade = len(numeros)
print("A lista contém", quantidade, "elementos.")
```

**Resultado Esperado:**

```text
A lista contém 7 elementos.
```

---

### Exercício 3: Alterando um elemento da lista

Substitua o segundo nome da lista (`"Bruno"`) por `"Bernardo"` e imprima a lista atualizada.

```python
nomes = ["Ana", "Bruno", "Carla"]

nomes[1] = "Bernardo"
print(nomes)
```

**Resultado Esperado:**

```text
['Ana', 'Bernardo', 'Carla']
```

---

### Exercício 4: Adicionando itens (`append`)

Crie uma lista vazia chamada `carrinho` e adicione três produtos um por um usando o método `.append()`.

```python
carrinho = []

carrinho.append("Arroz")
carrinho.append("Feijão")
carrinho.append("Café")

print(carrinho)
```

**Resultado Esperado:**

```text
['Arroz', 'Feijão', 'Café']
```

---

### Exercício 5: Removendo itens (`remove`)

Dada uma lista de compras, remova o item `"Sabão"` utilizando o método `.remove()` e exiba a lista resultante.

```python
compras = ["Leite", "Sabão", "Pão", "Açúcar"]

compras.remove("Sabão")
print(compras)
```

**Resultado Esperado:**

```text
['Leite', 'Pão', 'Açúcar']
```

---

### Exercício 6: Verificando existência de item (`in`)

Verifique se o número `12` está presente na lista de números sorteados usando a palavra-chave `in` e uma estrutura `if/else`.

```python
sorteados = [5, 8, 12, 27, 33]

if 12 in sorteados:
    print("O número 12 foi sorteado!")
else:
    print("O número 12 não está na lista.")
```

**Resultado Esperado:**

```text
O número 12 foi sorteado!
```

---

### Exercício 7: Fatiando uma lista (Slicing)

Dada uma lista com 6 números, extraia apenas os 3 primeiros elementos utilizando o fatiamento (`[:3]`).

```python
numeros = [10, 20, 30, 40, 50, 60]

primeiros = numeros[:3]
print(primeiros)
```

**Resultado Esperado:**

```text
[10, 20, 30]
```

---

### Exercício 8: Encontrando o maior e menor valor (`max` e `min`)

Dada uma lista de notas de um estudante, encontre e imprima a maior e a menor nota utilizando as funções `max()` e `min()`.

```python
notas = [6.5, 9.0, 4.5, 8.0, 7.5]

maior = max(notas)
menor = min(notas)

print("Maior nota:", maior)
print("Menor nota:", menor)
```

**Resultado Esperado:**

```text
Maior nota: 9.0
Menor nota: 4.5
```

---

### Exercício 9: Calculando a média (`sum` e `len`)

Calcule a média aritmética das notas de uma lista utilizando a soma total (`sum()`) e a quantidade de elementos (`len()`).

```python
notas = [8.0, 7.0, 9.0]

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

print("Média do aluno:", media)
```

**Resultado Esperado:**

```text
Média do aluno: 8.0
```

---

### Exercício 10: Concatenando listas (`+`)

Junte duas listas de alunos de grupos diferentes em uma única lista chamada `turma`.

```python
grupo_a = ["João", "Maria"]
grupo_b = ["Pedro", "Sofia"]

turma = grupo_a + grupo_b
print(turma)
```

**Resultado Esperado:**

```text
['João', 'Maria', 'Pedro', 'Sofia']
```

---

### Exercício 11: Ordenando elementos (`sort`)

Ordene uma lista de idades em ordem crescente utilizando o método `.sort()`.

```python
idades = [25, 18, 40, 12, 30]

idades.sort()
print(idades)
```

**Resultado Esperado:**

```text
[12, 18, 25, 30, 40]
```

---

### Exercício 12: Contando ocorrências (`count`)

Utilize o método `.count()` para verificar quantas vezes a palavra `"Python"` aparece na lista.

```python
linguagens = ["Python", "Java", "Python", "C++", "Python"]

qtd_python = linguagens.count("Python")
print("A palavra 'Python' aparece", qtd_python, "vezes.")
```

**Resultado Esperado:**

```text
A palavra 'Python' aparece 3 vezes.
```

---

### Exercício 13: Invertendo a ordem da lista (`[::-1]`)

Exiba os elementos de uma lista na ordem inversa utilizando o fatiamento de passo negativo (`[::-1]`).

```python
cores = ["Vermelho", "Verde", "Azul", "Amarelo"]

cores_invertidas = cores[::-1]
print(cores_invertidas)
```

**Resultado Esperado:**

```text
['Amarelo', 'Azul', 'Verde', 'Vermelho']
```

---

### Exercício 14: Percorrendo a lista com o laço `for`

Utilize um laço `for` simples para percorrer uma lista de nomes e exibir uma mensagem de boas-vindas personalizada para cada pessoa.

```python
clientes = ["Lucas", "Mariana", "Gabriel"]

for nome in clientes:
    print(f"Bem-vindo(a), {nome}!")
```

**Resultado Esperado:**

```text
Bem-vindo(a), Lucas!
Bem-vindo(a), Mariana!
Bem-vindo(a), Gabriel!
```

---

### Exercício 15: Convertendo String para Lista (`split`)

Dada uma string com nomes separados por vírgula, utilize o método `.split()` para transformar o texto em uma lista e mostre o total de itens.

```python
entrada = "Ana, Bruno, Caio, Daniela"

lista_nomes = entrada.split(", ")
print("Lista convertida:", lista_nomes)
print("Total de nomes:", len(lista_nomes))
```

**Resultado Esperado:**

```text
Lista convertida: ['Ana', 'Bruno', 'Caio', 'Daniela']
Total de nomes: 4
```

---

### Exercício 16: Somando elementos de uma lista com `for`

Utilize o laço `for` e uma variável acumuladora para calcular e imprimir a soma total de todos os elementos de uma lista de inteiros.

```python
numeros = [10, 20, 30, 40, 50]
soma_total = 0

for numero in numeros:
    soma_total += numero

print("Soma total dos elementos:", soma_total)
```

**Resultado Esperado:**

```text
Soma total dos elementos: 150
```

---

### Exercício 17: Filtrando números pares com `for` e `if`

Dada uma lista de números inteiros, percorra o vetor utilizando o laço `for` e imprima apenas os números pares (utilizando o operador de resto `% 2 == 0`).

```python
numeros = [12, 7, 18, 21, 34, 5, 40]

print("Números pares encontrados:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
```

**Resultado Esperado:**

```text
Números pares encontrados:
12
18
34
40
```

---

### Exercício 18: Gerando uma nova lista com valores multiplicados

Dada uma lista de números, utilize o laço `for` para multiplicar cada valor por 2 e adicionar o resultado em uma nova lista chamada `dobros`.

```python
valores = [2, 5, 8, 11, 15]
dobros = []

for valor in valores:
    dobros.append(valor * 2)

print("Lista original:", valores)
print("Lista com os dobros:", dobros)
```

**Resultado Esperado:**

```text
Lista original: [2, 5, 8, 11, 15]
Lista com os dobros: [4, 10, 16, 22, 30]
```

---

### Exercício 19: Contando elementos sob uma condição

Dada uma lista com notas de vários alunos, utilize o laço `for` e um contador para descobrir quantos alunos tiraram nota maior ou igual a `7.0`.

```python
notas = [8.5, 5.0, 7.0, 4.5, 9.5, 6.0]
aprovados = 0

for nota in notas:
    if nota >= 7.0:
        aprovados += 1

print("Quantidade de alunos aprovados:", aprovados)
```

**Resultado Esperado:**

```text
Quantidade de alunos aprovados: 3
```

---

### Exercício 20: Percorrendo uma lista com índice (`range` e `len`)

Utilize a combinação de `range()` e `len()` dentro de um laço `for` para exibir a posição (índice) e o nome do elemento armazenado em um vetor.

```python
linguagens = ["Python", "JavaScript", "C#", "Java"]

for i in range(len(linguagens)):
    print(f"Posição {i}: {linguagens[i]}")
```

**Resultado Esperado:**

```text
Posição 0: Python
Posição 1: JavaScript
Posição 2: C#
Posição 3: Java
```