from socket import *
import threading

def receberArquivo(connectionSocket):
	nome_arquivo = ""
	delimitador = "@" 

	while True:
		caractere = connectionSocket.recv(1).decode()
		if caractere == delimitador:
			break
		nome_arquivo += caractere

	#print("nome_arquivo  " + nome_arquivo)

	dados = connectionSocket.recv(1024).decode()

	with open(nome_arquivo, 'w') as arquivo:
		arquivo.write(dados)

	print("Arquivo recebido com sucesso\n")


def enviarArquivo(connectionSocket):
	nome_arquivo = ""
	delimitador = "@" 

	while True:
		caractere = connectionSocket.recv(1).decode()
		if caractere == delimitador:
			break
		nome_arquivo += caractere

	#print("nome_arquivo  " + nome_arquivo)
	with open(nome_arquivo, 'r') as arquivo:
		dados = arquivo.read()
	connectionSocket.send(dados.encode())
	print("Arquivo enviado com sucesso\n")
	
def encerrarComunicacao(connectionSocket):
	mensagem = "Encerrando conecção, obrigado.\n"
	connectionSocket.send(mensagem.encode())

def conectaCliente(connectionSocket):
	choice = connectionSocket.recv(1024).decode()
	#print("choice  " + choice)
	if choice == '1':
		encerrarComunicacao(connectionSocket)
	elif choice == '2':
		#print("Entrei aqui")
		receberArquivo(connectionSocket)
		encerrarComunicacao(connectionSocket)
	elif choice == '3':
		enviarArquivo(connectionSocket)
		encerrarComunicacao(connectionSocket)

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Servidor pronto para receber\n')

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=conectaCliente, args=(connectionSocket,))
    client_thread.start()

