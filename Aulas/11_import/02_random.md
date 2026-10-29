### A biblioteca random do Python serve para gerar números e escolhas aleatórias em seus programas. Ela já vem instalada com o Python, então você não precisa baixar nada para começar a usar.
Para utilizá-la, a primeira coisa que você deve fazer no seu código é importá-la:

```
import random
```


📌 As 4 Funções Mais Usadas (Com Exemplos)

Aqui estão as ferramentas básicas que você mais vai usar no dia a dia:

1. random.randint(início, fim)

Gera um número inteiro aleatório dentro do intervalo que você escolher (incluindo os números dos extremos).
• Exemplo prático: Simular o lançamento de um dado de 6 lados. 

```
dado = random.randint(1, 6)
print(dado)  # Pode exibir 1, 2, 3, 4, 5 ou 6
```


2. random.choice(lista)

Escolhe de forma aleatória um único elemento de dentro de uma lista.
• Exemplo prático: Decidir o que comer no almoço. 

```
opcoes = ["Pizza", "Hambúrguer", "Salada", "Sushi"]
almoco = random.choice(opcoes)
print(almoco)  # Sorteia um dos pratos
```


3. random.shuffle(lista)

Embaralha os elementos de uma lista original diretamente, mudando a ordem deles.
• Exemplo prático: Misturar as cartas de um baralho. 

```
cartas = ["Ás", "Rei", "Rainha", "Valete"]
random.shuffle(cartas)
print(cartas)  # Exibe a mesma lista, mas com a ordem toda bagunçada
```


4. random.random()

Gera um número decimal (float) aleatório entre 0.0 (inclusive) e 1.0 (exclusive). Ele não recebe nenhum argumento nos parênteses. 

```
numero_decimal = random.random()
print(numero_decimal)  # Exemplo de saída: 0.4729183
```



