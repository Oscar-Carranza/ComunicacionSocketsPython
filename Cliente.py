import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()# Es el localhost              
port = 9999
cliente.connect((host, port))
print("Cliente conectado al servidor")   

while True:
    mensaje = input(">> ")
    cliente.send(mensaje.encode('utf-8'))
    if (mensaje == 'exit' or mensaje == 'quit'):
        break

    #Para recibir mensajes del servidor:
    msg = cliente.recv(1024)  
    msg = msg.decode('utf-8')
    print("<Servidor>: " +msg+"\n")

cliente.close()
print("Conexión cerrada")