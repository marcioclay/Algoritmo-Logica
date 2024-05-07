# Abrindo arquivos em modo leitura e escrita
with open("dados.txt", 'r') as entrada, open("registro.txt", 'a') as saida:
  codigo_pesquisa = input("Digite o código a ser pesquisado: ")

  nome_encontrado = False
  for linha in entrada:
    codigo, nome = linha.strip().split()

    if codigo == codigo_pesquisa:
      print(f"Nome encontrado: {nome} (Código: {codigo})")
      saida.write(f"{nome} {codigo}\n")
      nome_encontrado = True
      break

  if not nome_encontrado:
    print(f"Nome não encontrado para o código {codigo_pesquisa}.")
