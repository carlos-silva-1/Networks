from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

N = 10

for n in range(1, N+1):
    n_str = str(n)
    clientSocket.send(n_str.encode())

clientSocket.close()
