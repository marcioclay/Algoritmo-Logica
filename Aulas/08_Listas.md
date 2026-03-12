##Aula: Manipulação de Listas em Programação

### 1. O que é uma Lista?

Uma Lista (ou Array em algumas linguagens) é uma estrutura de dados que permite armazenar múltiplos valores em uma única variável.

Imagine que, em vez de criar as variáveis ip1, ip2, ip3, você cria uma lista chamada ips_da_rede que guarda todos esses endereços. Cada item em uma lista possui uma posição numerada chamada Índice, que sempre começa no 0.

### 2. Criando e Listando (Acesso)
Para criar uma lista, usamos colchetes []. Para acessar um item específico, usamos o seu índice.

```
# Criando a lista de dispositivos
dispositivos = ["Roteador", "Switch", "Servidor", "Desktop"]

# Acessando itens pelo índice
print(dispositivos[0])  # Saída: Roteador
print(dispositivos[2])  # Saída: Servidor

# Listando todos os itens com um laço 'for'
for d in dispositivos:
    print(f"Equipamento: {d}")
```
### 3. Modificando Itens
Podemos alterar o valor de um item existente referenciando o seu índice e atribuindo um novo valor.

```
equipamentos = ["Impressora Laster", "Teclado"]

# O usuário trocou a impressora por um Scanner
equipamentos[0] = "Scanner Profissional"

print(equipamentos) # Saída: ['Scanner Profissional', 'Teclado']
```

### 4. Incluindo Novos Itens (Inserção)
Existem duas formas principais de adicionar itens:

.append(): Adiciona o item ao final da lista.

.insert(): Adiciona o item em uma posição específica.

```
softwares = ["Windows 10", "Office 2019"]

# Adicionando ao final
softwares.append("Antivírus")

# Adicionando o Linux na primeira posição (índice 0)
softwares.insert(0, "Ubuntu Server")

print(softwares) 
# Saída: ['Ubuntu Server', 'Windows 10', 'Office 2019', 'Antivírus']
```
### 5. Excluindo Itens (Remoção)
Para remover dados, as formas mais comuns são:

.remove(): Remove pelo valor do item.

.pop(): Remove pelo índice (se não informar o índice, remove o último).

del: Remove um item ou uma fatia da lista pelo índice.

```
usuarios = ["admin", "convidado", "suporte", "estagiario"]

# Removendo pelo nome
usuarios.remove("convidado")

# Removendo o último da lista (estagiario)
usuarios.pop()

# Removendo pelo índice usando del
del usuarios[0] # Remove o 'admin'

print(usuarios) # Saída: ['suporte']
```

### 6. Resumo de Comandos Rápidos

<img width="700" height="349" alt="image" src="https://github.com/user-attachments/assets/53c9c4fa-94cd-48fb-9bc8-d494dd4f4201" /> 

### 7. Desafio Prático 🚀
Crie um programa que gerencie uma Lista de Chamados Técnicos.

O programa deve iniciar com 3 chamados: "Formatação", "Troca de Toner" e "Configurar Wi-Fi".

Adicione um novo chamado: "Instalação de Backup".

O chamado "Troca de Toner" foi resolvido; remova-o da lista.

Exiba na tela a quantidade total de chamados pendentes e a lista atualizada.


