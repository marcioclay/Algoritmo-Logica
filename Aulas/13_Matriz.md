# Lista dentro de Lista
Até o momento, em nossas listas, colocamos dados como números inteiros, float e strings.
Porém, é possível colocar também uma lista, dentro de uma lista.

A lista:

    notas = [10, 9, 8]


Possui apenas três elementos, três inteiros. Uma linha e 3 colunas, ok ?

Agora vamos supor que temos três alunos, onde cada aluno possui 3 notas.
Podemos inicializar uma lista com as notas desses três alunos da seguinte maneira:

```
notas= [ [10, 9, 8],
              [9, 8, 7],
              [8, 10, 5] ]
```

Ou seja, temos 3 listas dentro de uma lista.
Temos 3 linhas e 3 colunas (tente ver como uma matriz de elementos, uma tabela).


## Como acessar elementos de uma Matriz

As notas do primeiro aluno estão na lista notas[0]
As notas do segundo aluno estão na lista notas[1]
As notas do terceiro aluno estão na lista notas[2]

Para acessar a primeira nota do primeiro aluno: notas[0][0]
Para acessar a segunda nota do primeiro aluno: notas[0][1]
Para acessar a terceira nota do primeiro aluno : notas[0][2]
Para acessar a primeira nota do segundo aluno: notas[1][0]
Para acessar a segunda nota do segundo aluno: notas[1][1]
Para acessar a terceira nota do segundo aluno : notas[1][0]
Para acessar a primeira nota do terceiro aluno : notas[2][0]
Para acessar a segunda nota do terceiro aluno : notas[2][1]
Para acessar a terceira nota do terceiro aluno  : notas[2][2]

```
Para calcular a média das notas do primeiro aluno
(notas[0][0] + notas[0][1] +notas[0][2]) / 3

Para calcular a média das notas do segundo aluno
(notas[1][0] + notas[1][1] +notas[1][2]) / 3
```

Para calcular a média das notas do terceiro aluno
(notas[2][0] + notas[2][1] +notas[2][2]) / 3
