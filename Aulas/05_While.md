## Aula: Estruturas de Repetição - O Laço while

### 1. Introdução
Na programação, muitas vezes precisamos que um bloco de código seja executado várias vezes até que uma condição seja atendida. Em vez de escrever o mesmo código repetidamente, utilizamos Estruturas de Repetição (ou loops).

O while (que significa enquanto) é uma das estruturas mais fundamentais. Ele executa um bloco de instruções enquanto uma condição específica for verdadeira.

### 2. Funcionamento Lógico
O while funciona como um "filtro" de entrada:

O programa chega na linha do while.

Ele verifica se a condição é Verdadeira (True).

Se for, ele entra no bloco e executa os comandos.

Ao final do bloco, ele volta para o topo e testa a condição novamente.

Se a condição for Falsa (False), o loop encerra e o programa segue para a próxima linha fora do bloco.

<img width="3000" height="3000" alt="image" src="https://github.com/user-attachments/assets/b308c31e-e12e-4ad0-91e5-5f34780aeffa" /> 

### 3. Sintaxe (Exemplo em Python)
A estrutura básica em Python segue este padrão:

```
while condicao:
    # Bloco de código que será repetido
    # Importante: algo aqui deve alterar a condição!
```
### 4. Exemplo Prático 01: Contador Simples
Imagine que precisamos imprimir os números de 1 a 5 no console.

```
contador = 1

while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # Incremento: essencial para não criar um loop infinito

print("Loop finalizado!")
```

Explicação do código:
Inicialização: Criamos a variável contador começando em 1.

Condição: O loop continuará enquanto contador for menor ou igual a 5.

Corpo: Imprime o valor atual.

Atualização: Somamos 1 ao contador (contador += 1). Sem isso, o contador seria sempre 1, a condição seria sempre verdadeira, e o programa nunca pararia (Loop Infinito).

### 5. Exemplo Prático 02: Validação de Dados
O while é excelente para forçar o usuário a digitar um dado correto. Por exemplo, um sistema que só aceita notas entre 0 e 10.

```
nota = float(input("Digite uma nota (0 a 10): "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("Por favor, digite uma nota válida entre 0 e 10: "))

print(f"Nota {nota} registrada com sucesso!")
```
### 6. Desafio para a Turma 🚀
Crie um pequeno script onde o usuário deve adivinhar um "número secreto" (ex: 7). O programa deve continuar pedindo o número até que o usuário acerte. Quando acertar, exiba uma mensagem de parabéns.

Dica de Ouro: Sempre verifique se a sua condição de parada eventualmente se tornará falsa, para evitar que o computador trave processando um loop infinito!
