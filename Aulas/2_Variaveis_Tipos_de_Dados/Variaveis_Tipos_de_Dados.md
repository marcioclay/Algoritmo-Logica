Unidade III — Variáveis, Constantes e Tipos de Dados

Os programas precisam trabalhar com informações.

Um sistema pode precisar armazenar:

Nome de um usuário;
Idade;
Preço de um produto;
Quantidade em estoque;
Resultado de um cálculo;
Situação de um aluno;
Informação sobre um equipamento conectado à rede.

Para trabalhar com essas informações, utilizamos variáveis, constantes e tipos de dados.

1. Conceito de Variável

Uma variável é um espaço utilizado pelo programa para armazenar um valor.

Podemos imaginar uma variável como uma caixa identificada por um nome.

┌─────────────┐
│    idade    │
│      25     │
└─────────────┘

Em Python:

idade = 25

Nesse exemplo:

idade é o nome da variável;
25 é o valor armazenado;
= é o operador de atribuição.

Podemos interpretar:

idade recebe 25
Exemplo
nome = "Maria"
idade = 20
altura = 1.65

O programa possui três variáveis:

Variável	Valor
nome	"Maria"
idade	20
altura	1.65

Podemos utilizar essas variáveis:

nome = "Maria"
idade = 20

print(nome)
print(idade)

Saída:

Maria
20
2. Declaração e Atribuição
2.1 Declaração

Em algumas linguagens de programação, é necessário declarar uma variável antes de utilizá-la, informando seu tipo.

Por exemplo, em algumas linguagens:

inteiro idade;
real altura;

Em Python, não é necessário declarar previamente o tipo da variável.

A variável é criada no momento em que recebe um valor:

idade = 20

Nesse momento, Python cria a variável idade e associa a ela o valor 20.

2.2 Atribuição

A atribuição consiste em associar um valor a uma variável.

idade = 25

Podemos alterar o valor posteriormente:

idade = 25

idade = 26

print(idade)

Saída:

26

O valor anterior foi substituído.

2.3 Variável recebendo o resultado de uma operação

Uma variável também pode receber o resultado de uma expressão:

numero1 = 10
numero2 = 5

soma = numero1 + numero2

print(soma)

Resultado:

15

Nesse caso:

numero1 + numero2

é calculado primeiro.

Depois, o resultado é armazenado em:

soma
3. Variáveis Podem Ter Seus Valores Alterados

Uma característica importante das variáveis é que seus valores podem mudar durante a execução do programa.

saldo = 100

print(saldo)

saldo = 150

print(saldo)

Saída:

100
150

Podemos representar:

saldo = 100
     ↓
saldo = 150

O valor da variável foi atualizado.

4. Constantes

Uma constante representa um valor que, conceitualmente, não deve ser alterado durante a execução do programa.

Exemplos:

Valor de π;
Limite máximo;
Taxa de imposto;
Velocidade da luz;
Nome de uma configuração.

Em Python, não existe uma palavra-chave específica que impeça completamente a alteração de uma constante.

Por convenção, utilizamos nomes escritos em letras maiúsculas.

PI = 3.14159
LIMITE_IDADE = 18

Exemplo:

LIMITE_IDADE = 18

idade = 20

if idade >= LIMITE_IDADE:
    print("Maior de idade")

A utilização de constantes torna o código mais fácil de compreender.

Compare:

if idade >= 18:
    print("Maior de idade")

com:

LIMITE_IDADE = 18

if idade >= LIMITE_IDADE:
    print("Maior de idade")

A segunda versão deixa mais claro o significado do valor 18.

5. Tipos de Dados

Um tipo de dado define a natureza da informação armazenada.

Por exemplo:

idade = 25

representa um número inteiro.

Já:

nome = "Carlos"

representa um texto.

Os principais tipos de dados estudados nesta unidade são:

Inteiro;
Real ou ponto flutuante;
String;
Caractere;
Booleano.
6. Tipo Inteiro — int

O tipo int representa números inteiros.

Exemplos:

idade = 30
quantidade = 10
temperatura = -5

Os números inteiros podem ser:

Positivos;
Negativos;
Zero.
numero1 = 10
numero2 = -10
numero3 = 0

Podemos realizar operações:

a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao_inteira = a // b
7. Tipo Real ou Ponto Flutuante — float

O tipo float representa números que possuem casas decimais.

Em Python, utilizamos o ponto para separar a parte inteira da parte decimal:

altura = 1.75
preco = 29.90
temperatura = 36.5

Em Python, o separador decimal é o ponto (.), e não a vírgula.

Correto:

preco = 29.90

Incorreto:

preco = 29,90

O segundo exemplo é interpretado pelo Python de outra maneira.

Exemplo
nota1 = 7.5
nota2 = 8.0

media = (nota1 + nota2) / 2

print(media)

Saída:

7.75
8. String — str

Uma string é uma sequência de caracteres utilizada para representar textos.

Em Python, strings podem ser escritas utilizando:

"texto"

ou:

'texto'

Exemplos:

nome = "Marcos"
cidade = "Vitória"
mensagem = "Olá, mundo!"
Strings podem conter números
codigo = "12345"

Nesse caso, "12345" é um texto, não um número.

Portanto:

numero = 12345

é diferente de:

texto = "12345"

A primeira variável possui um número inteiro.

A segunda possui uma string.

Concatenação

Podemos unir strings utilizando o operador +.

nome = "Ana"
sobrenome = "Silva"

nome_completo = nome + " " + sobrenome

print(nome_completo)

Saída:

Ana Silva
9. Caractere

Um caractere representa uma única unidade de texto, como:

A
B
7
@
#

Em algumas linguagens, existe um tipo específico chamado char.

Em Python, não existe um tipo char separado.

Um único caractere é representado como uma string com apenas um elemento:

letra = "A"

Tecnicamente:

type(letra)

retorna:

str

Portanto:

caractere = "A"

é uma str contendo apenas um caractere.

10. Booleano — bool

O tipo booleano representa valores lógicos.

Existem apenas dois valores:

True
False

Em português:

Verdadeiro
Falso

Exemplo:

usuario_logado = True
servidor_disponivel = False

Podemos utilizar valores booleanos em condições:

usuario_logado = True

if usuario_logado:
    print("Usuário conectado")
Booleanos e comparações

Uma comparação produz um resultado booleano:

idade = 20

resultado = idade >= 18

print(resultado)

Saída:

True

Outro exemplo:

idade = 15

resultado = idade >= 18

print(resultado)

Saída:

False
11. Identificando o Tipo de uma Variável

Podemos utilizar a função type() para descobrir o tipo de um valor.

idade = 20
altura = 1.75
nome = "Ana"
ativo = True

print(type(idade))
print(type(altura))
print(type(nome))
print(type(ativo))

Saída aproximada:

<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
12. Tabela dos Principais Tipos
Tipo	Python	Exemplo
Inteiro	int	20
Real	float	1.75
Texto	str	"Python"
Caractere	str	"A"
Booleano	bool	True
13. Regras para Nomenclatura de Identificadores

Um identificador é o nome utilizado para identificar elementos do programa, como:

Variáveis;
Funções;
Classes;
Constantes.

Exemplo:

idade = 20

Nesse caso:

idade

é um identificador.

Regras básicas
Regra 1 — Pode utilizar letras
nome = "Ana"
Regra 2 — Pode utilizar números

Mas o identificador não pode começar com um número.

Correto:

nota1 = 8

Incorreto:

1nota = 8
Regra 3 — Pode utilizar sublinhado
nome_completo = "Ana Silva"
Regra 4 — Não utilizar espaços

Incorreto:

nome completo = "Ana Silva"

Correto:

nome_completo = "Ana Silva"
Regra 5 — Não utilizar palavras reservadas

Python possui palavras reservadas para sua própria linguagem.

Exemplos:

if
else
for
while
class
def
return
True
False

Não devemos utilizar:

if = 10
Regra 6 — Python diferencia maiúsculas e minúsculas

Os identificadores abaixo são diferentes:

nome = "Ana"
Nome = "Carlos"
NOME = "João"

Python considera:

nome
Nome
NOME

como três identificadores diferentes.

14. Convenção para Nomes

Embora alguns nomes sejam permitidos, é importante utilizar nomes claros e significativos.

Evite:

x = 25
y = 1.75
z = "Ana"

Prefira:

idade = 25
altura = 1.75
nome = "Ana"

Um bom nome facilita a leitura do programa.

Convenção snake_case

Em Python, é comum utilizar o padrão snake_case para variáveis e funções:

nome_completo = "Ana Silva"
data_nascimento = "10/05/2000"
valor_total = 150.50

Para constantes, normalmente utilizamos letras maiúsculas:

LIMITE_MAXIMO = 100
TAXA_DESCONTO = 0.10
15. Entrada de Dados

A entrada de dados permite que o usuário forneça informações ao programa.

Em Python, utilizamos a função:

input()

Exemplo:

nome = input("Digite seu nome: ")

print("Olá,", nome)

Se o usuário digitar:

Carlos

o programa exibirá:

Olá, Carlos
16. Importante: input() Retorna String

Por padrão, tudo que é recebido pela função input() é tratado como str.

Observe:

idade = input("Digite sua idade: ")

print(type(idade))

Mesmo que o usuário digite:

25

o Python recebe:

"25"

Ou seja, uma string.

17. Conversão de Tipos

A conversão de tipos consiste em transformar um valor de um tipo para outro.

As funções mais utilizadas são:

int()
float()
str()
bool()
Converter para inteiro — int()
idade = int(input("Digite sua idade: "))

print(type(idade))

Se o usuário digitar:

25

o valor será convertido para:

25

do tipo:

int
Converter para float
preco = float(input("Digite o preço: "))

print(type(preco))

Se o usuário digitar:

29.90

o valor será convertido para:

29.90

do tipo:

float
Converter para string — str()
idade = 25

texto = str(idade)

print(type(texto))

O número:

25

é convertido para o texto:

"25"
18. Problema de Tipos Diferentes

Observe:

idade = input("Digite sua idade: ")

print(idade + 1)

Se o usuário digitar:

20

ocorrerá um erro.

Isso acontece porque:

"20" + 1

tenta combinar:

str + int

O Python não realiza automaticamente essa operação.

A solução é converter o valor:

idade = int(input("Digite sua idade: "))

print(idade + 1)

Agora:

20 + 1

Resultado:

21
19. Exemplo Completo

Vamos criar um programa que receba dados de um produto.

nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

print("Produto:", nome_produto)
print("Preço:", preco)
print("Quantidade:", quantidade)
print("Valor total:", total)
Tipos utilizados
Variável	Tipo
nome_produto	str
preco	float
quantidade	int
total	float
20. Exemplo com Booleano
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

maior_de_idade = idade >= 18

print("Nome:", nome)
print("Maior de idade:", maior_de_idade)

Se o usuário informar:

Nome: Ana
Idade: 20

o resultado será:

Nome: Ana
Maior de idade: True

A variável:

maior_de_idade

recebe o resultado de uma comparação.

21. Resumo

Nesta unidade, aprendemos que:

Uma variável armazena um valor que pode ser alterado;
A atribuição associa um valor a uma variável;
Uma constante representa um valor que, conceitualmente, não deve ser alterado;
Python possui diferentes tipos de dados;
int representa números inteiros;
float representa números com casas decimais;
str representa textos;
Um caractere individual também é representado como str em Python;
bool representa True ou False;
Identificadores devem seguir regras de nomenclatura;
input() recebe dados do usuário;
print() exibe dados;
input() retorna valores do tipo str;
Funções como int() e float() permitem converter tipos de dados.
Atividades Práticas
Atividade 1 — Dados pessoais

Crie um programa que receba:

Nome;
Idade;
Altura.

Depois, exiba todas as informações.

Utilize os tipos adequados.

Atividade 2 — Produto

Crie um programa que receba:

Nome do produto;
Preço;
Quantidade.

Calcule e exiba o valor total.

Atividade 3 — Conversão de tipos

Analise o código:

numero = input("Digite um número: ")

resultado = numero + 10

print(resultado)
Qual problema existe no código?
Qual é o tipo de numero?
Como corrigir o programa?
Atividade 4 — Identificadores

Identifique quais nomes são válidos em Python:

idade
nome_completo
2numero
valor-total
nome completo
nota1
class
NOME

Explique por que alguns nomes são inválidos.

Atividade 5 — Booleano

Crie um programa que:

Receba a idade de uma pessoa;
Armazene em uma variável booleana se ela é maior de idade;
Exiba o resultado.

Exemplo:

idade = 20

maior_de_idade = idade >= 18

print(maior_de_idade)

Resultado:

True
