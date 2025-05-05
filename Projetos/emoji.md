## Como usar emoji no print 

Usando caracteres Unicode

Unicode é um sistema padrão para codificação e representação de texto em diferentes idiomas e sistemas de escrita. O Unicode também inclui uma variedade de símbolos e ícones, como emojis. Você pode encontrar uma lista de emojis Unicode aqui:
```
https://unicode.org/emoji/charts/full-emoji-list.html
```
Para imprimir um emoji em Python usando Unicode, você precisa saber seu ponto de código, que é um número hexadecimal que identifica o caractere. Por exemplo, o ponto de código para o emoji de rosto sorridente é U+1F600. Você pode escrever esse ponto de código em Python usando o formato \Uxxxxxxxx, onde xxxxxxxx é o número hexadecimal de 8 dígitos. Por exemplo:

imprimir(“\U0001F600”).

Isso imprimirá 😀 na sua tela.

Substitua o "+" por 3x "0".


Você também pode usar o formato \uxxxx para números hexadecimais de 4 dígitos, como \u263A para ☺.

