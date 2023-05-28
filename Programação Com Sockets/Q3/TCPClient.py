from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

while True:
    message = input('Input lowercase sentence:')
    if not message:
        break
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    print(modifiedMessage.decode())

clientSocket.close()
