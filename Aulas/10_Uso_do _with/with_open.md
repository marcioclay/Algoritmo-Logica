# 📝 Manipulação de Arquivos TXT em Python: O Guia Definitivo com `open` e `with`

Bem-vindo ao guia prático sobre manipulação de arquivos de texto (`.txt`) em Python. Este material foi desenvolvido especialmente para alunos iniciantes aprenderem a interagir com arquivos de forma segura, moderna e eficiente.

---

## 1. O Conceito Base: `open()` vs `with open()`

Para mexer em qualquer arquivo, o Python precisa "abrir uma porta" até ele. No entanto, existem duas formas de fazer isso:

* **O jeito antigo (`open`)**: Você abre o arquivo, faz o que precisa e **obrigatoriamente** precisa fechar a porta com `.close()`. Se o seu programa der um erro antes de fechar, o arquivo pode ser corrompido ou travar o sistema.
* **O jeito moderno (`with open`)**: Ele abre o arquivo e garante que a porta será fechada automaticamente assim que o bloco de código terminar, mesmo se ocorrer um erro. **Esse é o padrão de mercado e o que utilizaremos.**

### Os Modos de Abertura Mais Comuns:
* `'r'` (*Read*): Abre para **ler** (padrão). O arquivo já deve existir.
* `'w'` (*Write*): Abre para **escrever**. Se o arquivo já existir, ele apaga tudo o que está dentro e cria um novo do zero.
* `'a'` (*Append*): Abre para **adicionar** conteúdo ao final do arquivo, sem apagar o que já existe.

---

## 2. Na Prática: Criando e Adicionando Dados (Incluir)

Vamos simular a criação de um arquivo chamado `alunos.txt` para salvar nomes.

### 🔹 Exemplo 1: Escrevendo do zero (`'w'`)
```python
# Criando o arquivo e adicionando as primeiras linhas
with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Bruno\n")

print("Arquivo criado com sucesso!")
```
> **Nota de Aula:** O `\n` serve para pular uma linha, garantindo que o próximo nome não fique colado no anterior.

### 🔹 Exemplo 2: Adicionando novos dados sem apagar os antigos (`'a'`)
Se usássemos `'w'` de novo, a Ana e o Bruno sumiriam. Para apenas **incluir** a Carla, usamos o modo de adição (`'a'`):
```python
# Adicionando um novo aluno ao final do arquivo
with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Carla\n")

print("Carla adicionada!")
```

---

## 3. Pesquisando Dados no Arquivo (Pesquisar)

Para buscar um nome, abrimos o arquivo no modo de leitura (`'r'`) e usamos um laço `for` para percorrer o arquivo linha por linha de forma eficiente.

```python
termo_busca = "Bruno"
encontrado = False

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # .strip() remove espaços em branco e o '\n' do final da linha
        if linha.strip() == termo_busca:
            encontrado = True
            break

if encontrado:
    print(f"O aluno '{termo_busca}' está na lista!")
else:
    print(f"O aluno '{termo_busca}' NÃO foi encontrado.")
```

---

## 4. Pesquisando Dados em Colunas

Muitas vezes, os arquivos guardam informações organizadas em colunas, separadas por vírgulas (formato CSV), espaços ou pontos e vírgulas. 

Imagine que nosso arquivo se chama `dados_alunos.txt` e possui a seguinte estrutura:
```text
ID,Nome,Idade
1,Ana,20
2,Bruno,22
3,Carla,19
```

Para pesquisar apenas na coluna **Nome**, usamos o método `.split(",")` para dividir o texto da linha em uma lista de elementos:

```python
nome_procurado = "Carla"
encontrado = False

with open("dados_alunos.txt", "r", encoding="utf-8") as arquivo:
    # Lendo a primeira linha (cabeçalho) para ignorá-la na pesquisa
    cabecalho = arquivo.readline()
    
    for linha in arquivo:
        # Transforma "3,Carla,19\n" em ['3', 'Carla', '19']
        colunas = linha.strip().split(",")
        
        id_aluno = colunas[0]
        nome_aluno = colunas[1]
        idade_aluno = colunas[2]
        
        # .lower() ajuda a ignorar diferenças entre maiúsculas e minúsculas
        if nome_aluno.lower() == nome_procurado.lower():
            print(f"Encontrado! ID: {id_aluno} | Nome: {nome_aluno} | Idade: {idade_aluno}")
            encontrado = True
            break

if not encontrado:
    print("Aluno não cadastrado.")
```

---

## 5. Como "Excluir" um Dado do Arquivo

Diferente de um banco de dados, arquivos de texto não possuem um comando direto para "deletar uma linha específica". O truque lógico que fazemos na programação é:
1. Ler o arquivo original por completo.
2. Salvar na memória (em uma lista) apenas as linhas que **não** queremos deletar.
3. Sobrescrever o arquivo original usando `'w'` apenas com as linhas que restaram.

Vamos excluir o "Bruno" do nosso arquivo `alunos.txt`:

```python
nome_para_excluir = "Bruno"
linhas_salvas = []

# Passo 1: Ler e filtrar os dados
with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # Se a linha NÃO for o Bruno, nós a guardamos
        if linha.strip() != nome_para_excluir:
            linhas_salvas.append(linha)

# Passo 2: Sobrescrever o arquivo com a nova lista (sem o Bruno)
with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas_salvas)

print(f"'{nome_para_excluir}' foi removido com sucesso!")
```

---

## 💡 Resumo Teórico para Fixação

| Função / Modo | O que faz? | Quando usar? |
| :---: | :--- | :--- |
| **`with open(...)`** | Garante abertura e fechamento seguro do arquivo. | Sempre! É a melhor prática de mercado. |
| **`'w'`** | Escreve do zero. Apaga o que existir antes. | Para criar novos arquivos ou resetar dados. |
| **`'a'`** | Adiciona conteúdo ao final do arquivo. | Para cadastrar ou incluir novos registros. |
| **`'r'`** | Abre o arquivo estritamente para leitura. | Para buscar, exibir ou processar dados existentes. |
| **`.split()`** | Quebra uma String baseado em um caractere. | Para ler dados organizados em colunas. |

---

## ✏️ Desafio Prático Proneposto

Crie um sistema de dicionário simples: um arquivo chamado `dicionario.txt` com o formato estruturado por colunas `Palavra;Significado`.

Desenvolva um menu interativo no terminal onde o usuário possa escolher:
1. **Incluir** uma nova palavra e seu significado.
2. **Pesquisar** o significado de uma palavra específica.
3. **Excluir** uma palavra do dicionário.
