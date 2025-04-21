# Introdução à Declaração de Variáveis e Tipos de Dados em Python

No Python, **variáveis** são como "caixinhas" que armazenam valores. Cada valor em Python tem um **tipo de dado**, que indica a natureza ou a categoria do valor. Vamos explorar como declarar variáveis, entender os principais tipos de dados e trabalhar com eles, com exemplos claros para iniciantes.

---

## 1. Declaração de Variáveis

Declarar uma variável em Python é simples: basta dar um nome à variável e atribuir um valor usando o símbolo de **igual** (`=`).

Exemplo:
```
nome = "Ana"          # Variável de tipo texto (string)
idade = 25            # Variável de tipo número inteiro (int)
altura = 1.68         # Variável de tipo número decimal (float)
```
Dicas importantes:

O nome da variável deve começar com uma letra ou _ (não pode começar com números ou caracteres especiais).

Nomes de variáveis devem ser claros e descritivos, como idade_usuario em vez de apenas x.

Use boas práticas, como snake_case (letras minúsculas e separadas por _).

## 2. Principais Tipos de Dados em Python
Python tem diversos tipos de dados. Aqui estão os mais usados:

a) String (Texto)
Armazena textos como palavras, frases ou caracteres.

Exemplo:

```
cidade = "São Paulo"
print(cidade)  # Saída: São Paulo
```
Strings devem estar entre aspas simples (') ou duplas (").

Você pode acessar caracteres individuais da string:

```
texto = "Python"
print(texto[0])  # Saída: P (primeiro caractere)
```
b) Inteiro (Int)
Representa números inteiros, como 1, 0, -45.

Exemplo:

```
idade = 30
numero_inteiro = -15
soma = idade + numero_inteiro
print(soma)  # Saída: 15
```
c) Float (Número Decimal)
Armazena números com casas decimais.

Exemplo:

```
peso = 68.5
altura = 1.70
imc = peso / (altura ** 2)  # Fórmula de cálculo do IMC
print(imc)  # Saída: 23.72
```
d) Booleano (Bool)
Pode ter apenas dois valores: True (verdadeiro) ou False (falso).

Exemplo:

```
chovendo = True
calor = False
print(chovendo and calor)  # Saída: False (porque uma das condições é falsa)
```
3. Conversão de Tipos (Type Casting)
Às vezes, é necessário converter o tipo de uma variável para realizar certas operações.

Exemplos de conversão:

```
# Inteiro para String
idade = 25
idade_texto = str(idade)
print("Idade: " + idade_texto)  # Saída: Idade: 25

# String para Float
altura = "1.75"
altura_numero = float(altura)
print(altura_numero + 0.1)  # Saída: 1.85

# Float para Inteiro
valor = 5.9
valor_inteiro = int(valor)  # Perde a parte decimal
print(valor_inteiro)  # Saída: 5
```
4. Exemplos Práticos
Exemplo 1: Calculando a Soma de Dois Números
```
numero1 = 10
numero2 = 20
soma = numero1 + numero2
print("A soma é:", soma)  # Saída: A soma é: 30
```
Exemplo 2: Verificando a Idade do Usuário
```
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
Exemplo 3: Trabalhando com Strings
```
nome = "João"
print("Olá, " + nome + "!")  # Saída: Olá, João!
print(f"Seu nome tem {len(nome)} letras.")  # Saída: Seu nome tem 4 letras.
```
5. Boa Prática: Usando Função type()
Você pode usar a função type() para verificar o tipo de uma variável:

```
variavel = 10
print(type(variavel))  # Saída: <class 'int'>
```
Conclusão
Agora que você conhece o básico sobre variáveis e tipos de dados, pode começar a experimentar no Python! Pratique criando variáveis, usando diferentes tipos de dados e convertendo entre eles. E lembre-se: programar é como aprender um novo idioma. Quanto mais você pratica, melhor você fica!
