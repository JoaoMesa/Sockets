import java.io.*;
import java.net.*;
class servidor {
public static void main(String argv[]) throws Exception
{
String clientSentence;
String capitalizedSentence;
System.out.println("Entrando no servidor");
ServerSocket welcomeSocket = new ServerSocket(12001);
while(true) {
Socket connectionSocket = welcomeSocket.accept();
BufferedReader inFromClient =
new BufferedReader(new
InputStreamReader(connectionSocket.getInputStream()));
DataOutputStream outToClient =
new DataOutputStream(connectionSocket.getOutputStream());

clientSentence = inFromClient.readLine();

capitalizedSentence = clientSentence.toUpperCase() + '\n';

outToClient.writeBytes(capitalizedSentence);
}
}
}
