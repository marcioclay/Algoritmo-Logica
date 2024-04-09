# Funções Python

![image](https://github.com/marcioclay/Algoritmo-Logica/assets/48799029/80cab893-b4e5-4816-8df6-c5df225a0c9a)


### Aprenda o básico das funções Python, como definir e usar suas próprias funções.

Ao escrever um programa, muitas vezes precisamos repetir o mesmo código várias vezes para entradas diferentes. Para evitar duplicação, o Python permite que você chame uma função pré-determinada para aproveitar o código que ela contém. As funções ajudam a reduzir a quantidade de linhas em um código, facilitam o processo de depuração e permitem criar programas mais legíveis e fáceis de manter.


### O que são funções Python e para que servem?

Sendo estruturas essenciais do código, as funções permitem definir um bloco de código reutilizável que pode ser executado muitas vezes dentro de um programa. É uma estrutura que agrupa partes do código, criando soluções modulares para problemas complexos.

As funções em Python cumprem objetivos específicos definidos pelo usuário ou pela linguagem. Eles recebem como parâmetros dados de entrada chamados argumentos que são indicados pelo usuário ou automaticamente, sendo processados e retornando como dados de saída.

#### As funções Python servem para:

- Dividir e classificar o código em partes mais simples para depurar e programar com maior facilidade.
- Reutilizar o código, evitando repetições desnecessárias em um programa.

### Tipos de funções em Python 

Podemos distinguir dois tipos de funções:

- Nativas (Built-in functions): opções disponíveis que já estão integradas no Python.
- Personalizadas: criadas pelo usuário. Para usá-las, você precisa definir as funções que atendam às necessidades do seu projeto.
  
Veja alguns exemplos das funções nativas mais comumente usadas de Python para processar dados textuais e numéricos. Ao chamar uma função, indicamos somente os valores com os quais ela vai operar:

```
# print() mostra o argumento na tela&nbsp;
print ("Oi")
Oi
# len() determina a quantidade de caracteres em uma cadeia deles.
len("Oi Python")
11
# range() cria um intervalo de números.
# list() cria uma lista a partir de um elemento.
x = range (5)
print (list(x))
[0, 1, 2, 3, 4]
# max() determina o valor máximo entre um grupo de números.
x = [0, 1, 2]
print (max(x))
2
# min() determina o valor mínimo entre um grupo de números.
x = [0, 1, 2]
print (min(x))
0
# sum() soma o total de uma lista de números.
x = [0, 1, 2]
print (sum(x))
3
```

Em seguida, veja como criar e chamar suas próprias funções.

### Como definir uma função em Python?

Uma função é declarada usando a seguinte sintaxe:

```
def nome (parâmetro):
  bloco de código
  return
```

1. Para criar uma nova função em Python, a palavra reservada def é utilizada.
2. Em seguida, é atribuído um nome ao identificador que será usado para chamá-la.
3. Depois do nome, uma lista opcional de parâmetros é incluída entre parênteses.
4. O cabeçalho da função termina com dois pontos.
5. Nas linhas seguintes, com uma indentação maior vem o corpo da função, ou seja, uma sequência de sentenças que executam uma operação.
6. Por último, opcionalmente, é adicionada a palavra reservada return para devolver um resultado.

Uma vez que a função é definida, você pode reutilizá-la várias vezes no seu programa.

Agora, como exemplo, podemos criar uma função simples de soma com dois parâmetros:
```
def soma(a, b):
  resultado = a + b
  return resultado
```

Para obter o resultado, chamamos a função digitando seu nome. Indicamos argumentos para parâmetros entre parêntesis e solicitamos “imprimir” para observar o resultado na tela:

```
print(soma(3,7))
10
```
### Como uma função é usada ou chamada?

Esta ferramenta pode ser muito útil e permite a criação de módulos de soluções prontos para usar a qualquer momento. Veja mais exemplos de uso das funções e quais possibilidades elas oferecem.

### A função a seguir não requer argumentos ou retorno:

```	
def bem-vindo():
  print("Bem-vindo ao Python!")
```

### Para aplicar a função que acabamos de definir, basta chamar seu nome.

```	
bem-vindo()
Bem-vindo ao Python!
```
### Se adicionarmos um parâmetro à função, ao chamá-la teremos que inserir um argumento:

```
def bem-vindo(nome):
  print("Bem-vindo ao Python " + nome + "!")

bem-vindo ("Pedro")
Bem-vindo ao Python Pedro!
```
### Se houver vários argumentos, podemos adicioná-los de duas formas:

Posicional: Os argumentos são adicionados na mesma ordem em que aparecem os parâmetros correspondentes na definição da função.
Nomeado: Independente da ordem, é especificado o nome do parâmetro ao qual se associa um argumento.

```
def bem-vindo(nome, sobrenome):
  print("Bem-vindo ao Python " + nome, sobrenome + "!")

bem-vindo("Pedro", "Lopes")
- Bem-vindo ao Python Pedro Lopes!
bem-vindo(sobrenome="Lopes", nome="Pedro")
- Bem-vindo ao Python Pedro Lopes!
```
A cada parâmetro pode ser atribuído um argumento padrão. Se a função for chamada sem atribuir um argumento a esse parâmetro, será utilizado um argumento padrão.

```
def bem-vindo(nome, idioma = "Python"):
  print("Bem-vindo ao " + idioma, nome + "!")

bem-vindo("Josh")
- Bem-vindo ao Python Josh!
bem-vindo("Josh", "Java")
- Bem-vindo ao Java Josh!
```
Às vezes, você precisa criar uma função com uma série de argumentos indeterminados para um parâmetro. Para fazer isso, colocamos um asterisco antes do nome do parâmetro e, ao chamarmos a função, adicionamos argumentos separados por vírgulas.

```
def cumprimento (*nomes):
  for nome in nomes:
    print(“Oi " + nome + "!")

cumprimento ("Paulo", "Monica", "Josh")
Oi Paulo!
Oi Monica!
Oi Josh!
```

### Quando uma função é definida para realizar um cálculo, por exemplo, e precisamos dela para retornar um valor, é usada a instrução return:

```
def quadrado (x):
  quadrado = x ** 2
  return quadrado

print (quadrado (5))
25
```

Se o código não tiver uma instrução de retornar o valor, a função não vai devolver nada. Se executamos a função do exemplo sem instrução, aparecerá escrito None na tela.

```	
def quadrado (x):
  quadrado = x ** 2

print (quadrado (5))
  
None
```

O Python também permite que sejam devolvidos vários valores:

```
def quadrado_e_cubo (x):
  quadrado = x ** 2
  cubo = x ** 3
  return quadrado, cubo
  
print (quadrado_e_cubo(5))
25, 125
```

As funções definidas não podem estar vazias. Mas, se por algum motivo, você tiver uma definição de função sem conteúdo e se quiser reservá-la para mais tarde, adicione a instrução pass para evitar um erro.

```	
def funcao_reservada():
  pass
```

As funções têm várias vantagens:

- Ao criar uma nova função, você define um bloco de instruções para fazer com que o seu programa seja mais fácil de ler, entender e depurar.
- As funções ajudam a reduzir linhas repetitivas. Elas permitem que você escreva o código apenas uma vez.
- Ao dividir um programa longo em funções, você pode revisá-lo e depurá-lo por partes antes de montar um código inteiro.
- As funções bem projetadas podem servir para muitos programas. Tendo escrito uma vez, você pode reutilizar a função quando quiser.  













