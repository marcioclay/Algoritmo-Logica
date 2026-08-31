## Métodos para Manipulação de Strings em Python

Este guia apresenta os métodos mais utilizados para trabalhar com textos (strings) em Python, acompanhados de explicações diretas e exemplos de código.

1. upper()

Converte todos os caracteres da string para letras maiúsculas.

```
texto = "python"
print(texto.upper())  # Saída: 'PYTHON'
```

2. lower()

Converte todos os caracteres da string para letras minúsculas.

```
texto = "PYTHON"
print(texto.lower())  # Saída: 'python'
```

3. strip()
Remove os espaços em branco (ou caracteres especificados) do início e do final da string.

```
texto = "   Olá, Mundo!   "
print(texto.strip())  # Saída: 'Olá, Mundo!'
```

4. replace()
Substitui todas as ocorrências de um trecho de texto por outro.

```
texto = "Gosto de Java"
print(texto.replace("Java", "Python"))  # Saída: 'Gosto de Python'
```

5. split()
Divide a string em uma lista de substrings com base em um delimitador (o padrão é o espaço).

```
texto = "maçã,banana,uva"
print(texto.split(","))  # Saída: ['maçã', 'banana', 'uva']
```

6. join()

Junta os elementos de uma lista de textos em uma única string, usando a string atual como separador.

```
frutas = ['maçã', 'banana', 'uva']
print(", ".join(frutas))  # Saída: 'maçã, banana, uva'
```

7. find()

Retorna a posição (índice) da primeira ocorrência de uma substring. Retorna -1 se o valor não for encontrado.

```
texto = "Aprender Python é legal"
print(texto.find("Python"))  # Saída: 9
print(texto.find("Java"))    # Saída: -1
```

8. index()

Funciona como o find(), mas lança uma exceção (ValueError) caso o texto procurado não exista na string.

```
texto = "Aprender Python é legal"
print(texto.index("Python"))  # Saída: 9
```

9. startswith()

Verifica se a string começa com um determinado trecho, retornando True ou False.

```
texto = "Python 3.10"
print(texto.startswith("Py"))  # Saída: True
```

10. endswith()

Verifica se a string termina com um determinado trecho, retornando True ou False.

```
arquivo = "relatorio.pdf"
print(arquivo.endswith(".pdf"))  # Saída: True
```

11. count()

Conta quantas vezes uma substring aparece no texto.

```
texto = "banana"
print(texto.count("a"))  # Saída: 3
```

12. capitalize()

Transforma o primeiro caractere da string em maiúsculo e deixa todo o restante em minúsculo.

```
texto = "olá MUNDO"
print(texto.capitalize())  # Saída: 'Olá mundo'
```

13. title()

Converte o primeiro caractere de cada palavra presente no texto para maiúsculo.

```
texto = "bem-vindo ao curso de python"
print(texto.title())  # Saída: 'Bem-Vindo Ao Curso De Python'
```

14. isalpha()

Verifica se a string contém apenas letras do alfabeto (sem números, espaços ou símbolos).

```
print("Python".isalpha())   # Saída: True
print("Python3".isalpha())  # Saída: False
```

15. isdigit()

Verifica se a string contém apenas dígitos numéricos.

```
print("12345".isdigit())  # Saída: True
print("123a".isdigit())   # Saída: False

16. isalnum()

Verifica se a string contém apenas caracteres alfanuméricos (letras e/ou números).

```
print("Python3".isalnum())   # Saída: True
print("Python 3".isalnum())  # Saída: False (devido ao espaço)
```
