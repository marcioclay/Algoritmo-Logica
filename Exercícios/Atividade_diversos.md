## Atividades

### 1. Lista de Números Pares:

```
def numeros_pares(lista):
    """Retorna uma lista com os números pares da lista original."""
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = numeros_pares(numeros)
print(pares)  # Saída: [2, 4, 6, 8, 10]
```

### 2. Verificação de Palíndromo:

```
def eh_palindromo(string):
    """Retorna True se a string for um palíndromo, False caso contrário."""
    string = string.lower()
    return string == string[::-1]

# Exemplo de uso
print(eh_palindromo("Arara"))  # Saída: True
print(eh_palindromo("Python"))  # Saída: False
```

### 3. Contagem de Vogais:

```
def contar_vogais(string):
    """Retorna o número de vogais na string."""
    vogais = "aeiou"
    contador = 0
    for letra in string.lower():
        if letra in vogais:
            contador += 1
    return contador

# Exemplo de uso
print(contar_vogais("Hello World"))  # Saída: 3
```

### 4. Média de Notas com Condição:

```

def media_notas(notas):
    """Retorna a média das notas e se o aluno foi aprovado ou reprovado."""
    media = sum(notas) / len(notas)
    if media >= 7:
        return media, "Aprovado"
    else:
        return media, "Reprovado"

# Exemplo de uso
notas = [7.5, 8.0, 6.5, 9.0]
resultado = media_notas(notas)
print(resultado)  # Saída: (7.75, 'Aprovado')
```

### 5. Validação de E-mail:

```
def eh_email_valido(email):
    """Retorna True se o e-mail for válido, False caso contrário."""
    return "@" in email and "." in email

# Exemplo de uso
print(eh_email_valido("teste@email.com"))  # Saída: True
print(eh_email_valido("testeemailcom"))  # Saída: False
```

### 6. Remoção de Duplicatas:

```

def remover_duplicatas(lista):
    """Retorna uma lista com os elementos únicos da lista original."""
    unicos = []
    for elemento in lista:
        if elemento not in unicos:
            unicos.append(elemento)
    return unicos

# Exemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5]
unicos = remover_duplicatas(lista)
print(unicos)  # Saída: [1, 2, 3, 4, 5]
```

### 7. Busca em Arquivo TXT:

```
def buscar_palavra_arquivo(nome_arquivo, palavra):
    """Retorna True se a palavra for encontrada no arquivo, False caso contrário."""
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                if palavra in linha:
                    return True
        return False
    except FileNotFoundError:
        return False

# Exemplo de uso
# Supondo que o arquivo "texto.txt" contenha a palavra "Python"
print(buscar_palavra_arquivo("texto.txt", "Python"))  # Saída: True
print(buscar_palavra_arquivo("texto.txt", "Java"))  # Saída: False
```
### 8. Inserção em Arquivo TXT:

```

def inserir_linhas_arquivo(nome_arquivo, linhas):
    """Insere as linhas no arquivo TXT."""
    try:
        with open(nome_arquivo, "a") as arquivo:
            for linha in linhas:
                arquivo.write(linha + "\n")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")

# Exemplo de uso
linhas = ["Linha 1", "Linha 2", "Linha 3"]
inserir_linhas_arquivo("texto.txt", linhas)
```

### 9. Ordenação de Lista de Strings:

```

def ordenar_strings(lista):
    """Retorna a lista de strings ordenada alfabeticamente."""
    return sorted(lista)

# Exemplo de uso
nomes = ["Carlos", "Ana", "Bruno", "Daniel"]
nomes_ordenados = ordenar_strings(nomes)
print(nomes_ordenados)  # Saída: ['Ana', 'Bruno', 'Carlos', 'Daniel']
```
### 10. Validação de Senha:

```

def senha_valida(senha):
    """Retorna True se a senha for válida, False caso contrário."""
    if len(senha) < 8:
        return False
    maiuscula = False
    minuscula = False
    numero = False
    for char in senha:
        if char.isupper():
            maiuscula = True
        elif char.islower():
            minuscula = True
        elif char.isdigit():
            numero = True
    return maiuscula and minuscula and numero

# Exemplo de uso
print(senha_valida("Senha123"))  # Saída: True
```
print(senha_valida("senha"))  # Saída: False
