from socket import *

def receberArquivo():
	nome_arquivo = connectionSocket.recv(1024).decode()
	dados = connectionSocket.recv(1024).decode()
	with open(nome_arquivo, 'w') as arquivo:
		arquivo.write(dados)
		print("Arquivo recebido com sucesso\n")


def enviarArquivo():
	nome_arquivo = connectionSocket.recv(1024).decode()
	with open(nome_arquivo, 'r') as arquivo:
		dados = arquivo.read()
		connectionSocket.send(dados.encode())
		print("Arquivo enviado com sucesso\n")


serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive\n')

while True:
	connectionSocket, addr = serverSocket.accept()
	choice = connectionSocket.recv(1024).decode()
    
	if choice == '2':
		receberArquivo()
	
	elif choice == '3':
		enviarArquivo()
            
	confirmation = 'Connected, everything went OK'
	connectionSocket.send(confirmation.encode())
	connectionSocket.close()
	
	
	
