from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

N = 10

for n in range(1, N+1):
    n_str = str(n)
    clientSocket.sendto(n_str.encode(), (serverName, serverPort))

clientSocket.close()
