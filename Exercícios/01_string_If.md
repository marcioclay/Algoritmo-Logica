# Exercícios de Python

## Bloco 1: Variáveis, Tipos de Dados e Métodos de String

### Exercício 1: Formatador de Nome
Crie um programa que receba o nome do usuário contendo espaços extras nas pontas (ex: `"   João Silva   "`).
* Remova os espaços em branco extras usando `.strip()`.
* Imprima o nome formatado em letras maiúsculas e em letras minúsculas.

### Exercício 2: Contador de Caracteres
Peça para o usuário digitar uma frase.
* Imprima o número total de caracteres da frase (incluindo espaços) usando a função `len()`.

### Exercício 3: Separador de Palavras
Solicite que o usuário digite três frutas separadas por vírgula (ex: `"maçã,banana,uva"`).
* Use o método `.split(",")` para transformar essa string em uma lista de frutas.
* Imprima a lista gerada.

### Exercício 4: Padronizador de E-mail
Solicite o e-mail do usuário. O e-mail pode conter letras maiúsculas e espaços acidentais nas pontas (ex: `"  Usuario@Email.COM  "`).
* Trate a entrada para que o e-mail fique sem espaços e inteiramente em letras minúsculas.
* Exiba o e-mail corrigido.

### Exercício 5: Análise de Texto Curto
Peça ao usuário para digitar um título de livro.
* Exiba a primeira palavra do título em maiúsculas (Dica: combine `.split()` com `.upper()`).
* Exiba o número total de caracteres do título original sem os espaços do início e do fim.

---

## Bloco 2: Condicionais Simples e Compostas (`if` e `if-else`)

### Exercício 6: Validador de Tamanho de Senha (`if` simples)
Crie um programa que solicite uma nova senha.
* Remova espaços nas extremidades da senha digitada.
* Se o tamanho da senha (usando `len()`) for menor que 8 caracteres, exiba a mensagem: `"Erro: A senha deve ter pelo menos 8 caracteres."`

### Exercício 7: Verificador de Nome de Usuário (`if-else`)
Solicite o nome de usuário para login.
* Converta a entrada para minúsculas usando `.lower()` e remova espaços extras.
* Se o nome digitado for `"admin"`, exiba `"Acesso concedido ao painel de controle."`.
* Caso contrário, exiba `"Acesso negado."`.

### Exercício 8: Filtro de Texto (`if-else`)
Peça para o usuário digitar um comentário.
* Verifique se o comentário convertido para minúsculas contém mais de 50 caracteres.
* Se sim, exiba: `"Comentário muito longo."`.
* Caso contrário, exiba: `"Comentário publicado com sucesso."`.

### Exercício 9: Checagem de Formato de Lista (`if-else`)
Peça ao usuário uma lista de itens separados por espaço.
* Divida a string em palavras usando `.split()`.
* Se a quantidade de itens for maior ou igual a 3, exiba `"Lista válida com [X] itens."` (substituindo `[X]` pela quantidade).
* Caso contrário, exiba `"Por favor, informe pelo menos 3 itens."`.

### Exercício 10: Classificador de Palavra Longa (`if-else`)
Solicite uma palavra ao usuário.
* Remova espaços nas pontas e converta a palavra para maiúsculas.
* Se a palavra tiver 10 ou mais caracteres, exiba: `"A palavra [PALAVRA] é longa."`.
* Caso contrário, exiba: `"A palavra [PALAVRA] é curta."`.

---

## Bloco 3: Condicionais Aninhadas (`if` dentro de `if`)

### Exercício 11: Validação de Cadastro de Usuário
Solicite o nome e a idade do usuário.
* Remova os espaços em branco do nome.
* **Se** o nome tiver mais de 2 caracteres:
  * **Se** a idade for maior ou igual a 18, exiba: `"Cadastro realizado com sucesso!"`.
  * **Senão**, exiba: `"Cadastro permitido apenas para maiores de idade."`.
* **Senão**, exiba: `"Nome inválido (muito curto)."`.

### Exercício 12: Sistema de Login com Duas Etapas
Peça o nome de usuário e a senha.
* Trate o nome de usuário com `.strip().lower()`.
* **Se** o usuário for igual a `"aluno"`:
  * **Se** a senha tratada com `.strip()` tiver exatamente 6 caracteres, exiba: `"Login efetuado!"`.
  * **Senão**, exiba: `"Senha incorreta (deve ter exatamente 6 caracteres)."`.
* **Senão**, exiba: `"Usuário não encontrado."`.

### Exercício 13: Analisador de Frase Completo
Solicite uma frase do usuário.
* Remova espaços nas pontas.
* **Se** a frase não estiver vazia (`len(frase) > 0`):
  * Divida a frase em palavras com `.split()`.
  * **Se** a quantidade de palavras for maior que 1, exiba a primeira palavra em letras maiúsculas e a última em letras minúsculas.
  * **Senão**, exiba: `"Você digitou apenas uma palavra."`.
* **Senão**, exiba: `"Você não digitou nenhuma frase."`.

### Exercício 14: Triagem de E-mail Corporativo
Solicite um endereço de e-mail.
* Trate o e-mail com `.strip().lower()`.
* **Se** o e-mail contiver o caractere `"@"`:
  * Separe o e-mail em duas partes usando `.split("@")`.
  * **Se** a segunda parte (o domínio) for igual a `"empresa.com"`, exiba: `"E-mail corporativo válido."`.
  * **Senão**, exiba: `"Acesso restrito a e-mails do domínio @empresa.com."`.
* **Senão**, exiba: `"Endereço de e-mail inválido."`.

### Exercício 15: Validador de Código de Desconto
Solicite um cupom de desconto digitado pelo usuário.
* Limpe espaços extras e converta o cupom para maiúsculas com `.strip().upper()`.
* **Se** o tamanho do cupom for igual a 6 caracteres:
  * **Se** o cupom começar com a palavra `"PROMO"` (ex: fatiamento `cupom[:5]`):
    * Exiba: `"Cupom de 20% aplicado com sucesso!"`.
  * **Senão**, exiba: `"Cupom inválido para esta campanha."`.
* **Senão**, exiba: `"Código de cupom deve ter exatamente 6 caracteres."`.
