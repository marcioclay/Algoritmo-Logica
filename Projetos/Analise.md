# ATIVIDADE PRÁTICA – ENGENHARIA REVERSA DE CÓDIGO COM IA

**Disciplina:**   
**Tema:** Análise, interpretação e correção de código  

## 1. Contextualização

Uma empresa solicitou a criação de um pequeno sistema para cadastrar e consultar tarefas.

O sistema foi desenvolvido com auxílio de uma Inteligência Artificial. Entretanto, durante os testes, foram identificados alguns problemas no funcionamento do programa.

Sua missão será atuar como um programador responsável pela análise desse sistema.

Você deverá compreender o código, identificar os problemas, corrigir os erros e demonstrar que entende o funcionamento do programa.

**Atenção:** Você poderá utilizar ferramentas de Inteligência Artificial para auxiliar na atividade, mas deverá compreender e explicar todas as alterações realizadas.

## 2. Objetivo

Desenvolver habilidades de interpretação de código Python, identificação de erros e resolução de problemas.

## 3. Código fornecido

O programa abaixo possui alguns erros intencionais.

Copie o código para o VS Code ou Pycharm e salve com o nome `tarefas.py`.

```python
opcao = -1

while opcao != 0:

    print("\n===== MENU DE TAREFAS =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        tarefa = input("Digite a tarefa: ")

        arquivo = open("tarefas.txt", "w")
        arquivo.write(tarefa)
        arquivo.close()

        print("Tarefa cadastrada!")

    elif opcao == 2:

        arquivo = open("tarefas.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

        print("\n===== LISTA DE TAREFAS =====")

        for tarefa in linhas:
            print(tarefa)

    elif opcao == 0:

        print("Programa encerrado!")

    else:

        print("Opção inválida!")
```

## 4. Organização dos arquivos

Crie uma pasta chamada `atividade_engenharia_reversa`.

Dentro dela, organize os arquivos:

```text
atividade_engenharia_reversa/
│
├── tarefas.py
│
└── tarefas.txt
```

O arquivo `tarefas.txt` deverá começar vazio.

## 5. Etapas da atividade

### Etapa 1 – Investigação

Execute o programa e realize os seguintes testes:

1. Cadastre uma tarefa chamada "Estudar Python".
2. Cadastre outra tarefa chamada "Fazer exercícios".
3. Escolha a opção de listar tarefas.
4. Observe o resultado apresentado.

Registre o comportamento encontrado.

### Etapa 2 – Engenharia reversa

Analise o código e responda:

1. Qual é a finalidade da variável `opcao`?
2. Para que serve o comando `while`?
3. O que acontece quando o usuário escolhe a opção 1?
4. Qual é a finalidade do comando `open()`?
5. Qual é a diferença entre os modos `"r"` e `"w"`?
6. Para que serve o comando `readlines()`?
7. Qual é a função do comando `close()`?

### Etapa 3 – Identificação dos erros

O programa apresenta problemas durante seu funcionamento.

1. Identifique pelo menos dois problemas no código.
2. Explique por que esses problemas acontecem.
3. Indique quais linhas precisam ser modificadas.

### Etapa 4 – Correção

Corrija o programa para que:

1. Seja possível cadastrar várias tarefas.
2. As tarefas anteriores não sejam apagadas ao cadastrar uma nova.
3. Cada tarefa apareça em uma linha diferente.
4. A opção de listagem apresente todas as tarefas cadastradas.

### Etapa 5 – Desafio individual

Implemente uma nova opção no menu:

**3 - Quantidade de tarefas cadastradas**

Ao selecionar essa opção, o programa deverá informar quantas tarefas estão registradas no arquivo `tarefas.txt`.

## 6. Utilização da Inteligência Artificial

Você poderá utilizar ChatGPT, Gemini ou outra ferramenta de IA.

Entretanto, deverá registrar:

1. Qual ferramenta de IA utilizou?
2. Qual pergunta ou comando enviou para a IA?
3. Qual problema a IA identificou?
4. Você concordou com a solução apresentada? Justifique.
5. O que você aprendeu durante a correção?

## 7. Avaliação

| Critério | Pontuação |
|---|---:|
| Execução e investigação do programa | 1,5 |
| Identificação dos problemas | 2,0 |
| Explicação dos comandos Python | 2,0 |
| Correção do programa | 2,5 |
| Desafio individual | 1,0 |
| Defesa técnica individual | 1,0 |
| **Total** | **10,0** |

## 8. Entrega

O aluno deverá entregar:

- Arquivo `tarefas.py` corrigido.
- Arquivo `tarefas.txt` utilizado nos testes.
- Respostas das perguntas da atividade.
- Registro da utilização da Inteligência Artificial.

**Importante:** O professor poderá solicitar que o aluno explique qualquer parte do código e realize uma alteração durante a aula.
