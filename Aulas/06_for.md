## Laço For
### 1. Introdução
Enquanto o while é baseado em uma condição aberta (executa enquanto algo for verdadeiro), o for é utilizado quando queremos percorrer uma sequência de dados (uma lista, uma string ou um intervalo de números).

Na computação, chamamos isso de Iteração. O for é a ferramenta ideal quando já sabemos, de antemão, quantas vezes o código deve ser executado ou quais itens precisamos processar.

### 2. Funcionamento Lógico
O for funciona como um "percorredor" automático:

Ele aponta para o primeiro item da coleção.

Executa o bloco de código usando esse item.

Passa para o próximo item automaticamente.

Quando não houver mais itens na lista, o loop encerra.

### 3. A Função range()
No Python, o for é frequentemente usado com a função range(), que gera uma sequência de números.
```
range(5): Gera (0, 1, 2, 3, 4)

range(1, 6): Gera (1, 2, 3, 4, 5)
```

### 4. Exemplo Prático 01: Tabuada Simples
Vamos criar um código que exibe a tabuada do número 5 de forma automática.

```
numero = 5

print(f"Tabuada do {numero}:")
```
### O range(1, 11) vai de 1 até 10
```
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("Fim da tabuada!")
```
Por que usar o for aqui?
Sabemos exatamente que a tabuada vai de 1 a 10.

Não precisamos gerenciar o incremento (como o i += 1 no while); o for faz isso sozinho a cada volta.

### 5. Exemplo Prático 02: Percorrendo Listas
Imagine que temos uma lista de nomes de computadores em uma rede e precisamos listar cada um deles.

```
servidores = ["Servidor-Web", "Banco-Dados", "DNS-Primario", "Firewall"]

print("Relatório de Ativos de Rede:")

for s in servidores:
    print(f"Verificando status do host: {s}...")

print("Verificação concluída.")
```
### 6. Diferença Crucial: while vs for

<img width="690" height="261" alt="image" src="https://github.com/user-attachments/assets/1cba5e9f-89ee-4a51-a6a1-9a290a38f6d1" /> 

### 7. Desafio para a Turma 🚀
Crie um script que receba uma palavra do usuário e use o for para imprimir cada letra dessa palavra em uma linha separada.
Bônus: Tente contar quantas letras a palavra possui dentro do mesmo loop.



