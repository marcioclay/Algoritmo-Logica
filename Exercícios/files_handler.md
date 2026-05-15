Lista de exercícios — Manipulação de arquivos com open e with (Python)

Cadastro de nomes em arquivo

Crie um programa que solicite ao usuário 5 nomes e grave cada nome em uma linha no arquivo nomes.txt.
Depois, abra o arquivo e exiba todos os nomes cadastrados.

Contador de linhas

Crie um programa que abra o arquivo frases.txt e informe:

Quantas linhas existem no arquivo;
Qual a primeira linha;
Qual a última linha.

Filtro de palavras

Leia o arquivo texto.txt e mostre somente as linhas que contenham a palavra "Python".

Arquivo de notas

Crie um programa que permita registrar nome e nota de 5 alunos no arquivo notas.txt no formato:

João;8.5
Maria;9.0

Depois leia o arquivo e mostre:

Nome do aluno;
Nota;
Média geral da turma.

Separador de pares e ímpares

Crie um programa que grave números digitados pelo usuário em numeros.txt.
Depois leia o arquivo e crie:

pares.txt
impares.txt

Separando corretamente os números.

Busca em arquivo

Crie um programa que abra clientes.txt, solicite um nome e verifique se esse nome está cadastrado no arquivo.
Exiba:

"Cliente encontrado"
"Cliente não encontrado"

Remoção de registro

Crie um programa que leia produtos.txt, solicite o nome de um produto e remova esse item do arquivo.
(Dica: ler tudo, guardar em lista e reescrever o arquivo).

Ordenação

Leia o arquivo nomes.txt, ordene os nomes em ordem alfabética e grave o resultado em ordenado.txt.

Estatísticas do arquivo

Crie um programa que abra texto.txt e informe:

Quantidade de linhas;
Quantidade total de palavras;
Quantidade de caracteres;
Palavra com maior tamanho.

Mini sistema de diário

Crie um programa com menu:

1 → Adicionar anotação
2 → Listar anotações
3 → Buscar palavra
4 → Sair

Todas as anotações devem ser armazenadas em diario.txt usando with open().

Desafio (mais próximo de projeto)

CRUD de arquivo texto

Crie um sistema de cadastro de alunos usando arquivo alunos.txt, com menu:

Cadastrar aluno
Listar alunos
Buscar aluno
Excluir aluno
Sair

Cada registro deve conter:

nome;idade;curso

Utilizar obrigatoriamente with open().
