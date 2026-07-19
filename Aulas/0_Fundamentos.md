# FUNDAMENTOS DA PROGRAMAÇÃO

## 1. O que é Programação?

A programação é o processo de criar instruções para que um computador realize determinadas tarefas.

Um computador, por si só, não possui a capacidade de compreender diretamente uma instrução como:

> “Calcule a média das notas dos alunos.”

Para que essa tarefa seja realizada, é necessário transformar essa instrução em uma sequência de comandos que o computador consiga interpretar e executar.

Essa sequência de instruções é escrita utilizando uma **linguagem de programação**, como:

* Python;
* Java;
* C;
* C++;
* JavaScript;
* C#.

Um programa pode ser entendido como um conjunto de instruções organizadas para resolver um determinado problema ou realizar uma determinada tarefa.

### Exemplo

Imagine um sistema que deve calcular a média de um aluno.

Uma pessoa poderia descrever a tarefa da seguinte maneira:

1. Receber a primeira nota;
2. Receber a segunda nota;
3. Somar as duas notas;
4. Dividir o resultado por dois;
5. Exibir a média.

O programador transforma essa sequência de ações em instruções utilizando uma linguagem de programação.

Em Python, por exemplo:

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)
```

O computador executará as instruções na ordem em que foram programadas.

Portanto, programar significa:

> **Analisar um problema, elaborar uma solução e transformar essa solução em instruções que um computador possa executar.**

---

# 2. Algoritmos e Programas

## 2.1 O que é um algoritmo?

Um **algoritmo** é uma sequência ordenada de passos utilizada para resolver um problema ou realizar uma tarefa.

Apesar de o termo algoritmo ser muito utilizado na computação, ele não é exclusivo dos computadores.

Uma receita de bolo, por exemplo, pode ser considerada um algoritmo.

### Exemplo: preparar um café

1. Colocar água em um recipiente;
2. Aquecer a água;
3. Colocar o café no filtro;
4. Despejar a água quente sobre o café;
5. Aguardar a filtragem;
6. Servir o café.

Essa sequência possui:

* **Início**;
* **Passos ordenados**;
* **Objetivo**;
* **Resultado final**.

Portanto, podemos dizer que existe um algoritmo para preparar o café.

Na computação, o princípio é semelhante. A diferença é que o algoritmo será utilizado para solucionar problemas de forma que possa ser executado por uma pessoa ou transformado em um programa de computador.

---

## 2.2 Características de um algoritmo

Um algoritmo deve apresentar algumas características importantes.

### Sequência

As instruções devem possuir uma ordem lógica.

Por exemplo:

```text
1. Receber a nota.
2. Verificar a nota.
3. Exibir o resultado.
```

Não faria sentido tentar verificar a nota antes de recebê-la.

---

### Clareza

As instruções devem ser compreensíveis e não apresentar ambiguidades.

Uma instrução como:

> “Faça o cálculo.”

é muito vaga.

Uma instrução mais clara seria:

> “Some as duas notas e divida o resultado por dois.”

---

### Finitude

Um algoritmo deve possuir uma sequência de passos que termine.

Por exemplo:

```text
1. Ler o número.
2. Multiplicar o número por 2.
3. Exibir o resultado.
4. Encerrar.
```

O algoritmo possui um fim definido.

---

### Entrada

São os dados fornecidos ao algoritmo.

Exemplos:

* Nome do aluno;
* Nota;
* Idade;
* Número de produtos;
* Senha.

---

### Processamento

É o conjunto de operações realizadas sobre os dados recebidos.

Exemplos:

* Somar;
* Comparar;
* Calcular;
* Classificar;
* Verificar.

---

### Saída

É o resultado produzido pelo algoritmo.

Exemplos:

* Média do aluno;
* Mensagem de aprovação;
* Valor total da compra;
* Resultado de uma pesquisa.

---

## 2.3 Entrada, processamento e saída

Uma forma simples de compreender um algoritmo é utilizar o modelo:

```text
ENTRADA → PROCESSAMENTO → SAÍDA
```

### Exemplo: cálculo da média

**Entrada:**

```text
Nota 1
Nota 2
```

**Processamento:**

```text
Média = (Nota 1 + Nota 2) / 2
```

**Saída:**

```text
Exibir a média
```

Representação:

```text
┌─────────┐
│ Entrada │
└────┬────┘
     │
     ▼
┌──────────────┐
│ Processamento│
└──────┬───────┘
       │
       ▼
┌────────┐
│ Saída  │
└────────┘
```

Esse modelo é fundamental para compreender o funcionamento de praticamente qualquer programa.

---

# 3. Diferença entre Algoritmo e Programa

Embora os termos algoritmo e programa estejam relacionados, eles não significam exatamente a mesma coisa.

## Algoritmo

É a descrição lógica dos passos necessários para resolver um problema.

Exemplo:

```text
Início

1. Ler a primeira nota.
2. Ler a segunda nota.
3. Calcular a média.
4. Exibir a média.

Fim
```

## Programa

É a implementação desse algoritmo utilizando uma linguagem de programação.

Exemplo:

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(media)
```

Podemos fazer a seguinte comparação:

> **Algoritmo é o planejamento da solução. Programa é a implementação desse planejamento em uma linguagem de programação.**

Uma analogia simples:

| Desenvolvimento de software | Construção de uma casa |
| --------------------------- | ---------------------- |
| Algoritmo                   | Projeto da casa        |
| Código-fonte                | Construção             |
| Programa executável         | Casa pronta            |

Antes de construir uma casa, normalmente é necessário elaborar um projeto.

Da mesma forma, antes de desenvolver um programa, é importante analisar o problema e elaborar um algoritmo.

---

# 4. O que são Problemas Computacionais?

Um **problema computacional** é uma situação que pode ser resolvida, total ou parcialmente, por meio de um computador.

Para isso, o problema precisa ser analisado e transformado em uma sequência de instruções.

### Exemplo

Imagine o seguinte problema:

> Uma escola precisa calcular a média dos alunos e informar se cada aluno foi aprovado ou reprovado.

Esse problema pode ser resolvido por um programa.

Primeiro, precisamos identificar:

### Dados de entrada

* Nome do aluno;
* Primeira nota;
* Segunda nota.

### Processamento

* Calcular a média;
* Comparar a média com o valor mínimo para aprovação.

### Saída

* Nome do aluno;
* Média;
* Situação: aprovado ou reprovado.

O problema pode ser representado da seguinte forma:

```text
Dados do aluno
      │
      ▼
┌─────────────────────┐
│ Receber as notas    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Calcular a média    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Verificar a média   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Exibir o resultado  │
└─────────────────────┘
```

---

# 5. Como Resolver um Problema Computacional?

A resolução de um problema computacional normalmente passa por várias etapas.

## Etapa 1 — Compreender o problema

Antes de programar, é necessário compreender exatamente o que deve ser resolvido.

Perguntas importantes:

* Qual é o problema?
* Qual é o objetivo?
* Quais informações serão necessárias?
* Qual resultado deve ser produzido?

---

## Etapa 2 — Identificar as entradas

Devemos identificar quais dados serão fornecidos ao programa.

### Exemplo

Problema:

> Calcular o valor total de uma compra.

Entradas:

```text
Preço do produto
Quantidade comprada
```

---

## Etapa 3 — Definir o processamento

É necessário determinar quais operações serão realizadas.

```text
Valor total = preço × quantidade
```

---

## Etapa 4 — Definir as saídas

Devemos definir quais informações serão apresentadas ao usuário.

```text
Valor total da compra
```

---

## Etapa 5 — Elaborar o algoritmo

A solução pode ser descrita da seguinte forma:

```text
Início

1. Ler o preço do produto.
2. Ler a quantidade.
3. Multiplicar o preço pela quantidade.
4. Exibir o valor total.

Fim
```

---

## Etapa 6 — Implementar o programa

Depois que o algoritmo foi elaborado, ele pode ser transformado em código.

```python
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

print("Valor total:", total)
```

---

## Etapa 7 — Testar a solução

Após criar o programa, é necessário verificar se ele funciona corretamente.

Por exemplo:

```text
Preço: 10
Quantidade: 3
```

Resultado esperado:

```text
Valor total: 30
```

Se o programa apresentar um resultado diferente, será necessário investigar o problema.

---

# 6. Exemplo Completo

## Problema

Uma loja deseja calcular o valor total de uma compra.

## Análise

### Entrada

```text
Preço do produto
Quantidade
```

### Processamento

```text
Preço × Quantidade
```

### Saída

```text
Valor total
```

## Algoritmo

```text
Início

Leia o preço do produto.
Leia a quantidade.
Calcule o valor total.
Exiba o valor total.

Fim
```

## Programa

```python
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

print("Valor total da compra:", total)
```

---

# 7. A Importância da Lógica de Programação

A linguagem de programação é apenas uma ferramenta utilizada para implementar uma solução.

Um programador pode conhecer muitos comandos de Python, Java ou C, mas ainda assim ter dificuldades para resolver problemas se não souber analisar e organizar o raciocínio.

Por isso, a lógica de programação é fundamental.

Podemos resumir o processo da seguinte forma:

```text
PROBLEMA
   ↓
ANÁLISE
   ↓
ALGORITMO
   ↓
CÓDIGO
   ↓
TESTE
   ↓
SOLUÇÃO
```

Um bom programador não começa simplesmente digitando código.

Antes de programar, ele procura responder:

> **Qual é o problema?**

Depois:

> **Quais dados são necessários?**

Em seguida:

> **Quais operações devem ser realizadas?**

E finalmente:

> **Qual resultado deve ser apresentado?**

---

# 8. Resumo

* **Programação** é o processo de criar instruções para que um computador execute tarefas.
* **Algoritmo** é uma sequência ordenada de passos para resolver um problema.
* **Programa** é a implementação de um algoritmo utilizando uma linguagem de programação.
* **Problema computacional** é uma situação que pode ser solucionada por meio de um computador.
* A resolução de problemas geralmente envolve:

  * Entrada;
  * Processamento;
  * Saída.
* Antes de escrever código, é importante compreender o problema e elaborar uma solução lógica.
* A programação é mais do que conhecer comandos: é saber **analisar problemas e construir soluções**.

---

# Atividade de Fixação

Para cada problema abaixo, identifique:

**a)** As entradas;
**b)** O processamento;
**c)** As saídas.

### 1. Calcular a área de um retângulo.

### 2. Calcular a média de três notas.

### 3. Calcular o valor total de uma compra.

### 4. Converter uma temperatura de Celsius para Fahrenheit.

### 5. Calcular a idade de uma pessoa a partir do ano de nascimento.

### 6. Verificar se um aluno foi aprovado com base em sua média.

### 7. Calcular o valor de uma corrida de táxi com base na distância percorrida.

### 8. Calcular o salário de um funcionário com base no salário e nas horas trabalhadas.

## Desafio

Escolha um dos problemas acima e escreva um algoritmo utilizando apenas linguagem natural, sem utilizar código de programação.

Exemplo:

```text
Problema: calcular a área de um retângulo.

Início

1. Ler a base.
2. Ler a altura.
3. Multiplicar a base pela altura.
4. Exibir a área.

Fim
```
