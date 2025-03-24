## DEF

## Em Python, a palavra-chave def é usada para definir funções. Funções são blocos de código nomeados que realizam tarefas específicas. 
## Elas são essenciais para organizar o código, torná-lo mais legível e reutilizável.

### Sintaxe Básica:

```
def nome_da_funcao(parametros):
    # Bloco de código da função
    # ...
    return valor_de_retorno  # Opcional
```
    
### def: Indica o início da definição da função.
### nome_da_funcao: O nome que você dá à sua função.
### parametros: Valores de entrada que a função pode receber (opcional).
### return: Encerra a função e retorna um valor (opcional).

### Exemplos Práticos:

### Função para somar dois números:

```
def somar(a, b):
    resultado = a + b
    return resultado

soma = somar(5, 3)
print(soma)  # Saída: 8
```

A função somar recebe dois parâmetros (a e b), calcula a soma e retorna o resultado.
Função para verificar se um número é par:

```
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(eh_par(6))   # Saída: True
print(eh_par(7))   # Saída: False
```

A função eh_par recebe um número, verifica se ele é divisível por 2 e retorna True ou False.
Função para imprimir uma mensagem personalizada:

```
def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("João")           # Saída: Olá, João!
saudacao("Maria", "Bom dia")  # Saída: Bom dia, Maria!
```

A função saudacao recebe um nome e uma mensagem (com valor padrão "Olá"). Ela imprime uma mensagem personalizada.
Vantagens de usar funções:

### Reutilização de código: Você pode chamar a mesma função várias vezes em diferentes partes do seu programa.
### Organização: Funções ajudam a dividir o código em blocos menores e mais fáceis de entender.
### Legibilidade: Funções com nomes descritivos tornam o código mais legível e fácil de manter.
### Modularidade: Funções permitem criar módulos de código independentes que podem ser reutilizados em outros projetos.
