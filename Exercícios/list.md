## Atividade de Fixação - Lista

 1. Soma dos Elementos:

- Crie uma lista chamada numeros com os seguintes valores: [10, 5, 20, 8, 15].
- Escreva um programa que calcule a soma de todos os elementos dentro dessa lista.
- Exiba o resultado da soma na tela.

```
numeros = [10, 5, 20, 8, 15]
soma = 0
for num in numeros:
    soma = soma + num
print(f"A soma dos elementos da lista é: {soma}")
```

2. Média dos Elementos:

- Crie uma lista chamada notas com os seguintes valores: [7.5, 8.0, 6.5, 9.0, 7.0].
- Escreva um programa que calcule a média aritmética das notas contidas na lista.
- Exiba a média na tela. Considere que a média é a soma dos elementos dividida
  pelo número de elementos.

```
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
soma = 0
for nota in notas:
    soma = soma + nota
if len(notas) > 0:
    media = soma / len(notas)
    print(f"A média das notas é: {media}")
else:
    print("A lista de notas está vazia.")
```

3. Encontrar o Maior Elemento:

- Crie uma lista chamada valores com os seguintes valores: [3, 12, 7, 25, 9].
- Escreva um programa que encontre o maior valor presente na lista.
- Exiba o maior valor na tela.
   
```
valores = [3, 12, 7, 25, 9]
if len(valores) > 0:
    maior = valores[0]
    for valor in valores:
        if valor > maior:
            maior = valor
    print(f"O maior valor da lista é: {maior}")
else:
    print("A lista está vazia.")
```

4. Inverter uma Lista:

- Crie uma lista chamada cores com os seguintes elementos: ["vermelho", "verde", "azul", "amarelo"].
- Escreva um programa que crie uma nova lista contendo os mesmos elementos da lista cores, mas na ordem inversa.
- Exiba a lista original e a lista invertida na tela.

```
cores = ["vermelho", "verde", "azul", "amarelo"]
lista_invertida = []
for i in range(len(cores) - 1, -1, -1):
    lista_invertida.append(cores[i])
print(f"Lista original: {cores}")
print(f"Lista invertida: {lista_invertida}")
```

5. Contar Ocorrências de um Elemento:

- Crie uma lista chamada frutas com os seguintes elementos: ["maçã", "banana", "laranja", "maçã", "uva", "maçã"].
- Defina uma variável chamada elemento_para_contar com o valor "maçã".
- Escreva um programa que conte quantas vezes o elemento armazenado na variável elemento_para_contar aparece dentro da lista frutas.
- Exiba a quantidade de ocorrências na tela.

```
frutas = ["maçã", "banana", "laranja", "maçã", "uva", "maçã"]
elemento_para_contar = "maçã"
contador = 0
for fruta in frutas:
    if fruta == elemento_para_contar:
        contador += 1
print(f"A fruta '{elemento_para_contar}' aparece {contador} vezes na lista.")
```
