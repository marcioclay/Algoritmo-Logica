# O Conceito Básico em 2 Passos

Imagine que você tem dois arquivos salvos na **mesma pasta** do seu computador:

```text
📁 meu_projeto/
├── minhas_funcoes.py   # Onde guardamos a ferramenta
└── principal.py        # Onde vamos usar a ferramenta
```

## Passo 1: Crie o arquivo com a função (`minhas_funcoes.py`)

Neste arquivo, você apenas define a função que deseja reutilizar.

```python
# Arquivo: minhas_funcoes.py

def saudar_aluno(nome):
    return f"Olá, {nome}! Seja bem-vindo à aula de Python."
```

## Passo 2: Importe e use no arquivo principal (`principal.py`)

No arquivo principal, você usa o comando `from ... import ...` para buscar a função criada no outro arquivo.

### Forma recomendada: importar uma função específica

```python
# Arquivo: principal.py

# Do arquivo minhas_funcoes, importe a função saudar_aluno.
from minhas_funcoes import saudar_aluno

# Agora você pode usar a função normalmente!
mensagem = saudar_aluno("Maria")
print(mensagem)
```

**Saída esperada:**

```text
Olá, Maria! Seja bem-vindo à aula de Python.
```

### Outra forma comum: importar o arquivo inteiro

Você também pode importar o arquivo inteiro. A diferença é que precisará colocar o nome do arquivo antes da função ao chamá-la.

```python
# Arquivo: principal.py

import minhas_funcoes

# Usando: nome_do_arquivo.nome_da_funcao()
mensagem = minhas_funcoes.saudar_aluno("João")
print(mensagem)
```

**Saída esperada:**

```text
Olá, João! Seja bem-vindo à aula de Python.
```

## ⚠️ Regra de Ouro 

Para o Python encontrar a função sem gerar o erro `ModuleNotFoundError`, **os dois arquivos `.py` devem estar salvos na mesma pasta**, neste exemplo.

Além disso, execute o arquivo `principal.py` e confira se o nome do arquivo importado está correto, sem a extensão `.py`.

