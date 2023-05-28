from socket import *
import threading

serverPort = 12000

def iniciaServidor():
	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind(('', serverPort))
	return sock

def atendeRequisicoes(message, clientAddress, serverSocket):
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

def main():
    threads = []
    sock = iniciaServidor()
    print("The server is ready to receive")
    for i in range(3):
        message, clientAddress = sock.recvfrom(2048)
        print ('Mensagem recebida de: ', clientAddress)
        cliente = threading.Thread(target=atendeRequisicoes, args=(message, clientAddress, sock))
        cliente.start()
        threads.append(cliente)
    
    for thread in threads:
        thread.join()
    
    sock.close()

main()
