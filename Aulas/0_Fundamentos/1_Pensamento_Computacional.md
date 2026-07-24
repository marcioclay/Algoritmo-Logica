## Fundamentos do Pensamento Computacional e da Programação

### 1. Pensamento Computacional

O pensamento computacional é uma forma estruturada de analisar problemas e desenvolver soluções que possam ser executadas por pessoas ou computadores.

Apesar do nome, pensamento computacional não significa pensar como um computador. Significa utilizar estratégias organizadas para resolver problemas de maneira lógica, eficiente e sistemática.

O pensamento computacional é baseado em algumas habilidades fundamentais:
```
Decomposição de problemas;
Reconhecimento de padrões;
Abstração;
Elaboração de algoritmos.
```

Essas habilidades são utilizadas tanto na programação quanto em situações do cotidiano.

Exemplo

Imagine o seguinte problema:

```
Desenvolver um programa em Python para calcular a média de um aluno e informar se ele foi aprovado.

Antes de escrever o código, é necessário pensar sobre o problema:

Quais dados serão necessários?
Como a média será calculada?
Qual será a regra para aprovação?
Qual resultado deverá ser exibido?
```
Esse processo de análise faz parte do pensamento computacional.

### 2. Decomposição de Problemas

A decomposição consiste em dividir um problema complexo em partes menores e mais fáceis de compreender e resolver.

Um problema grande pode parecer difícil quando analisado como um todo. Entretanto, quando dividido em etapas menores, sua solução se torna mais simples.

Exemplo
```
Considere o problema:

Criar um sistema de vendas para uma loja.

Esse problema pode ser dividido em várias partes:

Sistema de vendas
│
├── Cadastrar produtos
├── Consultar produtos
├── Registrar clientes
├── Registrar vendas
├── Calcular total da compra
├── Aplicar descontos
└── Emitir relatório
```

Cada parte pode ser analisada e desenvolvida separadamente.

Outro exemplo

Problema:
```
Criar um programa para calcular a média de um aluno e informar sua situação.

Podemos decompor o problema em:

1. Ler a primeira nota.
2. Ler a segunda nota.
3. Calcular a média.
4. Verificar se a média é suficiente para aprovação.
5. Exibir o resultado.
```

Em Python:

```
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
```

O programa foi construído a partir de pequenas etapas.

A decomposição transforma um problema grande em vários problemas menores.

### 3. Abstração

A abstração consiste em concentrar a atenção nas informações mais importantes de um problema e ignorar detalhes que não são necessários para sua solução.

Na programação, nem todas as informações do mundo real precisam ser representadas no programa.

Exemplo

Imagine um sistema para calcular a média de um aluno.

Na vida real, um aluno possui diversas informações:
```
Nome;
CPF;
Endereço;
Data de nascimento;
Telefone;
Curso;
Turma;
Notas;
Frequência.
```
Entretanto, se o objetivo do programa é apenas calcular a média, talvez sejam necessárias somente as notas:
```
Aluno
│
└── Notas
    ├── Nota 1
    └── Nota 2
```
```
Em Python:

nota1 = 7
nota2 = 8

media = (nota1 + nota2) / 2

print(media)
```
Para calcular a média, não é necessário conhecer o endereço ou o telefone do aluno.

A abstração permite concentrar-se apenas nas informações relevantes para o problema.

Abstrair é simplificar um problema, mantendo apenas os elementos importantes para sua solução.

### 4. Reconhecimento de Padrões

O reconhecimento de padrões consiste em identificar características ou comportamentos que se repetem em diferentes problemas.

Quando identificamos um padrão, podemos reutilizar uma solução ou uma estratégia.

Exemplo

Observe os seguintes problemas:
```
Problema 1

Calcular a média de duas notas:

media = (nota1 + nota2) / 2
```
Problema 2
```
Calcular a média de três notas:

media = (nota1 + nota2 + nota3) / 3
```
Problema 3

```
Calcular a média de quatro notas:

media = (nota1 + nota2 + nota3 + nota4) / 4

Existe um padrão:

Média = soma dos valores / quantidade de valores
```

Esse padrão pode ser utilizado em vários problemas.

Outro exemplo é o processamento de vários valores:
```
for numero in range(1, 6):
    print(numero)
```
```
O programa apresenta:

1
2
3
4
5
```
O padrão é:

Repetir uma operação para vários valores.

O reconhecimento de padrões ajuda o programador a:

- Evitar a repetição desnecessária de soluções;
- Identificar estruturas semelhantes;
- Reutilizar ideias;
- Desenvolver soluções mais rapidamente.

### 5. Entrada, Processamento e Saída

Uma grande quantidade de programas pode ser compreendida por meio do modelo:
```
ENTRADA → PROCESSAMENTO → SAÍDA
Entrada

A entrada corresponde aos dados fornecidos ao programa.

Em Python, normalmente utilizamos a função input() para receber dados do usuário.

nome = input("Digite seu nome: ")
```

Nesse exemplo, o usuário fornece um nome.

Outro exemplo:
```
idade = int(input("Digite sua idade: "))

A função input() recebe o valor como texto. Por isso, utilizamos int() para convertê-lo para um número inteiro.
```
Processamento

O processamento corresponde às operações realizadas pelo programa sobre os dados recebidos.
```
Exemplo:

nota1 = 7
nota2 = 8

media = (nota1 + nota2) / 2
```

Nesse caso, o processamento é:
```
Somar as notas
Dividir o resultado por 2
Saída
```
A saída é o resultado apresentado pelo programa.

Em Python, utilizamos a função print():
```
print(media)
Exemplo Completo
# Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
```

# Processamento
media = (nota1 + nota2) / 2

# Saída
print("Média:", media)

A estrutura pode ser representada assim:

┌──────────────┐
│    ENTRADA   │
│   nota1      │
│   nota2      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ PROCESSAMENTO │
│ calcular     │
│ média        │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     SAÍDA    │
│ exibir média │
└──────────────┘

### 6. Conceito de Linguagem de Programação

Uma linguagem de programação é um conjunto de regras e comandos utilizados para escrever programas.

Os computadores trabalham internamente com instruções representadas por sinais elétricos e códigos binários.

Para facilitar o desenvolvimento de programas, foram criadas linguagens que permitem aos seres humanos escrever instruções de maneira mais próxima da linguagem lógica e matemática.

Algumas linguagens de programação são:
```
Python;
Java;
C;
C++;
JavaScript;
C#;
Go;
Rust.
```

Neste curso, utilizaremos a linguagem Python.

Exemplo em Python
```
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

Nesse programa:
```
input() → recebe dados
print() → exibe dados
```
Uma linguagem de programação possui regras próprias, chamadas de sintaxe.

Por exemplo, em Python:
```
if idade >= 18:
    print("Maior de idade")
```
A indentação é importante para indicar que o comando print() pertence à estrutura if.

### 7. Compiladores e Interpretadores

Para que um computador execute um programa, o código escrito pelo programador precisa ser processado.

Existem duas formas tradicionais de realizar esse processamento:

Compilação;
Interpretação.

### 7.1 Compiladores

Um compilador traduz o código-fonte para uma forma que possa ser executada pelo computador.

O processo pode ser representado assim:

Código-fonte
     │
     ▼
┌────────────┐
│ Compilador │
└──────┬─────┘
       │
       ▼
Programa executável

Exemplo de linguagens que tradicionalmente utilizam compilação:

C;
C++;
Rust;
Go.

### 7.2 Interpretadores

Um interpretador analisa e executa o código durante sua execução.

Representação:
```
Código-fonte
     │
     ▼
┌───────────────┐
│ Interpretador │
└──────┬────────┘
       │
       ▼
Execução
```
O Python é tradicionalmente utilizado como uma linguagem interpretada.

Por exemplo:
```
print("Olá, mundo!")
```
Quando esse programa é executado, o interpretador Python analisa o código e executa a instrução.

Observação

Na prática, a implementação mais comum do Python, chamada CPython, realiza etapas intermediárias, como a geração de bytecode. Portanto, a distinção entre linguagens "compiladas" e "interpretadas" pode ser mais complexa do que a classificação tradicional apresentada neste momento.

Para o nível introdutório, podemos compreender:

O compilador traduz o programa antes da execução, enquanto o interpretador participa do processo de execução do código.

### 8. Erros em Programas

Durante o desenvolvimento de um programa, é comum ocorrerem erros.

Os principais tipos de erros estudados inicialmente são:

Erros de sintaxe;
Erros de execução;
Erros de lógica.

### 8.1 Erros de Sintaxe

A sintaxe corresponde às regras de escrita da linguagem de programação.

Um erro de sintaxe ocorre quando o código não segue essas regras.

Exemplo
```
if idade >= 18
    print("Maior de idade")
```
Esse código está incorreto porque falta : após a condição.

Forma correta:
```
if idade >= 18:
    print("Maior de idade")
```
Outro exemplo:
```
print("Olá"
```
Nesse caso, falta fechar o parêntese.

Forma correta:
```
print("Olá")
```
O interpretador Python normalmente apresenta uma mensagem indicando que existe um erro no código.

### 8.2 Erros de Execução

Um erro de execução ocorre quando o programa possui uma estrutura sintaticamente válida, mas ocorre um problema durante sua execução.

Exemplo:
```
numero = int(input("Digite um número: "))

resultado = 10 / numero

print(resultado)
```
Se o usuário digitar:

0

ocorrerá um erro, pois não é possível dividir um número por zero.

Outro exemplo:
```
idade = int(input("Digite sua idade: "))
```
Se o usuário digitar:

vinte

o programa não conseguirá converter o texto "vinte" para um número inteiro.

### 8.3 Erros de Lógica

Um erro de lógica ocorre quando o programa executa sem apresentar erro de sintaxe ou de execução, mas produz um resultado incorreto.

Exemplo:
```
nota1 = 8
nota2 = 6

media = nota1 + nota2 / 2

print(media)
```
O programa pode ser executado normalmente.

Entretanto, a expressão está incorreta.

O cálculo correto da média é:
```
media = (nota1 + nota2) / 2
```
O primeiro código calcula:
```
8 + (6 / 2) = 11

O resultado correto seria:

(8 + 6) / 2 = 7
```
Esse é um erro de lógica.

### 9. Comparação entre os Tipos de Erro

Tipo de erro	Característica	Exemplo
Sintaxe	O código não segue as regras da linguagem	Falta de :
Execução	Ocorre um problema durante a execução	Divisão por zero
Lógica	O programa executa, mas produz resultado incorreto	Fórmula errada

### 10. Processo de Desenvolvimento de uma Solução

A resolução de um problema utilizando programação pode seguir o seguinte processo:

┌────────────────────┐
│ 1. Compreender     │
│    o problema      │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 2. Decompor        │
│    o problema      │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 3. Identificar     │
│    padrões         │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 4. Abstrair        │
│    informações     │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 5. Criar algoritmo │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 6. Escrever código │
│    em Python       │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 7. Testar          │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 8. Corrigir erros  │
└────────────────────┘

Esse processo demonstra que programar não significa apenas escrever código.

Antes de criar um programa, é necessário:

Compreender o problema;
- Dividir o problema em partes;
- Identificar informações importantes;
- Observar padrões;
- Planejar uma solução;
- Implementar a solução em Python;
- Testar o programa;
- Corrigir possíveis erros.

Atividades de Fixação

Atividade 1 — Decomposição

Considere o problema:
```
Criar um programa para calcular o valor total de uma compra.
Divida o problema em pelo menos cinco etapas.
```
Atividade 2 — Entrada, Processamento e Saída

Para cada problema abaixo, identifique:

Entrada;
Processamento;
Saída.
a) Calcular a área de um retângulo.
b) Calcular a média de três notas.
c) Converter uma temperatura de Celsius para Fahrenheit.
d) Calcular o valor total de uma compra.
Atividade 3 — Identificação de Erros

Identifique o tipo de erro presente em cada situação:

a)
if idade >= 18
    print("Maior de idade")
b)
numero = 10
resultado = numero / 0
c)
nota1 = 8
nota2 = 6

media = nota1 + nota2 / 2
Desafio

Desenvolva um programa em Python que:

Receba o nome de um aluno;
Receba duas notas;
Calcule a média;
Exiba o nome do aluno;
Exiba a média calculada.

Antes de escrever o código, identifique:

Entrada:
- ?

Processamento:
- ?

Saída:
- ?

Depois, implemente a solução em Python.
