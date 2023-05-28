from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("The server is ready to receive")

novoSock, endereco = serverSocket.accept()

print('Conectado com: ', endereco)

while True:
    message = novoSock.recv(2048)
    if not message:
        break
    modifiedMessage = message.decode().upper()
    novoSock.send(modifiedMessage.encode())

novoSock.close()
serverSocket.close()