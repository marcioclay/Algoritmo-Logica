# Função Range

A função range() em Python é uma ferramenta poderosa que permite gerar sequências de números com controle e flexibilidade. Quer você precise de uma contagem simples ou de uma iteração complexa, o range() está aqui para te ajudar!

### O que é o range()?

Imagine um função que pode conjurar sequências de números do nada. O range() é essa função! Ele gera sequências de números inteiros, permitindo que você especifique o início, o fim e o incremento da sequência.

### Estrutura da Função:

### A sintaxe básica do range() é simples:

- range(start, stop, step)
- Use o código com cuidado.
- start (opcional): Define o ponto de partida da sequência. Se omitido, o valor padrão é 0.
- stop (opcional): Define o limite superior da sequência. Se omitido, a sequência vai até o infinito.
- step (opcional): Define o incremento da sequência. Se omitido, o valor padrão é 1.

### Exemplos :

Sequência Simples:
```
for numero in range(10):
  print(numero)
```

### Resultado:

0
1
2
3
4
5
6
7
8
9

### Sequência com Início e Fim:
```
for numero in range(5, 15):
  print(numero)
```
### Resultado:

5
6
7
8
9
10
11
12
13
14

### Sequência com Incremento:

```
for numero in range(0, 20, 2):
  print(numero)
```

### Resultado:

0
2
4
6
8
10
12
14
16
18

### Funções Avançadas:

### Sequência Invertida:
```
for numero in range(10, 0, -1):
  print(numero)
```

### Resultado:

10
9
8
7
6
5
4
3
2
1

### Sequência com Limite Inferior Inclusivo:
```
for numero in range(include_start=5, stop=15):
  print(numero)
```
### Resultado:

5
6
7
8
9
10
11
12
13
14

### Observações Importantes:

- O range() gera um objeto iterável, não uma lista. Para convertê-lo em uma lista, use a função list().
- O stop não é incluído na sequência.
- O step pode ser positivo ou negativo, controlando a direção da sequência.

Domine a Arte da Geração de Sequências:
Com o range(), você pode criar sequências para diversos propósitos:

- Documentação Oficial: http://python-reference.readthedocs.io/en/latest/docs/functions/range.html
- Tutoriais: https://realpython.com/courses/python-range-function/
- Exemplos Avançados: https://www.geeksforgeeks.org/python-range-method/
