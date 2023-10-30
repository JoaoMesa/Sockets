import java.io.*;
import java.net.*;
import java.nio.file.Files;
import java.nio.file.Paths;


class client {
public static void main(String argv[]) throws Exception{

	BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
	Socket clientSocket = new Socket("", 12001);
	DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
	BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		
		System.out.println("O que você quer?\n 1 - Sair \n 2 - Armazenar arquivo \n 3 - Receber Arquivo\n");
		String choice;
		
		choice=inFromUser.readLine();
		
		outToServer.writeBytes(choice);	
		
		if (choice.equals("2")){
			String nomeArquivo;
			System.out.println("Qual o nome do arquivo?");
			nomeArquivo = inFromUser.readLine();
				
			File file = new File(nomeArquivo);
			//System.out.println(nomeArquivo);
			
			String fileContent = new String(Files.readAllBytes(file.toPath()));

           		//System.out.println(fileContent);
           		
           		outToServer.writeBytes(nomeArquivo + "@");
           		outToServer.flush();
           		outToServer.writeBytes(fileContent);
           		outToServer.flush();
		}
		else if (choice.equals("3")){
			String nomeArquivo;
			System.out.println("Qual arquivo deseja importar?");
			nomeArquivo = inFromUser.readLine();
			
			//System.out.println(nomeArquivo);
			outToServer.writeBytes(nomeArquivo + "@");
			
			String datafromServer;
			datafromServer = inFromServer.readLine();
			
			try {
            			BufferedWriter writer = new BufferedWriter(new FileWriter(nomeArquivo));
            			writer.write(datafromServer);
				
            			writer.close(); 
            			System.out.println("Arquivo criado e texto escrito com sucesso.");
        } catch (IOException e) {
            e.printStackTrace();
        }
		}
	
	//System.out.println("Saindo do loop");
	String mensagem = inFromServer.readLine();
	System.out.println(mensagem);
	
}
}
