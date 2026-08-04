## Estruturas Condicionais em Python (if)

Durante a execução de um programa, nem sempre todas as instruções devem ser executadas. Em muitas situações, é necessário que o computador tome decisões com base em uma condição.

Imagine as seguintes situações:

- Um aluno só será aprovado se sua nota for maior ou igual a 7.
- Um caixa eletrônico só libera o saque se houver saldo suficiente.
- Um sistema só permite o acesso se o usuário informar a senha correta.

Em todos esses exemplos, existe uma condição que deve ser analisada antes de executar uma ação.

Em Python, utilizamos a estrutura if para realizar essa tomada de decisão.

As estruturas condicionais podem ser classificadas em:

- If simples
- If composto
- If aninhado

### 1. If Simples

O if simples é utilizado quando desejamos executar uma ação somente se uma condição for verdadeira.

Caso a condição seja falsa, o programa simplesmente continua sua execução.

Sintaxe
```
if condição:
    instruções
```
Observe que:

- A condição termina com dois pontos (:).
- O código que pertence ao if deve estar indentado (recuado).

Exemplo 1
```
idade = 20

if idade >= 18:
    print("Você é maior de idade.")
```

Saída
```
Você é maior de idade.
Exemplo 2
nota = 8

if nota >= 7:
    print("Aluno aprovado!")
```

Se a nota fosse 5, nenhuma mensagem seria exibida.

Exemplo com input()
```
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Entrada permitida.")
```

### 2. If Composto (if e else)

Em muitas situações, desejamos executar uma ação quando a condição for verdadeira e outra ação quando ela for falsa.

Para isso utilizamos o else.

Sintaxe

```
if condição:
    instruções
else:
    instruções
```

Exemplo 1

```
idade = 16

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

Saída

```
Menor de idade.
Exemplo 2
nota = 6

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

Exemplo com input()

```
senha = input("Digite a senha: ")
if senha == "python123":
    print("Acesso permitido.")
else:
    print("Senha incorreta.")
```

### 3. If Aninhado

O if aninhado ocorre quando um if é colocado dentro de outro if.

Ele é utilizado quando uma decisão depende de outra decisão.

Sintaxe

```
if condição1:
    if condição2:
        instruções
```

Exemplo 1

Uma pessoa só poderá comprar bebida se:

- for maior de idade;
-apresentar documento.
- idade = 20
- documento = True
```
if idade >= 18:
    if documento:
        print("Venda autorizada.")
```
Saída

```
Venda autorizada.
````
Exemplo 2
```
idade = 17
documento = True

if idade >= 18:
    if documento:
        print("Venda autorizada.")
```


Nesse caso nenhuma mensagem será exibida, pois a primeira condição já é falsa.

If Aninhado com else

Também podemos utilizar o else dentro das estruturas.
```
idade = 20
documento = False

if idade >= 18:
    if documento:
        print("Venda autorizada.")
    else:
        print("Documento obrigatório.")
else:
    print("Venda proibida para menores.")
```

Saída
```
Documento obrigatório.
```

#### Exemplo Prático

Um aluno será aprovado se:

- Nota maior ou igual a 7;
- Frequência maior ou igual a 75%.
```
nota = float(input("Digite a nota: "))
frequencia = int(input("Digite a frequência (%): "))

if nota >= 7:
    if frequencia >= 75:
        print("Aluno aprovado.")
    else:
        print("Reprovado por frequência.")
else:
    print("Reprovado por nota.")
```

#### Comparando as estruturas

- If Simples

Executa uma ação apenas quando a condição é verdadeira.
```
saldo = 100

if saldo > 0:
    print("Você possui saldo.")
```
- If Composto

Executa uma ação quando a condição é verdadeira e outra quando é falsa.
```
saldo = -20

if saldo >= 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo.")
```

- If Aninhado

Uma decisão depende de outra.
```
usuario = "admin"
senha = "1234"

if usuario == "admin":
    if senha == "1234":
        print("Login realizado.")
    else:
        print("Senha incorreta.")
else:
    print("Usuário inexistente.")
```

#### Erros comuns

Esquecer os dois pontos
- Errado
```
if idade >= 18
    print("Maior de idade")
```

- Correto
```
if idade >= 18:
    print("Maior de idade")
Esquecer a indentação
```

Errado
``` 
if idade >= 18:
print("Maior de idade")
```
Correto
```
if idade >= 18:
    print("Maior de idade")
```
A indentação é obrigatória em Python e define quais instruções pertencem ao bloco do if.

| Estrutura     | Quando utilizar                                     | Exemplo                                                    |
| ------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| `if`          | Quando existe apenas uma condição a ser verificada. | Verificar se um aluno foi aprovado.                        |
| `if...else`   | Quando existem dois caminhos possíveis.             | Aprovado ou reprovado.                                     |
| `if` aninhado | Quando uma decisão depende de outra.                | Verificar idade e documento antes de autorizar uma compra. |
