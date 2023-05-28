from socket import *
import json

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

username = input("Username:")
password = input("Password:")
payload = {"username": username, "password": password}
payload_json = json.dumps(payload)

if not username or not password:
    print("Erro: nem usuario nem senha podem estar vazios")
else:
    clientSocket.send(payload_json.encode())
    message = clientSocket.recv(2048)
    print(message.decode())

clientSocket.close()
