# Expressões Aritméticas, Relacionais e Lógicas
## Objetivos
- Compreender o uso correto da Expressão Aritméticas
- Compreender o uso correto da Expressão Relacional
- Compreender o uso correto da Expressão Lógica

  Em Python, as expressões aritméticas permitem realizar cálculos matemáticos com números e variáveis. São compostas por operandos e operadores, que podem ser combinados para gerar um resultado.

*********************************************   ## OPERADORES ARITMÉTICOS  **************************************************

- Adição (+): Soma dois valores.
- Subtração (-): Subtrai o segundo valor do primeiro.
- Multiplicação (*): Multiplica dois valores.
- Divisão (/): Divide o primeiro valor pelo segundo.
- Divisão inteira (//): Divide o primeiro valor pelo segundo e retorna o quociente inteiro.
- Módulo (%): Retorna o resto da divisão do primeiro valor pelo segundo.
- Exponenciação ():** Eleva o primeiro valor à potência do segundo.

Exemplos:

1. Soma:
   resultado = 2 + 3
   print(resultado) # Saída: 5
```
resultado = 2 + 3
print(resultado) # Saída: 5
```   

2. Subtração:
```
resultado = 5 - 2
print(resultado) # Saída: 3
```
3. Multiplicação:
```
resultado = 2 * 3
print(resultado) # Saída: 6
```
4. Divisão:

```
resultado = 6 / 2
print(resultado) # Saída: 3.0
```
5. Divisão inteira:

```
resultado = 6 // 2
print(resultado) # Saída: 3
```
6. Módulo:

```
resultado = 6 % 2
print(resultado) # Saída: 0
```
7. Exponenciação:

```
resultado = 2 ** 3
print(resultado) # Saída: 8
```

### Ordem de Precedência:

A ordem de precedência define a ordem em que as operações são realizadas em uma expressão.

- Parênteses
- Exponenciação
- Multiplicação e Divisão
- Adição e Subtração
  
Exemplos:

```
resultado = 2 + 3 * 4
print(resultado) # Saída: 14 (Primeiro a multiplicação, depois a soma)

resultado = (2 + 3) * 4
print(resultado) # Saída: 20 (Primeiro a soma, depois a multiplicação)
```

********************************************* ## OPERADORES RELACIONAIS ******************************************************

Em Python, as expressões relacionais permitem comparar valores e determinar se são verdadeiros ou falsos. Elas são utilizadas em instruções condicionais para controlar o fluxo de execução de um programa.


- Igual a (==): Verifica se dois valores são iguais.
- Diferente de (!=): Verifica se dois valores são diferentes.
- Maior que (>): Verifica se o primeiro valor é maior que o segundo.
- Menor que (<): Verifica se o primeiro valor é menor que o segundo.
- Maior ou igual a (>=): Verifica se o primeiro valor é maior ou igual ao segundo.
- Menor ou igual a (<=): Verifica se o primeiro valor é menor ou igual ao segundo.
  
Exemplos:

1. Igualdade:

```
valor1 = 5
valor2 = 5

resultado = valor1 == valor2
print(resultado) # Saída: True
```

2. Diferença:

```
valor1 = 5
valor2 = 6

resultado = valor1 != valor2
print(resultado) # Saída: True
```

3. Maior que:

```
valor1 = 6
valor2 = 5

resultado = valor1 > valor2
print(resultado) # Saída: True
```

4. Menor que:

```
valor1 = 5
valor2 = 6

resultado = valor1 < valor2
print(resultado) # Saída: True
```

5. Maior ou igual a:

```
valor1 = 5
valor2 = 5

resultado = valor1 >= valor2
print(resultado) # Saída: True
```

6. Menor ou igual a:

```
valor1 = 5
valor2 = 6

resultado = valor1 <= valor2
print(resultado) # Saída: True
```

Utilização em instruções condicionais:

As expressões relacionais podem ser utilizadas em instruções if para controlar o fluxo de execução de um programa.

```
valor = int(input("Digite um número: "))

if valor > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
```
