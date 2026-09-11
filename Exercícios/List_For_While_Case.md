# 📋 Lista de Exercícios: Listas, `for`, `while` e `match-case` em Python

**Instruções:** Responda às questões a seguir aplicando os conceitos aprendidos sobre estruturas de repetição, 
coleções de dados e controle de fluxo condicional.

---

## 📦 Parte 1: Listas (`list`)

### Questão 1
Crie uma lista chamada `frutas` contendo 5 frutas de sua preferência. Em seguida, exiba no terminal apenas a primeira e a última fruta da lista utilizando seus respectivos índices.

### Questão 2
Dada a lista `numeros = [10, 20, 30, 40]`:
1. Adicione o número `50` ao final da lista utilizando o método `.append()`.
2. Remova o número `20` da lista.
3. Exiba o tamanho final da lista utilizando a função `len()`.

### Questão 3
Escreva um programa que crie uma lista vazia chamada `notas`. Peça ao usuário para digitar 3 notas (valores decimais) uma por uma, adicione cada nota à lista e, ao final, exiba a lista completa na tela.

### Questão 4
Dada a lista `linguagens = ["Python", "C++", "Java", "JavaScript"]`, peça para o usuário digitar o nome de uma linguagem de programação. Utilizando o operador `in`, verifique se essa linguagem está presente na lista e exiba uma mensagem informando o resultado.

### Questão 5
Dada a lista de valores `valores = [15, 30, 45, 60]`, utilize a função embutida `sum()` para calcular e exibir a soma total de todos os elementos da lista.

---

## 🔄 Parte 2: Laço de Repetição `for`

### Questão 6
Utilizando a função `range()`, escreva um programa com a estrutura `for` que imprima todos os números inteiros de **1 a 15** na tela.

### Questão 7
Dada a lista `numeros = [2, 5, 8, 11, 14]`, crie um laço `for` que percorra essa lista e imprima o **dobro** de cada número.

### Questão 8
Escreva um programa que solicite ao usuário um número inteiro e exiba a **tabuada** desse número de 1 a 10 utilizando o laço `for`.

*Exemplo de saída para o número 5:*
```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

### Questão 9
Dada a lista de idades `idades = [12, 18, 25, 10, 30, 15, 22]`, utilize um laço `for` e uma estrutura condicional `if` para contar e exibir **quantas pessoas são maiores de idade** (idade igual ou superior a 18 anos).

### Questão 10
Escreva um programa que percorra os números de **1 a 20** usando `for` e imprima apenas os números que forem **pares** (dica: utilize o operador de resto `% 2 == 0`).

---

## 🔁 Parte 3: Laço de Repetição `while`

### Questão 11
Crie um programa que faça uma **contagem regressiva** de **10 até 1** utilizando a estrutura `while`. Ao final do laço, exiba a mensagem `"Fim da contagem!"`.

### Questão 12
Escreva um programa de validação de senha. O programa deve definir uma senha padrão (ex: `"python123"`) e solicitar que o usuário a digite dentro de um laço `while`. O laço só deve encerrar quando o usuário acertar a senha.

### Questão 13
Crie um programa que peça para o usuário digitar números inteiros repetidamente.
* O programa deve somar todos os números digitados.
* O laço `while` deve parar quando o usuário digitar o número `0`.
* Ao final, exiba a soma total acumulada.

### Questão 14
Escreva um programa que peça para o usuário digitar valores inteiros e os armazene em uma lista. O laço `while` deve continuar rodando até que o usuário digite um **número negativo**. Ao encerrar, exiba a lista de números armazenados (sem incluir o número negativo final).

### Questão 15
Simule a entrada de um caixa eletrônico: solicite ao usuário o valor de um saque. Enquanto o valor digitado for **menor ou igual a zero**, o programa deve exibir uma mensagem de erro e pedir para digitar o valor novamente usando `while`.

---

## 🔀 Parte 4: Seleção com `match-case`

### Questão 16
Escreva um programa que solicite ao usuário um número inteiro de **1 a 7** e, utilizando `match-case`, exiba o dia da semana correspondente:
* `1` ➔ Domingo
* `2` ➔ Segunda-feira
* `3` ➔ Terça-feira
* ...
* `7` ➔ Sábado
* Qualquer outro valor ➔ `"Dia inválido!"`

### Questão 17
Crie uma calculadora simples. O programa deve pedir dois números reais e um caractere representando a operação desejada (`"+"`, `"-"`, `*`, `"/"`). Utilize `match-case` para identificar a operação e exibir o resultado da conta.

### Questão 18
Uma loja classifica seus produtos de acordo com um código informado pelo cliente:
* Código `"A1"` ou `"A2"` ➔ Categoria: **Eletrônicos**
* Código `"B1"` ou `"B2"` ➔ Categoria: **Vestuário**
* Código `"C1"` ➔ Categoria: **Alimentos**
* Qualquer outro código ➔ **Código desconhecido**

Crie o programa utilizando `match-case` e a sintaxe de agrupamento de padrões com `|`.

---

## 🧠 Parte 5: Questões Integradas (Desafios)

### Questão 19
Dada a lista de comandos `comandos = ["iniciar", "pausar", "invalido", "parar"]`:
1. Percorra a lista de comandos utilizando um laço `for`.
2. Para cada elemento da lista, utilize uma estrutura `match-case` para exibir uma das seguintes mensagens:
   * `"iniciar"` ➔ `"Sistema iniciando..."`
   * `"pausar"` ➔ `"Sistema pausado."`
   * `"parar"` ➔ `"Sistema desligado."`
   * Qualquer outro ➔ `"Comando não reconhecido."`

### Questão 20
Crie um sistema simples de **Lista de Compras**:
1. Crie uma lista vazia chamada `compras`.
2. Utilize um laço `while` para pedir ao usuário que digite o nome de um produto.
3. Se o usuário digitar `"sair"`, o laço `while` deve ser encerrado.
4. Caso contrário, adicione o produto à lista `compras`.
5. Após o encerramento do laço, utilize um laço `for` para exibir todos os itens digitados no seguinte formato:
```text
Item 1: Arroz
Item 2: Feijão
Item 3: Leite
```
