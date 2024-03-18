# Introdução
As estruturas de dados são ferramentas essenciais para organizar e manipular dados em Python. Cada estrutura possui características e funcionalidades próprias, tornando-as adequadas para diferentes situações.

Nesta aula, exploraremos as principais estruturas de dados em Python: listas, tuplas, dicionários e conjuntos.

## 1. Listas
As listas são estruturas mutáveis que armazenam uma coleção ordenada de elementos de qualquer tipo. São versáteis e podem ser utilizadas para diversos fins, como armazenar nomes, números, datas, etc.

### Exemplo:

```
# Criando uma lista
lista_frutas = ["Maçã", "Banana", "Laranja", "Abacaxi"]

# Acessando elementos
print(lista_frutas[0])  # Saída: Maçã
print(lista_frutas[2])  # Saída: Laranja

# Adicionando elementos
lista_frutas.append("Melancia")

# Removendo elementos
lista_frutas.remove("Banana")

# Percorrendo a lista
for fruta in lista_frutas:
  print(fruta)
```

### Comentários:

lista_frutas é uma variável do tipo lista que armazena os nomes de quatro frutas.
Podemos acessar elementos da lista usando índices. O índice 0 representa o primeiro elemento, 1 o segundo, e assim por diante.
Podemos adicionar novos elementos ao final da lista usando o método append().
Podemos remover elementos da lista usando o método remove().
O loop for permite percorrer cada elemento da lista e realizar alguma ação.

## 2. Tuplas
As tuplas são semelhantes às listas, mas são imutáveis. Isso significa que, após a criação de uma tupla, não é possível adicionar, remover ou modificar seus elementos.

### Exemplo:

```
# Criando uma tupla
tupla_cores = ("Vermelho", "Verde", "Azul")

# Acessando elementos
print(tupla_cores[1])  # Saída: Verde

# Erro: tuplas são imutáveis
#tupla_cores.append("Amarelo")

# Percorrendo a tupla
for cor in tupla_cores:
  print(cor)
```

### Comentários:

tupla_cores é uma variável do tipo tupla que armazena as cores primárias.
As tuplas são imutáveis, o que significa que não podemos modificar seus elementos após a criação.
Podemos acessar elementos da tupla usando índices da mesma forma que as listas.

### 3. Dicionários
Os dicionários são estruturas que armazenam pares de chave-valor. As chaves são únicas e identificam cada valor associado. Os dicionários são ótimos para armazenar dados de forma organizada e eficiente, como informações de contato, dados de usuários, etc.

Exemplo:

```
# Criando um dicionário
dicionario_aluno = {
  "nome": "João Silva",
  "idade": 20,
  "curso": "Ciência da Computação"
}

# Acessando valores
print(dicionario_aluno["nome"])  # Saída: João Silva
print(dicionario_aluno["curso"])  # Saída: Ciência da Computação

# Adicionando elementos
dicionario_aluno["cidade"] = "São Paulo"

# Percorrendo o dicionário
for chave, valor in dicionario_aluno.items():
  print(f"{chave}: {valor}")
```

### Comentários:

dicionario_aluno é uma variável do tipo dicionário que armazena informações de um aluno.
As chaves do dicionário são strings que identificam cada informação.
Os valores do dicionário podem ser de qualquer tipo.
Podemos acessar valores usando a chave como índice.
O loop for permite percorrer cada par de chave-valor do dicionário.

### 4. Conjuntos
Os conjuntos são estruturas que armazenam coleções não ordenadas de elementos únicos. Eles são úteis para verificar a presença de elementos, realizar operações matemáticas entre conjuntos e eliminar elementos duplicados.

Exemplo:

```
# Criando um conjunto
numeros = {1, 2, 3, 4, 5, 2, 3}

# Verificando a presença de elementos

for x in numeros:
  print(x)
# Pode ser usado direto do print
print( 2 in numeros)

# Uma vez que um conjunto é criado, você não pode alterar seus itens, mas você pode adicionar novos itens.
# Para adicionar um item a um conjunto, use o add() método.
numeros = {1,2,3}
numeros.add(4)
print(numeros)
```
