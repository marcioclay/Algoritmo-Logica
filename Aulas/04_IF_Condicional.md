# CONDICIONAL IF

Em Python, a estrutura condicional if permite executar diferentes ações com base em uma condição booleana. 
É uma ferramenta fundamental para controlar o fluxo de execução de um programa.

##Estrutura básica:

```
if condicao:
    # Bloco de código a ser executado se a condição for True
else:
    # Bloco de código a ser executado se a condição for False
```

Exemplo:
```
Python
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
else:
    print("O número é negativo")
```

Variações:


### elif: Permite verificar outras condições além da primeira.
```
numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero == 0:
    print("O número é zero")
else:
    print("O número é negativo")
```

### if aninhado: Permite verificar condições dentro de outras condições.

```
numero = int(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par")
    else:
        print("O número é positivo e ímpar")
else:
    print("O número é negativo")
```

Dicas:

Utilize indentação para organizar o código e facilitar a leitura.
Utilize comentários para explicar o que cada parte do código faz.
Teste o código com diferentes valores de entrada para garantir que ele esteja funcionando corretamente.
Exemplos de uso:

Validar a entrada de dados do usuário.
Exibir diferentes mensagens de acordo com a situação.
Executar diferentes ações com base em um valor.
Recursos adicionais:

Tutorial Python: [https://www.devmedia.com.br/python-estrutura-condicional-if-else/38217]
Tutoriais sobre estruturas condicionais: [https://www.w3schools.com/python/default.asp]
Observações:

O condicional if é uma ferramenta poderosa, mas deve ser usado com cuidado.
É importante pensar cuidadosamente nas condições que serão verificadas e nos blocos de código que serão executados.
O uso excessivo de aninhamento de if pode tornar o código difícil de ler e entender.
