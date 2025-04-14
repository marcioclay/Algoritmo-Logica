## Manipulação de Arquivos 

### 1. Abrindo Arquivos com open()

A função open() é usada para abrir um arquivo. Para manipular um arquivo, você pode especificar o modo de abertura:

"r": modo de leitura.

"w": modo de escrita (sobrescreve o conteúdo do arquivo).

"a": modo de adição (adiciona ao final do arquivo, sem apagar o conteúdo existente).

Exemplo básico:

```
arquivo = open("exemplo.txt", "r")  # Abre para leitura
arquivo.close()  # Não se esqueça de fechar o arquivo após o uso
```

### 2. Lendo Dados de um Arquivo

a) Lendo o Arquivo Inteiro
Para ler todo o conteúdo de um arquivo:

```
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

b) Lendo Linha por Linha
Caso queira ler apenas uma linha de cada vez:

```
arquivo = open("exemplo.txt", "r")
linha = arquivo.readline()
print(linha)  # Exibe a primeira linha
arquivo.close()
```

c) Lendo Várias Linhas (Lista de Linhas)
Se quiser carregar todas as linhas em uma lista:

```
arquivo = open("exemplo.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    print(linha.strip())  # Exibe cada linha, removendo quebras de linha
arquivo.close()
```
### 3. Escrevendo em um Arquivo
Ao escrever em um arquivo, certifique-se de abrir o arquivo em modo de escrita ("w") ou adição ("a").

a) Escrevendo Dados (Sobrescrevendo)
```
arquivo = open("exemplo.txt", "w")
arquivo.write("Olá, mundo!\n")
arquivo.write("Essa é a segunda linha.\n")
arquivo.close()
```
b) Adicionando Dados
```
arquivo = open("exemplo.txt", "a")
arquivo.write("Adicionando mais uma linha.\n")
arquivo.close()
```
### 4. Apagando Dados de um Arquivo
Para apagar o conteúdo de um arquivo, basta abrir no modo de escrita ("w"), pois isso sobrescreve o conteúdo:

```
arquivo = open("exemplo.txt", "w")
arquivo.close()  # O arquivo estará vazio após esta operação
```
### 5. Buscando Dados Específicos
Para procurar por uma palavra ou texto específico no arquivo:

```
arquivo = open("exemplo.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    if "palavra_chave" in linha:
        print("Encontrado:", linha.strip())
arquivo.close()
```
Considerações Finais
Manipular arquivos pode ser incrivelmente útil para lidar com grandes volumes de dados, armazenar informações ou criar relatórios automatizados. Agora que você aprendeu os conceitos básicos, que tal praticar? Crie um arquivo .txt, insira algumas informações e experimente os códigos acima. Boa sorte na sua jornada com Python!
