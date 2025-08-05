# 🧠 O que é uma matriz?
Uma matriz é uma estrutura de dados que representa uma tabela de elementos organizados em linhas e colunas. Em Python, uma matriz pode ser representada de diversas formas, mas a forma mais comum para iniciantes é usar listas dentro de listas (listas aninhadas).

Exemplo visual:
Uma matriz 2x3 (2 linhas, 3 colunas) pode ser representada assim:

1  2  3
4  5  6
Em Python, fica assim:

python
```
matriz = [[1, 2, 3],
          [4, 5, 6]]
```

## 🧪 Criando e acessando elementos
🔹 Como acessar um elemento?
Basta usar dois índices: [linha][coluna]

```
print(matriz[0][1])  # Resultado: 2 (linha 0, coluna 1)
```
##🔹 Como percorrer a matriz com for?
```
for linha in matriz:
    for elemento in linha:
        print(elemento)
```

## 🔧 Manipulando a matriz
🔹 Alterar um valor:
```
matriz[1][2] = 10  # Muda o 6 para 10
```
🔹 Adicionar uma nova linha:
```
matriz.append([7, 8, 9])
```
📦 Dica: Use o pacote NumPy para operações avançadas
Para quem quer ir além, o pacote NumPy é ideal. Com ele, você pode fazer cálculos matemáticos com matrizes muito mais facilmente.

```
import numpy as np

matriz_np = np.array([[1, 2, 3],
                      [4, 5, 6]])

print(matriz_np.shape)  # Mostra o tamanho da matriz
print(matriz_np[1, 2])  # Acessa o elemento na linha 1, coluna 2
```
