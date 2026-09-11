# 🎯 Estruturas Condicionais no Python: O Comando `match-case`

Em programação, muitas vezes precisamos criar um menu de opções ou tomar decisões baseadas no valor de uma única variável. 
Quando temos muitas opções, utilizar vários blocos de `if`, `elif` e `else` pode deixar o código longo e difícil de ler.

Para resolver esse problema, o Python introduziu a estrutura **`match-case`** (disponível a partir do Python 3.10). 
Ela funciona de forma semelhante ao comando *switch-case* de outras linguagens.

---

## 💡 O que é o `match-case`?

Pense no `match-case` como um **controle remoto**:
* Você escolhe um número no controle (**`match`** na variável).
* A TV executa a ação correspondente àquele botão exato (**`case`** correspondente).

### Comparativo: `if-elif-else` vs `match-case`

| Usando `if-elif-else` | Usando `match-case` |
| :--- | :--- |
| Repete o nome da variável em toda linha (`if x == 1`, `elif x == 2`) | Avalia a variável apenas uma vez no topo (`match x`) |
| Recomendado para condições complexas (ex: `x > 10 e y < 5`) | Ideal para comparar valores exatos de uma única variável |

---

## 🛠️ Sintaxe Básica

```python
match variavel:
    case valor1:
        # Código executado se variavel == valor1
    case valor2:
        # Código executado se variavel == valor2
    case _:
        # Código padrão (equivalente ao 'else')
``` 

⚠️ Atenção: O underline case _: é chamado de Coringa (wildcard). 
Ele é executado caso nenhuma das opções anteriores seja verdadeira. Sempre o coloque no final!

📖 Exemplo Prático 1: Menu Telefônico
Vamos simular o atendimento automático de uma empresa:

# Solicitando a opção ao usuário
opcao = int(input("Digite uma opção (1-Suporte, 2-Financeiro, 3-Falar com Atendente): "))
```
# Avaliando a opção escolhida
match opcao:
    case 1:
        print("Você escolheu: Suporte Técnico.")
    case 2:
        print("Você escolheu: Setor Financeiro.")
    case 3:
        print("Aguarde, transferindo para um atendente...")
    case _:
        print("Opção inválida! Por favor, escolha um número entre 1 e 3.")
  ```

  🔀 Agrupando Múltiplos Valores
Você pode verificar mais de um valor no mesmo case utilizando o operador de barra vertical | (que significa OU).

Exemplo Prático 2: Dia Útil ou Fim de Semana

```
dia = input("Digite o dia da semana (ex: sabado, segunda): ").strip().lower()

match dia:
    case "sabado" | "domingo":
        print("É fim de semana! Hora de descansar. 🥳")
    case "segunda" | "terca" | "quarta" | "quinta" | "sexta":
        print("É dia útil. Vamos trabalhar e estudar! 💻")
    case _:
        print("Dia da semana não reconhecido.")
```

📌 Resumo Rápido

* match: Define a variável que será analisada.

* case valor:: Executa o bloco se a variável for igual ao valor.

* case valor1 | valor2:: Executa se a variável for igual a valor1 ou valor2.

* case _:: Executa se nenhuma opção anterior for correspondente (o "resto").
