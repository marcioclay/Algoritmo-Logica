# Tratamento de Erros em Python com try e except: Um Guia Completo e Detalhado

## O Python oferece um sistema robusto de tratamento de erros utilizando as instruções try e except.

### Objetivo:

### Este guia irá te auxiliar a entender e utilizar de forma eficaz os recursos de tratamento de erros em Python, com exemplos práticos e detalhados.

1. Introdução:

Erros são eventos indesejáveis que podem ocorrer durante a execução de um programa por diversos motivos, como falhas na entrada de dados, operações matemáticas inválidas ou problemas de acesso a arquivos.

O tratamento adequado de erros é crucial para garantir a confiabilidade e robustez do seu código, evitando falhas inesperadas e proporcionando uma melhor experiência para o usuário.

2. Bloco try:

O bloco try é utilizado para agrupar instruções de código que podem gerar erros. Dentro do bloco try, o Python tentará executar as instruções normalmente.

Exemplo:

```
try:
  # Tente abrir o arquivo
  arquivo = open("meu_arquivo.txt", "r")

  # Leia o conteúdo do arquivo
  conteudo = arquivo.read()

  # Imprima o conteúdo na tela
  print(conteudo)

except Exception as erro:
  # Se ocorrer um erro, o código dentro do `except` será executado
  print(f"Erro ao abrir o arquivo: {erro}")
finally:
  # O bloco `finally` é opcional e será executado sempre, mesmo que não haja erro
  print("Fechando o arquivo...")
  arquivo.close()
```


3. Bloco except:

O bloco except é utilizado para capturar e tratar erros específicos que podem ocorrer dentro do bloco try.

Exemplo:

```
try:
  # Tente converter a string para um número inteiro
  numero = int("10a")

  # Realize uma operação matemática
  resultado = numero / 2

  # Imprima o resultado
  print(resultado)

except ValueError as erro:
  # Se a conversão falhar (ValueError), o código dentro do `except` será executado
  print(f"Erro de conversão: {erro}")
  print("A string deve conter apenas números.")

except ZeroDivisionError as erro:
  # Se a divisão por zero ocorrer (ZeroDivisionError), o código dentro do `except` será executado
  print(f"Erro de divisão: {erro}")
  print("Não é possível dividir por zero.")
```

4. Múltiplos Blocos except:

É possível ter diversos blocos except dentro de um mesmo bloco try, capturando diferentes tipos de erros. A ordem dos blocos except é importante, pois o Python irá verificar as exceções na ordem em que foram definidas.

Exemplo:

```
try:
  # Tente abrir o arquivo
  arquivo = open("meu_arquivo.txt", "r")

  # Leia o conteúdo do arquivo
  conteudo = arquivo.read()

  # Converta o conteúdo para um número inteiro
  numero = int(conteudo)

  # Realize uma operação matemática
  resultado = numero / 2

  # Imprima o resultado
  print(resultado)

except FileNotFoundError as erro:
  # Se o arquivo não existir (FileNotFoundError), o código dentro do `except` será executado
  print(f"Erro: Arquivo '{erro.filename}' não encontrado.")

except ValueError as erro:
  # Se a conversão falhar (ValueError), o código dentro do `except` será executado
  print(f"Erro de conversão: {erro}")
  print("O conteúdo do arquivo não é um número válido.")

except ZeroDivisionError as erro:
  # Se a divisão por zero ocorrer (ZeroDivisionError), o código dentro do `except` será executado
  print(f"Erro de divisão: {erro}")
  print("Não é possível dividir por zero.")

finally:
  # O bloco `finally` é opcional e será executado sempre, mesmo que não haja erro
  print("Fechando o arquivo...")
  arquivo.close()
```

5. Objeto de Exceção (Exception):

O objeto de exceção (Exception) captura um erro genérico. É possível utilizar subclasses de Exception para capturar erros mais específicos, como ValueError, FileNotFoundError, ZeroDivisionError, entre outras.

6. Bloco finally:

O bloco finally é opcional e será executado sempre, mesmo que não haja erro. É utilizado para realizar tarefas de finalização, como fechar arquivos.

Exemplo
```
try:
    n = input("Digite um numero maior que 10: ")
    if n > 10:
        print("numero maior que 10")
    else:
        print("Numero menor que 10")

except Exception as erro:
    print(f"Entrada incorreta : {erro}")
finally:
    print("Digite novamente")
```
