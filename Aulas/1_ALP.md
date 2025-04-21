# Explicação sobre o Uso do `print` e `input` em Python

O Python é uma linguagem extremamente intuitiva, especialmente para iniciantes. Dois comandos essenciais para interação com o usuário são o `print()` e o `input()`. Ambos são ferramentas fundamentais para exibir informações e coletar dados em programas. Vamos entender como usá-los com explicações e exemplos práticos.

---

## 1. O Comando `print()`

O comando `print()` é usado para exibir informações na tela. Ele pode mostrar textos, números e até resultados de cálculos ou valores de variáveis.

### **Sintaxe Básica**
```python
print("Mensagem para exibir")
```
Exemplos
Exibindo uma mensagem simples:

```
print("Olá, mundo!")
# Saída: Olá, mundo!
```
Exibindo valores de variáveis:

```
nome = "Ana"
idade = 25
print("Nome:", nome)
print("Idade:", idade)
# Saída:
# Nome: Ana
# Idade: 25
```
Formatando texto com f-strings:

```
nome = "Carlos"
idade = 30
print(f"Olá, {nome}! Você tem {idade} anos.")
```
# Saída: Olá, Carlos! Você tem 30 anos.
2. O Comando input()
O comando input() é usado para solicitar que o usuário digite informações. Os dados inseridos pelo usuário são sempre retornados como uma string (texto), mesmo que sejam números.

Sintaxe Básica
```
variavel = input("Mensagem para o usuário: ")
```
Exemplos
Solicitar o nome do usuário:

```
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```
# Se o usuário digitar "Ana", a saída será: Olá, Ana!
Solicitar números e convertê-los: Como o input() retorna valores em formato de texto, é necessário converter para números caso você queira realizar cálculos.

```
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
print(f"A soma é: {soma}")
```
# Se o usuário digitar 10 e 20, a saída será: A soma é: 30
3. Diferenças entre print() e input()
   ## Diferenças entre `print()` e `input()`

| Comando    | Objetivo                                   | Exemplo                                                        |
|------------|-------------------------------------------|----------------------------------------------------------------|
| `print()`  | Exibir informações na tela                | `print("Bem-vindo!")`                                          |
| `input()`  | Solicitar dados ao usuário                | `nome = input("Qual é o seu nome? ")`                         |
| Conversões | Necessárias para números no `input()`     | `idade = int(input("Digite sua idade: "))`                    |


4. Uso Combinado de print() e input()
Os comandos print() e input() podem ser combinados para criar programas interativos. Um exemplo prático:

```
print("Bem-vindo ao programa de soma!")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"O resultado da soma é: {soma}")
Saída esperada
Bem-vindo ao programa de soma!
Digite o primeiro número: 15.5
Digite o segundo número: 20
O resultado da soma é: 35.5
```
Conclusão
Os comandos print() e input() são essenciais para criar programas que interagem com o usuário. Enquanto o print() é usado para exibir mensagens, o input() coleta informações, permitindo que seus programas se tornem mais dinâmicos. Experimente utilizá-los com diferentes formatos e aplicações para se tornar cada vez mais familiar com eles!
