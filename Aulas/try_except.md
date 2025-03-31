## Try e Except: Seu Escudo Contra Erros em Python

Imagine que você está cozinhando. Você segue uma receita, mas às vezes algo dá errado: você queima a comida, derruba sal em excesso ou esquece um ingrediente. 
Em vez de desistir, você tenta consertar o que deu errado, certo?

Em Python, o try e except funcionam como um escudo contra esses "erros de cozinha". Eles permitem que seu programa tente executar um bloco de código (o try) e, se algo der errado, em vez de "quebrar" e parar, ele pode "consertar" o erro (o except).

## Como funciona:

### Tente (try): Você coloca o código que pode dar errado dentro de um bloco try.
### Exceção (except): Se um erro ocorrer dentro do bloco try, o Python "pula" para o bloco except correspondente ao tipo de erro.
Lide com o erro: Dentro do bloco except, você escreve o código para lidar com o erro, seja exibindo uma mensagem, tentando novamente ou fazendo outra coisa.
Exemplos:

Divisão por zero:
```
num1 = 10
num2 = 0

try:
    resultado = num1 / num2  # Isso causará um erro (ZeroDivisionError)
    print(resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
```

Neste exemplo, o programa tenta dividir num1 por num2, mas isso causa um erro porque num2 é zero.
O bloco except ZeroDivisionError captura esse erro e exibe uma mensagem amigável.
Entrada inválida:
```
try:
    idade = int(input("Digite sua idade: "))  # Se o usuário digitar "abc", isso causará um erro
    print(f"Sua idade é {idade}.")
except ValueError:
    print("Por favor, digite um número inteiro.")
```

O programa tenta converter a entrada do usuário em um número inteiro.
Se o usuário digitar algo que não seja um número, o bloco except ValueError captura o erro e exibe uma mensagem de erro.

Por que usar try e except?

Evitar que o programa quebre: Eles impedem que erros inesperados interrompam a execução do seu programa.
Melhorar a experiência do usuário: Eles permitem que você exiba mensagens de erro amigáveis em vez de mensagens de erro técnicas.
Tornar o código mais robusto: Eles permitem que você lide com erros de forma controlada, tornando seu programa mais confiável.
Em resumo:

Pense no try e except como um cinto de segurança para o seu código. Eles não impedem que os erros aconteçam, mas garantem que seu programa possa lidar com eles de forma segura e continuar funcionando.
