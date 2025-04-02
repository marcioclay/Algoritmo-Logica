## Manipulação de Arquivos TXT em Python: open(), close() e with

Em Python, a manipulação de arquivos TXT é essencial para ler e escrever dados em arquivos de texto simples. A função open() é a chave para interagir com arquivos, permitindo abrir, ler e escrever dados. O método close() garante que o arquivo seja fechado corretamente após a manipulação. A instrução with simplifica esse processo, lidando automaticamente com o fechamento do arquivo.

### 1. Abrindo e Fechando Arquivos com open() e close():

### Abrindo um arquivo: A função open() recebe o nome do arquivo e o modo de abertura como argumentos. Os modos comuns são:
'r': Leitura (o arquivo deve existir).
'w': Escrita (cria um novo arquivo ou sobrescreve um existente).
'a': Adição (adiciona dados ao final do arquivo).
'x': Criação exclusiva (cria um novo arquivo, falha se o arquivo já existir).
Fechando um arquivo: O método close() encerra a conexão com o arquivo, liberando recursos do sistema.

Exemplo:

```
try:
    arquivo = open('meu_arquivo.txt', 'w')  # Abre o arquivo para escrita
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo de escrita em arquivo.\n')
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
finally:
    if 'arquivo' in locals():
        arquivo.close()  # Fecha o arquivo
```
        
2. Usando with para Manipulação de Arquivos:

A instrução with simplifica a manipulação de arquivos, garantindo que o arquivo seja fechado automaticamente, mesmo em caso de erros.
O bloco with cria um contexto no qual o arquivo é aberto e fechado automaticamente após a conclusão do bloco.
Exemplo:

```
try:
    with open('meu_arquivo.txt', 'r') as arquivo:  # Abre o arquivo para leitura
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
```

Vantagens do with:

Simplicidade: O código fica mais conciso e legível.
Segurança: O arquivo é sempre fechado, mesmo em caso de erros.
Eficiência: Evita vazamentos de recursos do sistema.
Exemplo Prático:


# Escrevendo dados em um arquivo
```
dados = ['Nome: João', 'Idade: 30', 'Cidade: São Paulo']
try:
    with open('dados.txt', 'w') as arquivo:
        for linha in dados:
            arquivo.write(linha + '\n')
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
```

# Lendo dados de um arquivo
```
try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            print(linha.strip())  # Remove espaços em branco extras e quebras de linha
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
    ```
## Conclusão:

A manipulação de arquivos TXT em Python é facilitada pelas funções open() e close(), e simplificada pela instrução with. O with é a forma mais recomendada, pois garante o fechamento automático do arquivo e torna o código mais limpo e seguro.

## Para imprimir a lista na horizontal tanto no console quanto em um arquivo de texto, você precisa ajustar a forma como os elementos da lista são formatados antes de serem impressos ou escritos no arquivo.

1. Imprimindo na Horizontal no Console:

Para imprimir os elementos da lista na horizontal no console, você pode usar a função print() com o argumento end para especificar o caractere que separa os elementos. Por padrão, end é uma quebra de linha (\n), mas você pode alterá-lo para um espaço (' ') ou outro caractere de sua escolha.

```
inserir = [3, 2, 6, 4, 8, 7]

# Imprimindo na horizontal com espaços entre os elementos
for x in inserir:
    print(x, end=' ')

print()  # Adiciona uma quebra de linha no final para evitar que a próxima impressão fique na mesma linha
```
2. Escrevendo no Arquivo de Texto na Horizontal:

Para escrever os elementos da lista na horizontal em um arquivo de texto, você precisa formatar a string que será escrita no arquivo de forma semelhante à saída do console.

inserir = [3, 2, 6, 4, 8, 7]

# Formatando a string com espaços entre os elementos
linha = ' '.join(map(str, inserir))

# Escrevendo a string formatada no arquivo
```
with open("dados.txt", "w") as ler:
    ler.write(linha)
```
Explicação:

' '.join(map(str, inserir)):
map(str, inserir): Converte cada elemento da lista inserir em uma string.
' '.join(...): Junta as strings resultantes em uma única string, separando-as com espaços.
ler.write(linha): Escreve a string formatada no arquivo de texto.
Código Completo:

```
inserir = [3, 2, 6, 4, 8, 7]
```
# Imprimindo na horizontal no console
```
for x in inserir:
    print(x, end=' ')
print()
```
# Escrevendo na horizontal no arquivo de texto
```
linha = ' '.join(map(str, inserir))
with open("dados.txt", "w") as ler:
    ler.write(linha)
    ```
Com essas alterações, a saída no console e no arquivo de texto será uma única linha com os elementos da lista separados por espaços.
