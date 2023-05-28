from socket import *
import threading

serverName = ''
serverPort = 12000

def iniciaServidor():
	'''Cria um socket de servidor e o coloca em modo de espera por conexoes
	Saida: o socket criado'''
	# cria o socket 
	sock = socket(AF_INET, SOCK_STREAM) #Internet( IPv4 + TCP) 
	# vincula a localizacao do servidor
	sock.bind((serverName, serverPort))
	# coloca-se em modo de espera por conexoes
	sock.listen(3) 
	return sock

def atendeRequisicoes(clisock, endr):
    '''Recebe mensagens e as envia de volta para o cliente (ate o cliente finalizar)
    Entrada: socket da conexao e endereco do cliente
    Saida: '''
    while True:
        #recebe dados do cliente
        message = clisock.recv(2048) 
        if not message: # dados vazios: cliente encerrou
            print(str(endr) + '-> encerrou')
            clisock.close() # encerra a conexao com o cliente
            return
        modifiedMessage = message.decode().upper()
        clisock.send(modifiedMessage.encode())
		
def main():
    threads = []
    sock = iniciaServidor()
    print("The server is ready to receive")
    for i in range(3):
        clisock, endr = sock.accept()
        print ('Conectado com: ', endr)
        cliente = threading.Thread(target=atendeRequisicoes, args=(clisock, endr))
        cliente.start()
        threads.append(cliente)
    
    for thread in threads:
        thread.join()

    sock.close()

main()
