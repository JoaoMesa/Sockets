from socket import *

serverName = ''
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
	choice = int(input("O que você quer?\n 1 - Sair \n 2 - Armazenar arquivo \n 3 - Receber Arquivo\n 4 - Criar arquivo localmente\n"))
	clientSocket.send(str(choice).encode())
    
	if choice == 1:
		break
	elif choice == 2:
		nome_arquivo = input("Digite o nome do arquivo a ser enviado: ")
		clientSocket.send(nome_arquivo.encode())
		with open(nome_arquivo, 'r') as arquivo:
			dados = arquivo.read()
			clientSocket.send(dados.encode())
			print("Arquivo enviado com sucesso\n")
	elif choice == 3:
		nome_arquivo = input("Digite o nome do arquivo a ser recebido: ")
		clientSocket.send(nome_arquivo.encode())
		dados = clientSocket.recv(1024).decode()
		with open(nome_arquivo, 'w') as arquivo:
			arquivo.write(dados)
		print("Arquivo recebido com sucesso\n")
		
	elif choice == 4:
		nome_arquivo = input("Digite o nome do arquivo a ser criado (lembre de especificar o tipo do arquivo: \n")
		dados = input("O que escrever no arquivo?\n")
		with open(nome_arquivo, 'w') as arquivo:
			arquivo.write(dados)
		print("Arquivo criado com sucesso\n")

        
confirmation = clientSocket.recv(1024).decode()
print('From Server:', confirmation)

clientSocket.close()
