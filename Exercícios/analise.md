# Atividade de Fixação


## Questão 1 – Crie um dicionário chamado notas_alunos com os seguintes dados:
```
notas_alunos = {
    "Ana": 8.5,
    "Bruno": 7.0,
    "Carlos": 9.2,
    "Diana": 6.8,
    "Eduardo": 7.5
}
```
- Pergunta: Escreva um código que:

- Mostre a nota do aluno Carlos

- Adicione um novo aluno chamado Fernanda com nota 8.0

- Imprima todos os nomes dos alunos

## Questão 2 – Usando pandas de forma básica
Transforme o dicionário notas_alunos em um DataFrame do pandas:

```
import pandas as pd

df = pd.DataFrame(list(notas_alunos.items()), columns=["Aluno", "Nota"])
```

- Pergunta (versão simplificada): Com base no DataFrame df, escreva um código que:

- Mostre todos os dados da tabela

- Exiba apenas os nomes dos alunos

 ## - Questão 3 Você já tem o dicionário notas_alunos com os dados dos alunos e suas notas:

```
notas_alunos = {
    "Ana": 8.5,
    "Bruno": 7.0,
    "Carlos": 9.2,
    "Diana": 6.8,
    "Eduardo": 7.5,
    "Fernanda": 8.0
}
```
- Transforme esse dicionário em um DataFrame chamado df:

``` 
import pandas as pd

df = pd.DataFrame(list(notas_alunos.items()), columns=["Aluno", "Nota"])
```
- Pergunta: Escreva um código que:

- Mostre apenas os alunos que tiraram nota menor que 7

Exiba a quantidade total de alunos cadastrados
