## Lista de exercícios — Manipulação de arquivos com open e with (Python)

1. Cadastro de nomes em arquivo

2. Crie um programa que solicite ao usuário 5 nomes e grave cada nome em uma linha no arquivo nomes.txt.

3. Depois, abra o arquivo e exiba todos os nomes cadastrados.

4. Crie um programa que abra o arquivo frases.txt e informe:

- Quantas linhas existem no arquivo
- Qual a primeira linha
- Qual a última linha.

5. Filtro de palavras

- Leia o arquivo texto.txt e mostre somente as linhas que contenham a palavra "Python".


6. Crie um programa que permita registrar nome e nota de 5 alunos no arquivo notas.txt no formato:

- João;8.5
- Maria;9.0

Depois leia o arquivo e mostre:

- Nome do aluno;
- Nota;
- Média geral da turma.

7. Crie um programa que grave números digitados pelo usuário em numeros.txt.

Depois leia o arquivo e crie:

- pares.txt
- impares.txt

8. Crie um programa que abra clientes.txt, solicite um nome e verifique se esse nome está cadastrado no arquivo.

Exiba:

- "Cliente encontrado"
- "Cliente não encontrado"

---
9. Crie um programa com menu:

 → Adicionar anotação
 
 → Listar anotações
 
 → Buscar palavra
 
 → Sair

Todas as anotações devem ser armazenadas em diario.txt usando with open().

---
10. Desafio (mais próximo de projeto)

CRUD de arquivo texto

Crie um sistema de cadastro de alunos usando arquivo alunos.txt, com menu:

- Cadastrar aluno
- Listar alunos
- Buscar aluno
- Excluir aluno
- Sair

- Cada registro deve conter:
nome;idade;curso

Utilizar obrigatoriamente with open().
