from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

msg_final = "Obrigado por utilizar nossos serviçoes! Até logo!"

message = input('Digite algo:')

while True:
    clientSocket.send(message.encode())
    received_msg = clientSocket.recv(2048)
    print(received_msg.decode())
    if msg_final in received_msg.decode():
        break
    message = input()

clientSocket.close()
