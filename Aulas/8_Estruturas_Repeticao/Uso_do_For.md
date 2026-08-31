## 🔄 Entendendo o Laço de Repetição for em Python 

## Tópico: Estruturas de Repetição (for)

### 1. O que é um Laço de Repetição?
   Imagine que você trabalha na recepção de uma empresa e recebeu uma pilha com 5 crachás para entregar aos funcionários que acabaram de chegar.
   O que você faz?
   1. Pega o 1º crachá e entrega para a pessoa.
   2. Pega o 2º crachá e entrega para a pessoa.
   3. Pega o 3º crachá e entrega para a pessoa.
   4. Repete esse processo até que os crachás da pilha acabem.

Na programação, isso se chama Iteração ou Laço de Repetição (Loop). 
O laço for serve justamente para isso: executar um bloco de código várias vezes, passando item por item de uma 
coleção (como uma lista de nomes, uma sequência de números ou os caracteres de um texto).

### 2. Por que usar o for?
Veja este problema: se o seu professor pedir para você imprimir na tela o número $1$ até o número $5$, você poderia escrever:

```
print(1)
print(2)
print(3)
print(4)
print(5)
```

Funciona? Funciona! Mas e se o professor pedir para imprimir do $1$ até o $1.000$? 
Você escreveria mil linhas de print?Com o laço for, resolvemos isso em apenas 2 linhas de código:
```
for numero in range(1, 1001):
    print(numero)
```

# 3. A Anatomia do `for` — Sintaxe

A estrutura básica do `for` em Python é composta por **4 elementos principais**:

```python
for item in colecao:
    # Código a ser repetido para cada item
```

## Entendendo palavra por palavra

* `for`: palavra reservada do Python que significa **"para cada"**.
* `item`: variável temporária que você cria. Ela vai guardar o elemento atual da vez.
* `in`: palavra reservada que significa **"em"** ou **"dentro de"**.
* `colecao`: grupo de elementos que você deseja percorrer, como uma lista, um texto ou uma sequência numérica.
* `:` (dois-pontos): **obrigatório**. Indica o início do bloco de instruções.
* **Indentação (recuo)**: espaço antes da linha de código. Normalmente utilizamos **4 espaços**. Tudo que estiver indentado pertence ao laço de repetição.

---

# 4. Praticando com Exemplos

## Exemplo 1 — Percorrendo uma Lista de Nomes

Vamos criar uma lista com nomes de alunos e fazer o Python saudar cada um deles:

```python
alunos = ["Ana", "Bruno", "Carla", "Diego"]

for aluno in alunos:
    print(f"Presente, {aluno}!")
```

### O que o Python faz?

O `for` percorre a lista **um elemento por vez**:

1. **Volta 1:** `aluno` recebe `"Ana"` → imprime `"Presente, Ana!"`
2. **Volta 2:** `aluno` recebe `"Bruno"` → imprime `"Presente, Bruno!"`
3. **Volta 3:** `aluno` recebe `"Carla"` → imprime `"Presente, Carla!"`
4. **Volta 4:** `aluno` recebe `"Diego"` → imprime `"Presente, Diego!"`
5. A lista acabou → o Python encerra o laço.

### Saída

```text
Presente, Ana!
Presente, Bruno!
Presente, Carla!
Presente, Diego!
```

---

## Exemplo 2 — Percorrendo uma String

Em Python, um texto pode ser percorrido **caractere por caractere**.

```python
palavra = "PYTHON"

for letra in palavra:
    print(letra)
```

### Saída no terminal

```text
P
Y
T
H
O
N
```

Nesse exemplo, a variável `letra` recebe um caractere diferente a cada repetição.

---

## Exemplo 3 — Usando o Contador `range()`

Quando não temos uma lista pronta, mas queremos repetir algo um número determinado de vezes, podemos utilizar a função `range()`.

### a) `range(parada)`

Gera números começando do `0` até o limite informado, **sem incluir o limite**.

```python
for i in range(5):
    print(i)
```

### Saída

```text
0
1
2
3
4
```

> **Atenção:** o número `5` não é incluído.

---

### b) `range(inicio, parada)`

Podemos definir onde a sequência começa e onde termina.

```python
for i in range(1, 6):
    print(f"Rodada {i}")
```

### Saída

```text
Rodada 1
Rodada 2
Rodada 3
Rodada 4
Rodada 5
```

Observe que o número final `6` **não é incluído**.

---

### c) `range(inicio, parada, passo)`

Podemos definir também de quanto em quanto os números serão incrementados.

```python
# Imprimir apenas os números pares de 2 a 10

for numero in range(2, 11, 2):
    print(numero)
```

### Saída

```text
2
4
6
8
10
```

Nesse caso:

* `2` → início
* `11` → parada
* `2` → passo

O `11` não é incluído.

---

# 5. Exemplo Prático Integrado — Somando Notas

Vamos utilizar o `for` em um problema comum de lógica de programação: **somar as notas de um aluno e calcular a média**.

```python
notas = [7.5, 8.0, 6.5, 9.0]
soma_total = 0

for nota in notas:
    soma_total = soma_total + nota

quantidade = len(notas)
media = soma_total / quantidade

print(f"Soma total das notas: {soma_total}")
print(f"Média final: {media:.2f}")
```

### O que acontece?

A variável `soma_total` começa com `0`.

A cada repetição do `for`, uma nota é adicionada:

```text
0 + 7.5 = 7.5
7.5 + 8.0 = 15.5
15.5 + 6.5 = 22.0
22.0 + 9.0 = 31.0
```

Depois calculamos a quantidade de notas:

```python
quantidade = len(notas)
```

E finalmente calculamos a média:

```python
media = soma_total / quantidade
```

### Saída

```text
Soma total das notas: 31.0
Média final: 7.75
```

> **Dica:** a variável `soma_total` é chamada de **acumulador**, pois seu valor vai sendo atualizado a cada repetição.

---

# ⚠️ Atenção! Erros Comuns dos Iniciantes

## 1. Esquecer os dois-pontos `:`

Os dois-pontos são obrigatórios no final da declaração do `for`.

### ❌ Errado

```
for i in range(5)
    print(i)
```

### ✅ Correto

```
for i in range(5):
    print(i)
```

---

## 2. Esquecer a indentação

O código que pertence ao `for` precisa estar indentado.

### ❌ Errado

```
for i in range(3):
print(i)
```

### ✅ Correto

```
for i in range(3):
    print(i)
```

> **Regra importante:** em Python, a indentação não é apenas uma questão de organização. Ela define quais instruções pertencem ao bloco do `for`.

---

# 📝 Exercícios de Fixação

Tente resolver os exercícios abaixo utilizando seu editor de código, como **VS Code, Replit ou IDLE**.

---

## 🎯 Exercício 1 — Tabuada Simples

Escreva um programa que:

1. Peça um número inteiro ao usuário.
2. Utilize o laço `for`.
3. Utilize a função `range()`.
4. Mostre a tabuada desse número de `1` a `10`.

### Exemplo de execução

Se o usuário digitar:

```
5
```

O programa deverá produzir:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## 🎯 Exercício 2 — Contador Regressivo

Crie um programa que faça uma contagem regressiva para o lançamento de um foguete, começando em `10` e terminando em `0`.

Ao final, o programa deverá imprimir:

```
Decolar! 🚀
```

### Exemplo de saída

```
10
9
8
7
6
5
4
3
2
1
0
Decolar! 🚀
```

### 💡 Dica

Utilize o terceiro parâmetro do:

```
range(inicio, parada, passo)
```

Para fazer uma contagem regressiva, o `passo` deverá ser negativo.

---

## 🎯 Exercício 3 — Verificador de Aprovados

Considere a seguinte lista de notas:

```
notas = [4.5, 7.0, 8.5, 5.0, 9.0, 6.0]
```

Crie um programa que utilize `for` para percorrer a lista e verificar cada nota.

O programa deverá imprimir:

* `"Aprovado"` se a nota for **maior ou igual a `6.0`**.
* `"Recuperação"` se a nota for **menor que `6.0`**.

### 💡 Dica

Você precisará utilizar:

* `for`
* `if`
* operador relacional `>=`
* operador relacional `<`

### Exemplo de estrutura

```
notas = [4.5, 7.0, 8.5, 5.0, 9.0, 6.0]

for nota in notas:
    # Faça a verificação aqui
```

---

# 📌 Resumo

O `for` é utilizado quando queremos **repetir um conjunto de instruções para cada elemento de uma sequência**.

A estrutura básica é:

```
for item in colecao:
    # instruções
```

Podemos utilizar o `for` para percorrer:

* Listas
* Strings
* Sequências numéricas
* Resultados da função `range()`

A função `range()` pode ser utilizada de três formas principais:

```
range(parada)
```

```
range(inicio, parada)
```

```
range(inicio, parada, passo)
```

> **Conceito fundamental:** o `for` percorre os elementos **um por vez**, executando o bloco indentado para cada elemento.



