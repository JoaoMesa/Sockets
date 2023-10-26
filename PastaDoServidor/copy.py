from socket import *
import threading

def receberArquivo(connectionSocket):
    # Lê o nome do arquivo até o delimitador
	nome_arquivo = ""
	delimitador = "@"  # Delimitador personalizado, como uma quebra de linha

	while True:
		caractere = connectionSocket.recv(1).decode()
		if caractere == delimitador:
			break
		nome_arquivo += caractere

	print("nome_arquivo  " + nome_arquivo)

	# Lê os dados
	dados = connectionSocket.recv(1024).decode()

	with open(nome_arquivo, 'w') as arquivo:
		arquivo.write(dados)

	print("Arquivo recebido com sucesso\n")


def enviarArquivo(connectionSocket):
    nome_arquivo = connectionSocket.recv(1024).decode()
    with open(nome_arquivo, 'r') as arquivo:
        dados = arquivo.read()
    connectionSocket.send(dados.encode())
    print("Arquivo enviado com sucesso\n")

def conectaCliente(connectionSocket):
	choice = connectionSocket.recv(1024).decode()
	print("choice  " + choice)
	if choice == '2':
		print("Entrei aqui")
		receberArquivo(connectionSocket)
	elif choice == '3':
		enviarArquivo(connectionSocket)

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive\n')

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=conectaCliente, args=(connectionSocket,))
    client_thread.start()

