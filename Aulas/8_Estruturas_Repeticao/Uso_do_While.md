## O Laço de Repetição while

## 1. O que é e para que serve o while?
A palavra while significa "enquanto". Usamos o laço while quando queremos que o Python repita um bloco de código enquanto uma condição for verdadeira (True).
A grande diferença entre o for e o while é: 

- for: Usado quando sabemos exatamente quantas vezes queremos repetir algo (ou quando percorremos uma lista pronta).
- while: Usado quando não sabemos quantas vezes a repetição vai acontecer, pois depende de algo mudar no decorrer do programa (uma senha digitada pelo usuário, um valor atingido, etc.).
  
Analogia da vida real: 
- Enquanto você estiver com fome $\rightarrow$ continue comendo. 
- Enquanto a bateria do celular for menor que $100\%$ $\rightarrow$ continue carregando.

## 2. A Anatomia do while (Sintaxe)

Para que um while funcione corretamente sem travar o computador, ele precisa de 3 passos fundamentais:
```
  ### 1. Inicialização da variável de controle
  
  contador = 1  
   
  ### 2. Teste da condição
  
  while contador <= 5:  
      print(f"Número: {contador}")
   
  ### 3. Atualização (passo essencial!)
  
      contador = contador + 1  
  ```

O que acontece em cada passo:
- Inicialização: Criamos uma variável antes de começar o laço para acompanhar o estado da repetição.
- Teste: O Python verifica se a condição é True. Se for, executa o bloco interno.
- Atualização: Alteramos o valor da variável de controle dentro do laço. Sem isso, a condição nunca mudará!

## 3. Praticando com Exemplos

Exemplo 1: Repetição com Contagem Simples
```
x = 1

while x <= 3:
    print(f"Executando a volta número {x}")
    x += 1  # Mesma coisa que: x = x + 1

print("Fim da repetição!")
```

Saída no terminal:
```
Executando a volta número 1
Executando a volta número 2
Executando a volta número 3
Fim da repetição!
```

Exemplo 2: Validando uma Senha (Repetição Indeterminada)
Não sabemos quantas vezes o usuário vai errar a senha antes de acertar. 
Por isso, o while é ideal aqui:
```
senha_correta = "1234"
senha_digitada = input("Digite a senha de acesso: ")

while senha_digitada != senha_correta:
    print("❌ Senha incorreta! Tente novamente.")
    senha_digitada = input("Digite a senha de acesso: ")

print("🔓 Acesso liberado com sucesso!")
```
Exemplo 3: Menu Interativo com break
A instrução break serve para interromper e fechar o laço while imediatamente, independentemente da condição.

```
while True:
    print("\n--- MENU ---")
    print("1. Ver saldo")
    print("2. Fazer depósito")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "3":
        print("Saindo do sistema...")
        break  # Interrompe o loop infinito na hora
    elif opcao == "1":
        print("Seu saldo é R$ 1.000,00")
    elif opcao == "2":
        print("Depósito realizado!")
    else:
        print("Opção inválida!")
```


## ⚠️ Perigo: O Loop Infinito! 
Se você esquecer de atualizar a variável de controle, a condição será sempre verdadeira, e o programa ficará preso em um loop infinito até travar.
```
# ERRO ❌ (Faltou atualizar o contador)
contador = 1

while contador <= 5:
    print(contador)
    # Faltou a linha: contador += 1
    # O Python vai imprimir '1' para sempre!
```

##📝 Exercícios de Fixação

🎯 Exercício 1: 
Contagem Regressiva
Crie um programa que faça uma contagem regressiva de $10$ até $0$ usando while e, no final, imprima "Fogo! 🚀".

🎯 Exercício 2: 
Somador de Números
Crie um programa que peça para o usuário digitar vários números inteiros. O programa deve ir somando todos os números digitados. O laço deve parar apenas quando o usuário digitar 0. No final, mostre o resultado da soma.

🎯 Exercício 3: 
Jogo da AdivinhaçãoCrie uma variável numero_secreto = 7. 
Peça ao usuário para adivinhar o número. O laço while deve continuar pedindo palpites até que o usuário acerte. Quando acertar, exiba a mensagem "Parabéns, você adivinhou!".
