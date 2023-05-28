from socket import *
import threading

serverPort = 12000

def iniciaServidor():
	sock = socket(AF_INET, SOCK_DGRAM)
	sock.bind(('', serverPort))
	return sock

def atendeRequisicoes(message):
    print(message.decode())

def main():
    sock = iniciaServidor()
    print("The server is ready to receive")
    while True:
        message, clientAddress = sock.recvfrom(2048)
        atendeRequisicoes(message)

main()
