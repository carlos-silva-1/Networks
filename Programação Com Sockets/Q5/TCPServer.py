from socket import *
import json

serverPort = 12000

username = "user"
password = "pass"

dado = "14"
msg_erro = "Wrong username or password"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("The server is ready to receive")

novoSock, endereco = serverSocket.accept()

print('Conectado com: ', endereco)

while True:
    packet = novoSock.recv(2048)

    if not packet:
        break

    payload_json = packet.decode()
    payload = json.loads(payload_json)

    if payload["username"] != username or payload["password"] != password:
        novoSock.send(msg_erro.encode())
    else:
        novoSock.send(dado.encode())

novoSock.close()
serverSocket.close()
