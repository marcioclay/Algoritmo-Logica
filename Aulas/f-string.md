## F-Strings
### As f-strings (Formatted String Literals) são a maneira mais moderna e eficiente de formatar textos em Python, disponíveis desde a versão 3.6. Para um técnico em informática, dominar isso é essencial para criar relatórios, logs e interfaces de terminal organizadas.

A sintaxe básica consiste em colocar um f antes das aspas: f"Texto {variavel}".

Formatação de Saídas com f-strings
### 1. Formatando Números Decimais (float)
Quando trabalhamos com cálculos financeiros ou medições de sensores, o Python pode exibir muitas casas decimais (ex: 3.333333335). Com f-strings, controlamos isso facilmente usando :.[quantidade]f.
```
valor_dolar = 5.23891
print(f"O valor atual é R$ {valor_dolar:.2f}") 
# Saída: O valor atual é R$ 5.24 (arredonda automaticamente)
```
### 2. Alinhamento e Espaçamento (Tabelas no Terminal)
Muito útil para criar listas de dispositivos ou usuários onde as colunas precisam estar alinhadas.

:< Alinha à esquerda (padrão para textos).

:> Alinha à direita (padrão para números).

:^ Alinha ao centro.

```
print(f"{'DISPOSITIVO':<15} | {'STATUS':^10}")
print("-" * 30)
print(f"{'Roteador L3':<15} | {'ONLINE':^10}")
print(f"{'Switch Core':<15} | {'OFFLINE':^10}")
```
Dica: O número após o símbolo (ex: <15) define a largura total do campo em caracteres.

### 3. Separadores de Milhar e Porcentagem
Para facilitar a leitura de grandes números ou exibir taxas de conclusão:

```
# Separador de milhar (usa vírgula ou underline)
memoria_bytes = 1048576
print(f"Memória: {memoria_bytes:,} bytes")
# Saída: Memória: 1,048,576 bytes

# Porcentagem
progresso = 0.75
print(f"Download: {progresso:.1%}")
# Saída: Download: 75.0%
```

### 4. Preenchimento com Zeros (Zero Padding)
Essencial para formatar IDs, endereços IP ou horas.

```
dia = 9
mes = 3
ano = 2026
# Garante que o número tenha pelo menos 2 dígitos, preenchendo com zero à esquerda
print(f"Data: {dia:02d}/{mes:02d}/{ano}")
# Saída: Data: 09/03/2026
```

### 5. Executando Expressões Simples
Você pode realizar cálculos ou chamar métodos diretamente dentro das chaves:

```
nome = "servidor_linux"
print(f"Nome do host: {nome.upper()}") # Saída: SERVIDOR_LINUX

preco = 100
print(f"Preço com imposto (5%): {preco * 1.05:.2f}") # Saída: 105.00
```

### Resumo de consulta rápida:

<img width="607" height="302" alt="image" src="https://github.com/user-attachments/assets/9975c424-bacb-41d3-abb6-29e28791ea31" /> 






