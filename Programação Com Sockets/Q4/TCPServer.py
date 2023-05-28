from socket import *
import threading

serverName = ''
serverPort = 12000

def iniciaServidor():
	# cria o socket 
	sock = socket(AF_INET, SOCK_STREAM) #Internet( IPv4 + TCP) 
	# vincula a localizacao do servidor
	sock.bind((serverName, serverPort))
	# coloca-se em modo de espera por conexoes
	sock.listen(1) 
	return sock

def atendeRequisicoes(clisock, endr):
    while True:
        #recebe dados do cliente
        message = clisock.recv(2) 
        if not message: # dados vazios: cliente encerrou
            print(str(endr) + '-> encerrou')
            clisock.close() # encerra a conexao com o cliente
            return
        print(message.decode())
		
def main():
    sock = iniciaServidor()
    print("The server is ready to receive")
    while True:
        clisock, endr = sock.accept()
        print ('Conectado com: ', endr)
        atendeRequisicoes(clisock, endr)

    sock.close()

main()
