## A função input() em Python

Até agora aprendemos a utilizar a função print(), que serve para exibir informações na tela. Entretanto, muitos programas precisam receber informações digitadas pelo usuário, como nome, idade, salário ou notas.

Para isso, utilizamos a função input().

A função input() permite que o programa espere o usuário digitar uma informação pelo teclado. Após a digitação, o valor é armazenado em uma variável para ser utilizado posteriormente.

Sintaxe: 
```
variavel = input("Mensagem para o usuário: ")
``` 

A mensagem entre aspas é chamada de prompt, pois orienta o usuário sobre o que deve ser digitado. 

### 1. Lendo um texto

Vamos criar um programa que solicita o nome do usuário.
```
nome = input("Digite seu nome: ")
print(nome)
```
Exemplo de execução
```
Digite seu nome: João
João
``` 

Observe que o programa fica aguardando o usuário digitar o nome e pressionar Enter. 

### 2. Exibindo a informação digitada

Normalmente utilizamos o print() para mostrar o valor armazenado.
```
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```
Exemplo
```
Digite seu nome: Maria
Olá, Maria!
``` 
### 3. Lendo mais de uma informação

Podemos utilizar vários input() no mesmo programa.
```
nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
```
Exemplo
```
Digite seu nome: Carlos
Digite sua cidade: Vitória

Nome: Carlos
Cidade: Vitória
``` 

### 4. Atenção: o input() sempre retorna texto

Esse é um dos conceitos mais importantes para quem está começando.

Mesmo que o usuário digite um número, o Python o interpreta como texto (string).

Exemplo:
```
idade = input("Digite sua idade: ")
print(idade)
```
Se o usuário digitar:
```
18
```
O valor armazenado será:
```
"18"
```
e não o número 18.


### 5. O problema ao somar números

Observe este exemplo:
```
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print(numero1 + numero2)
```
Se o usuário digitar:
```
10
20
```
O resultado será:
```
1020
```
Isso acontece porque o Python juntou os dois textos.

### 6. Convertendo para inteiro

Quando desejamos realizar cálculos, devemos converter o texto para um número inteiro utilizando a função int().
```
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(numero1 + numero2)
```
Exemplo
```
Digite o primeiro número: 10
Digite o segundo número: 20

30
```
Agora o Python realizou uma soma matemática.

### 7. Convertendo para número decimal

Quando o valor pode possuir casas decimais, utilizamos float().
```
altura = float(input("Digite sua altura: "))
print(altura)
```

Exemplo
```
Digite sua altura: 1.75

1.75
```

### 8. Exemplo completo
```
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print()
print("===== CADASTRO =====")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} metros")
```
Exemplo de execução
```
Digite seu nome: Ana
Digite sua idade: 20
Digite sua altura: 1.68

===== CADASTRO =====
Nome: Ana
Idade: 20 anos
Altura: 1.68 metros
````


