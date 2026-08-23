# Listas em Python

## 1. O que são listas?

Uma **lista** é uma estrutura utilizada para armazenar vários valores dentro de uma única variável.

Por exemplo, imagine que precisamos armazenar os nomes de cinco alunos. Poderíamos criar cinco variáveis:

```python
aluno1 = "Ana"
aluno2 = "Carlos"
aluno3 = "João"
aluno4 = "Maria"
aluno5 = "Pedro"
```
Isso funciona, mas não é uma forma prática de trabalhar com muitos dados.

Podemos utilizar uma lista: 
```
alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]
```

Agora todos os nomes estão armazenados dentro da variável alunos.
--- 

## 2. Como criar uma lista

Para criar uma lista utilizamos colchetes [].

```
alunos = ["Ana", "Carlos", "João"]
```

Uma lista também pode armazenar números:

```
idades = [18, 20, 19, 22]
```

Também podemos criar uma lista vazia:
```
alunos = []
```
Nesse caso, a lista foi criada, mas ainda não possui elementos.

## 3. Diferentes tipos de dados em uma lista

Uma lista pode armazenar diferentes tipos de dados:
```
dados = ["Maria", 25, 1.65, True]
```
Nesse exemplo temos:

- "Maria" → string
- 25 → int
- 1.65 → float
- True → bool


Entretanto, para quem está começando a programar, é recomendável trabalhar inicialmente com listas que armazenem dados do mesmo tipo.

Exemplo:
```
nomes = ["Ana", "Carlos", "João"]
```

## 4. Índices da lista

Cada elemento de uma lista possui uma posição chamada de índice.

Em Python, o primeiro índice é 0.

Considere a lista:

```
alunos = ["Ana", "Carlos", "João"]
```

Podemos representá-la assim:

```
Índice:     0         1         2
            ↓         ↓         ↓
Lista:    ["Ana", "Carlos", "João"]
```

Portanto:

print(alunos[0])

Saída:
```
Ana
```

Outro exemplo:
```
print(alunos[1])
```
Saída:
```
Carlos
```
E:
```
print(alunos[2])
```

Saída:
```
João
```

Atenção

O primeiro elemento está no índice 0, e não no índice 1.

## 5. Alterando um elemento

Podemos alterar um elemento utilizando seu índice.

```
alunos = ["Ana", "Carlos", "João"]

alunos[1] = "Pedro"

print(alunos)

Saída:

['Ana', 'Pedro', 'João']
```

O elemento "Carlos" foi substituído por "Pedro".

## 6. Adicionando elementos com append()

O método append() adiciona um novo elemento no final da lista.
```
alunos = ["Ana", "Carlos"]

alunos.append("João")

print(alunos)

Saída:

['Ana', 'Carlos', 'João']
```

Podemos adicionar vários elementos:

```
alunos.append("Maria")
alunos.append("Pedro")

print(alunos)

Saída:

['Ana', 'Carlos', 'João', 'Maria', 'Pedro']
```

## 7. Inserindo elementos com insert()

O método insert() permite adicionar um elemento em uma posição específica.

A sintaxe é:
```
lista.insert(posicao, elemento)
```
Exemplo:

```
alunos = ["Ana", "Carlos", "João"]

alunos.insert(1, "Maria")

print(alunos)

Saída:

['Ana', 'Maria', 'Carlos', 'João']
```

Observe que "Maria" foi inserida no índice 1.

## 8. Removendo elementos com remove()

O método remove() remove um elemento pelo seu valor.

```
alunos = ["Ana", "Carlos", "João"]

alunos.remove("Carlos")

print(alunos)

Saída:

['Ana', 'João']
```

Atenção

O valor informado precisa existir na lista.

Se tentarmos:
```
alunos.remove("Pedro")
```

e "Pedro" não estiver na lista, o Python apresentará um erro.

## 9. Removendo elementos com pop()

O método pop() remove um elemento utilizando seu índice.
```
alunos = ["Ana", "Carlos", "João"]

alunos.pop(1)

print(alunos)

Saída:

['Ana', 'João']
```

O elemento que estava no índice 1 foi removido.

pop() sem índice

Também podemos utilizar pop() sem informar o índice:
```
alunos = ["Ana", "Carlos", "João"]

alunos.pop()

print(alunos)

Saída:

['Ana', 'Carlos']
```

Quando utilizado sem índice, pop() remove o último elemento.

## 10. Removendo elementos com del

Outra forma de remover um elemento é utilizando del.

```
alunos = ["Ana", "Carlos", "João"]

del alunos[1]

print(alunos)

Saída:

['Ana', 'João']
```

Também podemos utilizar del para excluir toda a lista:
```
del alunos
```

Depois disso, a variável alunos não existirá mais.

## 11. Listando os elementos

Podemos mostrar uma lista inteira utilizando print():

```
alunos = ["Ana", "Carlos", "João"]

print(alunos)

Saída:

['Ana', 'Carlos', 'João']
```

Porém, muitas vezes queremos mostrar cada elemento separadamente.

Para isso podemos utilizar o for:

```
alunos = ["Ana", "Carlos", "João"]

for aluno in alunos:
    print(aluno)

Saída:

Ana
Carlos
João
```

O for percorre a lista elemento por elemento.

## 12. Descobrindo a quantidade de elementos

A função len() informa a quantidade de elementos existentes na lista.
```
alunos = ["Ana", "Carlos", "João"]

print(len(alunos))

Saída:

3
```

Outro exemplo:
```
numeros = [10, 20, 30, 40, 50]

print(len(numeros))

Saída:

5
```

## 13. Verificando se um elemento existe

Podemos verificar se determinado elemento está dentro da lista utilizando in.
```
alunos = ["Ana", "Carlos", "João"]

print("Ana" in alunos)

Saída:

True
```

Agora:
```
print("Pedro" in alunos)

Saída:

False
```
Podemos utilizar essa verificação com if:
```
alunos = ["Ana", "Carlos", "João"]

nome = input("Digite um nome: ")

if nome in alunos:
    print("Aluno encontrado!")
else:
    print("Aluno não encontrado!")
```

## 14. Percorrendo uma lista com for

Uma das operações mais importantes com listas é percorrer seus elementos.
```
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(fruta)

Saída:

maçã
banana
laranja
uva
```
A variável fruta recebe um elemento da lista a cada repetição.

## 15. Percorrendo uma lista utilizando índices

Também podemos percorrer uma lista utilizando range() e len().
```
alunos = ["Ana", "Carlos", "João"]

for i in range(len(alunos)):
    print(alunos[i])

Saída:

Ana
Carlos
João
```

Nesse exemplo:
```
len(alunos) informa a quantidade de elementos;
range() cria uma sequência de números;
i representa o índice;
alunos[i] acessa o elemento.
```

Quando não precisamos do índice, é mais simples utilizar:
```
for aluno in alunos:
    print(aluno)
```

## 16. Ordenando uma lista com sort()

O método sort() organiza os elementos da lista.

Números
```
numeros = [50, 10, 30, 20, 40]

numeros.sort()

print(numeros)

Saída:

[10, 20, 30, 40, 50]

```

Strings
```
alunos = ["João", "Ana", "Carlos", "Maria"]

alunos.sort()

print(alunos)

Saída:

['Ana', 'Carlos', 'João', 'Maria']
```

## 17. Invertendo uma lista com reverse()

O método reverse() inverte a ordem dos elementos.
```
numeros = [10, 20, 30, 40, 50]

numeros.reverse()

print(numeros)

Saída:

[50, 40, 30, 20, 10]
```

## 18. Trabalhando com listas de números

Podemos utilizar algumas funções do Python para trabalhar com listas numéricas.
```
notas = [7, 8, 9, 6, 10]
Maior valor
print(max(notas))

Saída:

10
```

Menor valor
```
print(min(notas))

Saída:

6
```

Soma
```
print(sum(notas))

Saída:

40
```

Quantidade
```
print(len(notas))

Saída:

5
```

Média

Podemos utilizar essas funções para calcular a média:
```
media = sum(notas) / len(notas)

print(media)

Saída:

8.0
```

## 19. Copiando uma lista

Podemos criar uma cópia de uma lista utilizando copy().
```
alunos = ["Ana", "Carlos", "João"]

copia = alunos.copy()

print(copia)

Saída:

['Ana', 'Carlos', 'João']
```

A cópia permite trabalhar com uma segunda lista sem alterar diretamente a lista original.

## 20. Limpando uma lista

O método clear() remove todos os elementos da lista.
```
alunos = ["Ana", "Carlos", "João"]

alunos.clear()

print(alunos)

Saída:

[]
```

A lista continua existindo, mas agora está vazia.

## 21. Exemplo completo

Vamos criar um programa simples para cadastrar alunos.
```
alunos = []

alunos.append("Ana")
alunos.append("Carlos")
alunos.append("João")

print("Lista de alunos:")

for aluno in alunos:
    print(aluno)

print("Quantidade de alunos:", len(alunos))

Saída:

Lista de alunos:
Ana
Carlos
João
Quantidade de alunos: 3
```


## 22. Lista utilizando input()

Podemos permitir que o usuário informe os nomes.
```
alunos = []

nome1 = input("Digite o primeiro aluno: ")
nome2 = input("Digite o segundo aluno: ")
nome3 = input("Digite o terceiro aluno: ")

alunos.append(nome1)
alunos.append(nome2)
alunos.append(nome3)

print("\nAlunos cadastrados:")

for aluno in alunos:
    print(aluno)
```

## 23. Cadastro utilizando for

Podemos melhorar o programa anterior utilizando uma estrutura de repetição.

```
alunos = []

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

print("\nAlunos cadastrados:")

for aluno in alunos:
    print(aluno)
```

Nesse exemplo:

Uma lista vazia é criada.
O for é executado três vezes.
O usuário informa um nome.
O nome é adicionado à lista.
Ao final, os nomes são apresentados.


## 24. Principais comandos

Comando	Função	Exemplo
[]	Cria uma lista	alunos = []
append()	Adiciona no final	alunos.append("Ana")
insert()	Adiciona em uma posição	alunos.insert(1, "Ana")
remove()	Remove pelo valor	alunos.remove("Ana")
pop()	Remove pelo índice	alunos.pop(0)
del	Remove pelo índice	del alunos[0]
len()	Retorna a quantidade	len(alunos)
in	Verifica se existe	"Ana" in alunos
sort()	Ordena a lista	alunos.sort()
reverse()	Inverte a lista	alunos.reverse()
clear()	Remove todos os elementos	alunos.clear()
copy()	Copia a lista	nova = alunos.copy()
max()	Retorna o maior valor	max(notas)
min()	Retorna o menor valor	min(notas)
sum()	Soma os valores	sum(notas)





