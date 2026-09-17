# Python — Funções com `def`

## 1. O que é uma função?

Uma **função** é um bloco de código criado para realizar uma determinada tarefa.

Em Python, usamos a palavra-chave `def` para **criar uma função**.

Podemos pensar em uma função como uma pequena "máquina":

```text
Entrada → Função → Resultado
```

Por exemplo:

```text
Número → Somar → Resultado
```

Uma função pode:

* executar uma tarefa;
* receber informações;
* processar essas informações;
* retornar um resultado.

---

# 2. Por que usar funções?

Imagine que precisamos mostrar uma mensagem várias vezes.

Sem função:

```python
print("Bem-vindo ao sistema!")
print("Bem-vindo ao sistema!")
print("Bem-vindo ao sistema!")
```

Podemos criar uma função:

```python
def mensagem():
    print("Bem-vindo ao sistema!")
```

Depois, basta chamar a função:

```python
mensagem()
mensagem()
mensagem()
```

### Vantagem

Em vez de repetir o código várias vezes, criamos uma função e podemos utilizá-la quando necessário.

---

# 3. Como criar uma função

A estrutura básica é:

```python
def nome_da_funcao():
    # código da função
```

Exemplo:

```python
def saudacao():
    print("Olá!")
```

Observe:

```python
def saudacao():
```

* `def` → informa que estamos criando uma função;
* `saudacao` → nome da função;
* `()` → indica os parâmetros da função;
* `:` → inicia o bloco de código.

O código que pertence à função deve possuir **indentação**.

```python
def saudacao():
    print("Olá!")
    print("Seja bem-vindo!")
```

---

# 4. Como chamar uma função

Criar uma função não significa que ela será executada automaticamente.

Precisamos **chamar** a função.

```python
def saudacao():
    print("Olá!")

saudacao()
```

Saída:

```text
Olá!
```

Podemos chamar a mesma função várias vezes:

```python
def saudacao():
    print("Olá!")

saudacao()
saudacao()
saudacao()
```

Saída:

```text
Olá!
Olá!
Olá!
```

---

# 5. Função sem parâmetros

Uma função pode não receber nenhuma informação.

Exemplo:

```python
def mostrar_menu():
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Sair")

mostrar_menu()
```

Saída:

```text
1 - Cadastrar
2 - Consultar
3 - Sair
```

Nesse caso, a função apenas executa uma tarefa.

---

# 6. Função com parâmetro

Uma função também pode receber informações.

Essas informações são chamadas de **parâmetros**.

Exemplo:

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Marcio")
```

Saída:

```text
Olá, Marcio
```

Nesse exemplo:

```python
def saudacao(nome):
```

`nome` é um **parâmetro**.

Quando chamamos:

```python
saudacao("Marcio")
```

`"Marcio"` é o valor passado para o parâmetro `nome`.

---

# 7. Outro exemplo com parâmetro

```python
def mostrar_idade(idade):
    print("Sua idade é", idade)

mostrar_idade(25)
```

Saída:

```text
Sua idade é 25
```

Podemos utilizar valores diferentes:

```python
mostrar_idade(18)
mostrar_idade(30)
mostrar_idade(45)
```

Saída:

```text
Sua idade é 18
Sua idade é 30
Sua idade é 45
```

---

# 8. Função com mais de um parâmetro

Uma função pode receber vários parâmetros.

Exemplo:

```python
def apresentar(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)

apresentar("Marcio", 30)
```

Saída:

```text
Nome: Marcio
Idade: 30
```

A ordem dos valores é importante.

```python
apresentar("Marcio", 30)
```

Significa:

```text
nome = "Marcio"
idade = 30
```

---

# 9. Funções e operações matemáticas

Podemos utilizar funções para realizar cálculos.

Exemplo:

```python
def somar(a, b):
    resultado = a + b
    print(resultado)

somar(10, 5)
```

Saída:

```text
15
```

Outro exemplo:

```python
def multiplicar(a, b):
    resultado = a * b
    print(resultado)

multiplicar(4, 3)
```

Saída:

```text
12
```

---

# 10. Usando `input()` dentro de uma função

Também podemos utilizar `input()`.

```python
def cadastrar():
    nome = input("Digite seu nome: ")
    print("Olá,", nome)

cadastrar()
```

Exemplo de execução:

```text
Digite seu nome: Marcio
Olá, Marcio
```

Nesse caso, a própria função solicita a informação ao usuário.

---

# 11. Função com `if`, `elif` e `else`

As estruturas condicionais também podem ser utilizadas dentro de funções.

Exemplo:

```python
def verificar_idade(idade):

    if idade >= 18:
        print("Maior de idade")

    else:
        print("Menor de idade")


verificar_idade(20)
```

Saída:

```text
Maior de idade
```

Outro exemplo:

```python
verificar_idade(15)
```

Saída:

```text
Menor de idade
```

---

# 12. Função com `for`

Também podemos utilizar estruturas de repetição.

```python
def contar():
    for numero in range(1, 6):
        print(numero)

contar()
```

Saída:

```text
1
2
3
4
5
```

A função organiza o código responsável pela contagem.

---

# 13. O comando `return`

Uma função pode **retornar um valor**.

Para isso utilizamos `return`.

Exemplo:

```python
def somar(a, b):
    resultado = a + b
    return resultado
```

Agora podemos armazenar o resultado:

```python
resultado = somar(10, 5)

print(resultado)
```

Saída:

```text
15
```

A diferença é importante.

Com `print()`:

```python
def somar(a, b):
    print(a + b)
```

A função apenas mostra o resultado.

Com `return`:

```python
def somar(a, b):
    return a + b
```

A função **devolve o resultado**, permitindo utilizá-lo posteriormente.

---

# 14. `return` e armazenamento em variável

Podemos fazer:

```python
def somar(a, b):
    return a + b

resultado = somar(20, 10)

print("Resultado:", resultado)
```

Saída:

```text
Resultado: 30
```

Também podemos utilizar o resultado em outra operação:

```python
def somar(a, b):
    return a + b

resultado = somar(10, 5)

dobro = resultado * 2

print(dobro)
```

Saída:

```text
30
```

---

# 15. Diferença entre `print()` e `return`

Observe os dois exemplos.

### Usando `print()`

```python
def dobro(numero):
    print(numero * 2)

dobro(5)
```

Saída:

```text
10
```

### Usando `return`

```python
def dobro(numero):
    return numero * 2

resultado = dobro(5)

print(resultado)
```

Saída:

```text
10
```

Embora a saída seja igual, o funcionamento é diferente.

| `print()`                         | `return`                                       |
| --------------------------------- | ---------------------------------------------- |
| Mostra uma informação na tela     | Devolve um valor                               |
| Usado para exibir resultados      | Usado para utilizar o resultado posteriormente |
| Não precisa armazenar o resultado | Pode armazenar o resultado em uma variável     |

---

# 16. Exemplo completo

Vamos criar uma função para verificar se um aluno foi aprovado.

```python
def verificar_aprovacao(nota):

    if nota >= 60:
        return "Aprovado"

    else:
        return "Reprovado"


nota = float(input("Digite a nota: "))

resultado = verificar_aprovacao(nota)

print(resultado)
```

Exemplo:

```text
Digite a nota: 75
Aprovado
```

---

# 17. Função utilizando texto

As funções também podem trabalhar com strings.

```python
def analisar_nome(nome):

    print("Nome:", nome)
    print("Quantidade de caracteres:", len(nome))
    print("Maiúsculo:", nome.upper())
    print("Minúsculo:", nome.lower())


nome = input("Digite seu nome: ")

analisar_nome(nome)
```

Se o usuário digitar:

```text
Marcio
```

A saída será semelhante a:

```text
Nome: Marcio
Quantidade de caracteres: 6
Maiúsculo: MARCIO
Minúsculo: marcio
```

---

# 18. Função com lista

Também podemos enviar uma lista para uma função.

```python
def mostrar_nomes(nomes):

    for nome in nomes:
        print(nome)


lista = ["Ana", "Carlos", "Marcio"]

mostrar_nomes(lista)
```

Saída:

```text
Ana
Carlos
Marcio
```

---

# 19. Várias funções no mesmo programa

Um programa pode possuir várias funções.

```python
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


print(somar(10, 5))
print(subtrair(10, 5))
print(multiplicar(10, 5))
```

Saída:

```text
15
5
50
```

Cada função possui uma responsabilidade.

```text
somar()       → realiza soma
subtrair()    → realiza subtração
multiplicar() → realiza multiplicação
```

Isso torna o programa mais organizado.

---

# 20. Boas práticas para criar funções

Ao criar funções, procure seguir algumas regras.

### 1. Use nomes claros

Evite:

```python
def x(a, b):
```

Prefira:

```python
def calcular_media(nota1, nota2):
```

---

### 2. Uma função deve ter uma responsabilidade

Evite criar uma função que faça muitas tarefas diferentes.

Por exemplo:

```python
def sistema():
    # cadastra usuário
    # calcula nota
    # imprime relatório
    # verifica senha
```

É melhor dividir:

```python
def cadastrar_usuario():
    ...


def calcular_nota():
    ...


def imprimir_relatorio():
    ...


def verificar_senha():
    ...
```

---

### 3. Use indentação corretamente

Correto:

```python
def saudacao():
    print("Olá")
```

Incorreto:

```python
def saudacao():
print("Olá")
```

Python utiliza a indentação para identificar quais comandos pertencem à função.

---

# 21. Funções ajudam a evitar repetição

Imagine este código:

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)

nome = input("Digite seu nome: ")
print("Olá,", nome)

nome = input("Digite seu nome: ")
print("Olá,", nome)
```

Podemos organizar:

```python
def saudacao():
    nome = input("Digite seu nome: ")
    print("Olá,", nome)


saudacao()
saudacao()
saudacao()
```

O código fica menor e mais organizado.

---

# 22. Modelo mental para entender `def`

Uma forma simples de lembrar:

```text
def
 ↓
CRIAR uma função
 ↓
nome da função
 ↓
receber informações
 ↓
executar código
 ↓
retornar resultado
```

Exemplo:

```python
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
```

Podemos interpretar:

```text
calcular_media
       ↓
recebe nota1 e nota2
       ↓
calcula a média
       ↓
retorna o resultado
```

---

# 23. Resumo

A palavra-chave:

```python
def
```

é utilizada para **criar funções em Python**.

A estrutura básica é:

```python
def nome_da_funcao():
    comandos
```

Uma função pode receber parâmetros:

```python
def saudacao(nome):
    print("Olá,", nome)
```

Pode realizar cálculos:

```python
def somar(a, b):
    return a + b
```

Pode utilizar estruturas condicionais:

```python
def verificar(idade):

    if idade >= 18:
        return "Maior"

    else:
        return "Menor"
```

E pode utilizar estruturas de repetição:

```python
def contar():

    for numero in range(1, 6):
        print(numero)
```

## Conceitos principais

| Conceito  | Exemplo            | Função             |
| --------- | ------------------ | ------------------ |
| `def`     | `def somar():`     | Cria uma função    |
| Parâmetro | `def somar(a, b):` | Recebe informações |
| Chamada   | `somar(10, 5)`     | Executa a função   |
| `print()` | `print(resultado)` | Mostra informação  |
| `return`  | `return resultado` | Devolve um valor   |

---

# 24. Exercícios para fixação

## Exercício 1 — Saudação

Crie uma função chamada `saudacao()` que mostre:

```text
Olá! Seja bem-vindo ao Python.
```

Depois, chame a função.

---

## Exercício 2 — Nome

Crie uma função chamada `mostrar_nome(nome)`.

A função deve receber um nome e mostrar:

```text
Olá, Marcio
```

Exemplo:

```python
mostrar_nome("Marcio")
```

---

## Exercício 3 — Soma

Crie uma função:

```python
somar(a, b)
```

Ela deve receber dois números e mostrar a soma.

Exemplo:

```python
somar(10, 20)
```

Resultado:

```text
30
```

---

## Exercício 4 — Dobro

Crie uma função chamada:

```python
dobro(numero)
```

A função deve receber um número e **retornar o dobro**.

Exemplo:

```python
resultado = dobro(8)

print(resultado)
```

Resultado:

```text
16
```

---

## Exercício 5 — Par ou ímpar

Crie uma função:

```python
verificar_numero(numero)
```

Utilize `if` e `else` para verificar se o número é:

```text
Par
```

ou

```text
Ímpar
```

Dica:

```python
numero % 2
```

---

## Exercício 6 — Média

Crie uma função:

```python
calcular_media(nota1, nota2)
```

A função deve:

1. receber duas notas;
2. calcular a média;
3. retornar a média.

Depois, mostre o resultado com `print()`.

---

## Exercício 7 — Aprovação

Crie uma função:

```python
verificar_aprovacao(media)
```

Utilize:

```text
media >= 60 → Aprovado
media < 60  → Reprovado
```

A função deve retornar a mensagem correspondente.

---

## Exercício 8 — Cadastro simples

Crie uma função chamada:

```python
cadastrar()
```

Ela deve:

1. solicitar o nome com `input()`;
2. solicitar a idade;
3. mostrar os dados cadastrados.

Exemplo:

```text
Digite seu nome: João
Digite sua idade: 20

Nome: João
Idade: 20
```

---

# Desafio final

Crie um pequeno programa utilizando **funções**, contendo:

```text
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
```

Crie uma função para cada operação:

```python
def somar(a, b):
    ...


def subtrair(a, b):
    ...


def multiplicar(a, b):
    ...


def dividir(a, b):
    ...
```

Utilize `input()`, `if`, `elif` e `else` para construir o menu.

### Objetivo

Ao final do exercício, o aluno deverá conseguir:

* criar uma função com `def`;
* chamar uma função;
* utilizar parâmetros;
* utilizar `return`;
* utilizar `if/elif/else` dentro de funções;
* utilizar `for` dentro de funções;
* organizar um programa dividindo tarefas em funções.
