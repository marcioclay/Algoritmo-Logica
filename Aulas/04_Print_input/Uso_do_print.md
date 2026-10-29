## A função print() em Python

Quando começamos a aprender programação, uma das primeiras funções que utilizamos é a print().

A função print() serve para exibir informações na tela. Ela é muito utilizada para mostrar mensagens ao usuário, apresentar resultados de cálculos e verificar se o programa está funcionando corretamente.

Sempre que desejamos que alguma informação apareça na tela, utilizamos a função print().

Sintaxe: 
```
print(valor)
```

O valor pode ser um texto, um número, uma variável ou até mesmo o resultado de uma operação matemática. 

### 1. Exibindo um texto

Podemos utilizar aspas simples (' ') ou aspas duplas (" ").
```
print("Olá, mundo!")
```
Saída:
```
Olá, mundo!
```
Outro exemplo:
```
print("Bem-vindo ao curso de Python!")
```

### 2. Exibindo números

Também é possível mostrar números diretamente.
```
print(10)
print(25.8)
```
Saída
```
10
25.8
```

### 3. Exibindo variáveis

Na maioria das vezes, o print() é utilizado para mostrar o conteúdo de uma variável.
```
nome = "Maria"
idade = 20

print(nome)
print(idade)
```

Saída
```
Maria
20
```

### 4. Exibindo várias informações

Podemos informar vários valores separados por vírgula.

```
nome = "Carlos"
idade = 18

print(nome, idade)
```

Saída
```
Carlos 18
```

Observe que o Python coloca um espaço automaticamente entre os valores. 

### 5. Concatenando textos

Também podemos juntar textos utilizando o operador +.

```
nome = "Ana"

print("Olá " + nome)
```

Saída
```
Olá Ana
```
Importante: O operador + funciona apenas quando todos os valores são do tipo texto (str).

Por exemplo, o código abaixo gera erro:
```
idade = 20

print("Idade: " + idade)
```

Para corrigir: 

```
idade = 20

print("Idade: " + str(idade))
```

### 6. Utilizando f-strings (forma recomendada)

A partir do Python 3.6, foi introduzida a f-string, que tornou a escrita muito mais simples.

Basta colocar a letra f antes das aspas.

Dentro das chaves {} colocamos as variáveis.

```
nome = "Pedro"
idade = 25

print(f"Nome: {nome}")
print(f"Idade: {idade}")
```

Saída

```
Nome: Pedro
Idade: 25
```
Também podemos misturar texto e cálculos.

```
nota1 = 8
nota2 = 7

print(f"Soma = {nota1 + nota2}")
```
Saída

```
Soma = 15
```

Outro exemplo:
```
produto = "Notebook"
preco = 3500

print(f"O produto {produto} custa R$ {preco}.")
```

### 7. Utilizando format()

Antes das f-strings, era comum utilizar o método format().

Ele ainda é muito encontrado em códigos antigos e continua funcionando normalmente.
```
nome = "Lucas"
idade = 22

print("Nome: {} Idade: {}".format(nome, idade))
```

Saída
```
Nome: Lucas Idade: 22
```

Também podemos usar índices.

```
nome = "Lucas"
idade = 22

print("Nome: {0} Idade: {1}".format(nome, idade))
```

### Comparando os três métodos

- Método tradicional
```
nome = "João"
print("Olá", nome)
```

- Usando f-string
```
nome = "João"
print(f"Olá {nome}")
```

- Usando format()
```
nome = "João"
print("Olá {}".format(nome))
```

Todos produzem o mesmo resultado.
```
Olá João
```
Hoje em dia, a f-string é a forma mais utilizada por ser mais simples e fácil de ler.

### 8. Formatando números decimais

Muitas vezes um cálculo produz várias casas decimais.

Exemplo:
```
valor = 10 / 3
print(valor)
```

Saída

3.3333333333333335

Podemos controlar a quantidade de casas decimais.

- Usando f-string
valor = 10 / 3

print(f"{valor:.2f}")

Saída
```
3.33
```

O significado é:
```
: → inicia a formatação.
.2 → duas casas decimais.
f → número do tipo ponto flutuante (float).
```

Outro exemplo:
```
preco = 123.45678
print(f"Preço: R$ {preco:.2f}")
```

Saída
```
Preço: R$ 123.46
```

- Usando format()

Também podemos formatar números utilizando format().
```
valor = 10 / 3
print("{:.2f}".format(valor))
```
Saída
```
3.33
```
Outro exemplo:
```
preco = 2599.9

print("Preço: R$ {:.2f}".format(preco))
```
Saída
```
Preço: R$ 2599.90
```
Exemplo completo
```
nome = "Maria"
idade = 21
altura = 1.685

print("=== Cadastro ===")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} metros")
```
Saída
```
=== Cadastro ===
Nome: Maria
Idade: 21 anos
Altura: 1.69 metros
```

Resumo


| Método                 | Exemplo                          | Quando utilizar                                        |
| ---------------------- | -------------------------------- | ------------------------------------------------------ |
| `print()`              | `print(nome)`                    | Exibir uma variável ou texto simples.                  |
| `print()` com vírgulas | `print("Nome:", nome)`           | Exibir várias informações de forma simples.            |
| Concatenação (`+`)     | `"Olá " + nome`                  | Juntar textos. Requer conversão de números para `str`. |
| **f-string**           | `print(f"Nome: {nome}")`         | Forma mais moderna, recomendada e fácil de ler.        |
| `format()`             | `print("Nome: {}".format(nome))` | Muito utilizado em códigos mais antigos.               |
| Formatação decimal     | `f"{valor:.2f}"`                 | Limitar a quantidade de casas decimais.                |

Recomendação: Em novos programas, prefira utilizar f-strings, pois elas tornam o código mais limpo, legível e facilitam a inclusão de variáveis e expressões diretamente no texto.
