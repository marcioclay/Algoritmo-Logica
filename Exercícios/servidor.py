# Ajuste o código,pois pode conter erros.
import socket
HOST = ''              # Endereco IP do Servidor e o endereco atual do computador
PORT = 5000            # Porta que o Servidor na maquina
# Cria o socket do servidor
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT) # Forma a tupla de host, porta

tcp.bind(orig)		# Solicita ao S.O. acesso exclusivo a porta 5000
tcp.listen(10)		# Entra no modo de escuta


print(">>> Aguardando Conexão")
codigo = open('dados.txt', 'r',encoding='utf-8')
while True:
    con, cliente = tcp.accept() # Aceita conexao do cliente
    print ('Concetado por', cliente)
    
    while True:
#------- inicio do protocolo --------------
        msg = con.recv(1024)
        msg = msg.decode('UTF-8')
        print (cliente, msg)
        if codigo ==msg:
            msg = input(">> Digite a Mensagem: ")
            msg = msg.encode('UTF-8')
            con.send(msg)
        else:
            msg_erro="Codigo não identificado"
            msg_erro = msg.encode('UTF-8')
            con.send(msg_erro)



#---------------- fim do protocolo --------------

con.close()		# fecha a conexao com o cliente
codigo.close()
