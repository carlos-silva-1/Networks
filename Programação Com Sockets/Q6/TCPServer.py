from socket import *
import threading

serverName = ''
serverPort = 12000

msg_boas_vindas = "Olá! Bem-vindo! Qual o seu nome?"
msg_servicos = "! Como posso te ajudar? Digite o número que corresponde à opção desejada: \n1 - Agendar um horário de monitoria \n2 - Listar as próximas atividades da disciplina \n3 - Email do professor"
msg_monitoria = "Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br"
msg_atividades_pendentes = "Fique atento para as datas das próximas atividades. Confira o que vem por aí! \nP1: 26 de Maio de 2022 \nLista3: 29 de Maio de 2022"
msg_email_prof = "Quer falar com o professor? O e-mail dele é sadoc@dcc.ufrj.br"
msg_final = "Obrigado por utilizar nossos serviçoes! Até logo!"
msg_to_send = ""

def iniciaServidor():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((serverName, serverPort))
	sock.listen(3) 
	return sock

def atendeRequisicoes(clisock, endr):
    message = clisock.recv(2048) 
    clisock.send(msg_boas_vindas.encode())

    nome = clisock.recv(2048)
    clisock.send(("Certo, " + nome.decode() + msg_servicos).encode())

    escolha = clisock.recv(2048)
    num_escolha = escolha.decode()
    if num_escolha == "1":
        msg_to_send = msg_monitoria
    elif num_escolha == "2":
        msg_to_send = msg_atividades_pendentes
    elif num_escolha == "3":
        msg_to_send = msg_email_prof
    msg_to_send = msg_to_send + "\n" + msg_final
    clisock.send(msg_to_send.encode())
		
def main():
    sock = iniciaServidor()
    print("The server is ready to receive")
    while True:
        clisock, endr = sock.accept()
        print ('Conectado com: ', endr)
        atendeRequisicoes(clisock, endr)

    sock.close()

main()
