from socket import *

serverName = ''
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
	choice = int(input("O que você quer?\n 1 - Sair \n 2 - Armazenar arquivo \n 3 - Receber Arquivo\n"))
	clientSocket.send(str(choice).encode())
    
	if choice == 1:
		break
	elif choice == 2:
		nome_arquivo = input("Digite o nome do arquivo a ser enviado: ")
		with open(nome_arquivo + '.txt', 'r') as arquivo:
			dados = arquivo.read()
			clientSocket.send(dados.encode())
			print("Arquivo enviado com sucesso")
	elif choice == 3:
		nome_arquivo = input("Digite o nome do arquivo a ser recebido: ")
		clientSocket.send(nome_arquivo.encode())
		dados = clientSocket.recv(1024).decode()
		with open(nome_arquivo + '.txt', 'w') as arquivo:
			arquivo.write(dados)
		print("Arquivo recebido com sucesso")

        
confirmation = clientSocket.recv(1024).decode()
print('From Server:', confirmation)

clientSocket.close()
