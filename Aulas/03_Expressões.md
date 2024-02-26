# Expressões Aritméticas, Relacionais e Lógicas
## Objetivos
- Compreender o uso correto da Expressão Aritméticas
- Compreender o uso correto da Expressão Relacional
- Compreender o uso correto da Expressão Lógica

  Em Python, as expressões aritméticas permitem realizar cálculos matemáticos com números e variáveis. São compostas por operandos e operadores, que podem ser combinados para gerar um resultado.

### Operadores Aritméticos:

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
