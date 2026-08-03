## Operadores Lógicos, Aritméticos e Relacionais

Antes de um programa tomar decisões ou realizar cálculos, ele precisa comparar informações e executar operações matemáticas. Para isso, utilizamos os operadores, que são símbolos responsáveis por manipular valores e produzir resultados.

Na programação, os operadores são divididos em três grupos principais:

- Operadores Aritméticos – realizam cálculos matemáticos;
- Operadores Relacionais – comparam valores;
- Operadores Lógicos – combinam condições para auxiliar na tomada de decisões.

Esses operadores são fundamentais para a construção de algoritmos e serão utilizados praticamente em todos os programas desenvolvidos ao longo do curso.

### 1. Operadores Aritméticos

Os operadores aritméticos são utilizados para realizar cálculos matemáticos, assim como fazemos em uma calculadora.

| Operador | Descrição        | Exemplo      |
| -------- | ---------------- | ------------ |
| +        | Soma             | 5 + 3 = 8    |
| -        | Subtração        | 8 - 2 = 6    |
| *        | Multiplicação    | 4 * 3 = 12   |
| /        | Divisão          | 10 / 2 = 5.0 |
| //       | Divisão inteira  | 10 // 3 = 3  |
| %        | Resto da divisão | 10 % 3 = 1   |
| **       | Potência         | 2 ** 3 = 8   |


Exemplo
```
numero1 = 20
numero2 = 6

print("Soma:", numero1 + numero2)
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)
print("Divisão:", numero1 / numero2)
print("Divisão inteira:", numero1 // numero2)
print("Resto:", numero1 % numero2)
print("Potência:", numero1 ** 2)
```

Saída

```
Soma: 26
Subtração: 14
Multiplicação: 120
Divisão: 3.3333333333333335
Divisão inteira: 3
Resto: 2
Potência: 400
```

Exemplo prático

Imagine que uma loja vende um produto por R$ 150,00.

``` 
preco = 150
quantidade = 3

total = preco * quantidade

print("Valor total:", total)
```

Resultado:

```
Valor total: 450
```

Nesse exemplo, utilizamos a multiplicação para calcular o valor total da compra.
---

### 2. Operadores Relacionais

Os operadores relacionais são utilizados para comparar dois valores.

O resultado de uma comparação sempre será:

- True (verdadeiro)
- False (falso)

  | Operador | Significado    |
| -------- | -------------- |
| ==       | Igual          |
| !=       | Diferente      |
| >        | Maior          |
| <        | Menor          |
| >=       | Maior ou igual |
| <=       | Menor ou igual |

Exemplo
```
idade = 20

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 20)
print(idade <= 20)
```

Saída
```
False
True
True
False
True
True
```

Exemplo prático

Verificar se um aluno foi aprovado.
```
nota = 8

print(nota >= 7)
```
Resultado
```
True
```
--- 

### 3. Operadores Lógicos

Os operadores lógicos permitem combinar duas ou mais condições.

São muito utilizados em estruturas de decisão, como o comando if.

Os principais operadores são:

| Operador | Significado |
| -------- | ----------- |
| and      | E           |
| or       | OU          |
| not      | NÃO         |

#### Operador AND

O operador and exige que todas as condições sejam verdadeiras.

Exemplo
```
idade = 20
possui_carteira = True

print(idade >= 18 and possui_carteira)
```

Resultado
```
True
```

#### Operador OR

O operador or exige que apenas uma condição seja verdadeira.

Exemplo
```
chuva = False
guarda_chuva = True

print(chuva or guarda_chuva)
```

Resultado
```
True
```
Outro exemplo:
```
chuva = False
guarda_chuva = False

print(chuva or guarda_chuva)
```
Resultado
```
False
```

#### Operador NOT

O operador not inverte o valor lógico.

Exemplo
```
ligado = True

print(not ligado)
```
Resultado
```
False
```

Exemplo Completo

Um sistema deve verificar se uma pessoa pode entrar em um evento.

Regras:
```
Ter 18 anos ou mais;
Possuir ingresso.
idade = 22
ingresso = True

print(idade >= 18 and ingresso)
```
Resultado
```
True
```
