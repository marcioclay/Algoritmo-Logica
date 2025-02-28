## O que são Strings?

Em Python, strings são sequências de caracteres, como letras, números e símbolos. Podemos criar strings colocando o texto entre aspas simples (' ') ou duplas (" ").

```
nome = "João da Silva"
mensagem = 'Olá, mundo!'
```

## Ferramentas Essenciais para Manipular Strings


Python nos oferece diversas ferramentas para trabalhar com strings. Vamos conhecer algumas das mais importantes:

1. len(): Medindo o Tamanho

len() significa "length" (comprimento) em inglês.
Essa função nos diz quantos caracteres uma string possui.
Exemplo:

```
nome = "Maria"
tamanho = len(nome)  # tamanho será 5
print(tamanho)
```

2. lower() e upper(): Mudando a Caixa

lower() transforma todos os caracteres da string em letras minúsculas.
upper() transforma todos os caracteres da string em letras maiúsculas.

Exemplo:

```
texto = "Python é INCRÍVEL!"
minusculo = texto.lower()  # minusculo será "python é incrível!"
maiusculo = texto.upper()  # maiusculo será "PYTHON É INCRÍVEL!"
```

3. strip(): Limpando os Espaços

strip() remove espaços em branco do início e do final da string.
Isso é útil quando recebemos textos de usuários, que podem acidentalmente digitar espaços extras.

Exemplo:

```
texto = "   Olá, mundo!   "
limpo = texto.strip()  # limpo será "Olá, mundo!"
```

split(): Dividindo em Pedaços


4. split() divide uma string em uma lista de substrings, usando um separador como critério.
   
Se não especificarmos um separador, o split() usará espaços em branco por padrão.

Exemplo:

```
frase = "Python é uma linguagem poderosa"
palavras = frase.split()  # palavras será ["Python", "é", "uma", "linguagem", "poderosa"]
data = "2023-10-27"
partes = data.split("-")  # partes será ["2023", "10", "27"]
```
5. Indexação e Fatiamento: Acessando Partes da String

Podemos acessar caracteres individuais de uma string usando índices, que começam em 0.
Também podemos extrair pedaços da string usando fatiamento.

Exemplo:

```
nome = "Carlos"
primeira_letra = nome[0]  # primeira_letra será "C"
parte = nome[1:4]  # parte será "arl"
```

6. Concatenação: Juntando Strings

Podemos usar o operador + para juntar duas ou mais strings.
Exemplo:
```
nome = "Ana"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome  # nome_completo será "Ana Silva"
```
