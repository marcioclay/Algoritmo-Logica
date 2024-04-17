# Função Range

Explicando o range(len(idades) - 1, -1, -1) em Python

Objetivo:

Desvendar os segredos do range(len(idades) - 1, -1, -1) em Python, revelando passo a passo como ele opera e quais resultados gera.

Cenário:

Imagine que você possui uma lista chamada idades com 5 elementos, representando as idades de 5 pessoas. Deseja iterar por essa lista na ordem inversa, imprimindo as idades das pessoas do mais velho para o mais novo.

O range é uma função mágica em Python que gera sequências de números. Com ele, você pode controlar quais números serão utilizados em loops, definindo o início, o fim e o incremento da sequência.

Desvendando:

len(idades) - 1:

A função len() retorna a quantidade de elementos na lista idades.
Subtraímos 1 desse valor para obter o índice do último elemento da lista.
Por exemplo, se a lista tiver 5 elementos, len(idades) - 1 será 4, representando o índice do último elemento (4).
-1:

Define o limite inferior da sequência.
Neste caso, como queremos iterar na ordem inversa, o limite inferior deve ser menor que o ponto de partida.
-1:

Define o incremento da sequência.
Um valor negativo indica que a sequência deve ser decrementada.
Ou seja, a cada iteração, o valor do índice será diminuído em 1.
Conjurando a Sequência:

Ao combinar esses elementos no range(), obtemos a seguinte sequência:

[4, 3, 2, 1, 0]
O Resultado Mágico:

Ao utilizar essa sequência em um loop for, iteramos pela lista idades na ordem inversa:

```
for indice in range(len(idades) - 1, -1, -1):
  print(f"Idade: {idades[indice]}")
```

Se a lista idades contém:

[30, 25, 22, 18, 15]
A impressão será:

Idade: 30
Idade: 25
Idade: 22
Idade: 18
Idade: 15
Observações:

O range() é versátil e pode ser utilizado para gerar sequências com diversos padrões.
Explore a documentação oficial do Python para descobrir mais sobre seus recursos: http://python-reference.readthedocs.io/en/latest/docs/functions/range.html
Combine o range() com loops for para realizar tarefas complexas e iterar por diferentes tipos de dados.
