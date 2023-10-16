from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
	connectionSocket, addr = serverSocket.accept()
	choice = connectionSocket.recv(1024).decode()
    
	if choice == '2':
		dados = connectionSocket.recv(1024).decode()
		with open('arquivo_recebido.txt', 'w') as arquivo:
			arquivo.write(dados)
		print("Arquivo recebido com sucesso")
	
	elif choice == '3':
		nome_arquivo = connectionSocket.recv(1024).decode()
		with open(nome_arquivo + '.txt', 'r') as arquivo:
			dados = arquivo.read()
			connectionSocket.send(dados.encode())
			print("Arquivo enviado com sucesso")
            
	confirmation = 'Connected, everything went OK'
	connectionSocket.send(confirmation.encode())
	connectionSocket.close()
