# Ajuste o código,pois pode conter erros.
import socket
import re

HOST = ''  # Endereço IP do Servidor e o endereço atual do computador
PORT = 5000  # Porta que o Servidor na máquina
# Cria o socket do servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)  # Forma a tupla de host, porta

tcp.bind(orig)  # Solicita ao S.O. acesso exclusivo a porta 5000
tcp.listen(10)  # Entra no modo de escuta

print(">>> Aguardando Conexão")

# Leitura do arquivo de códigos
with open('dados.txt', 'r', encoding='utf-8') as arquivo_codigos:
    codigos_validos = [linha.strip() for linha in arquivo_codigos]

while True:
    con, cliente = tcp.accept()  # Aceita conexão do cliente
    print('Conectado por', cliente)

    while True:
        # Recebe a mensagem do cliente
        msg_cliente = con.recv(1024).decode('UTF-8')
        print(f"{cliente}: {msg_cliente}")

        # Verifica se o código é válido
        if msg_cliente in codigos_validos:
            # Acesso autorizado
            msg_resposta = "Acesso autorizado! Digite sua mensagem: "
            msg_resposta = msg_resposta.encode('UTF-8')
            con.send(msg_resposta)

            # Abre o chat
            while True:
                # Envia mensagem do servidor
                msg_servidor = input(">> Digite sua mensagem: ")
                msg_servidor = msg_servidor.encode('UTF-8')
                con.send(msg_servidor)

                # Recebe a resposta do cliente
                msg_resposta_cliente = con.recv(1024).decode('UTF-8')
                print(f"{cliente}: {msg_resposta_cliente}")

                # Verifica se o cliente deseja sair
                if msg_resposta_cliente.lower() == "sair":
                    break

            # Envia mensagem de despedida
            msg_despedida = "Até a próxima!"
            msg_despedida = msg_despedida.encode('UTF-8')
            con.send(msg_despedida)

            break  # Sai do loop do chat

        else:
            # Código não encontrado
            msg_erro = "Código não identificado! Tente novamente."
            msg_erro = msg_erro.encode('UTF-8')
            con.send(msg_erro)

    con.close()  # Fecha a conexão com o cliente



#---------------- fim do protocolo --------------

con.close()		# fecha a conexao com o cliente
codigo.close()
