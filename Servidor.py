import socket 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()                           
port = 9999                                           
servidor.bind((host, port))

servidor.listen(1)  #Numero máximo de conexiones

conn, addr = servidor.accept()
#regresa la conexión y dirección a donde se hizo la conexión
print("Servidor conectado a un cliente")

while True: 
   msg = conn.recv(1024) #El 1024 es por protocolo
   msg = msg.decode('utf-8')
   if msg  == 'exit':
      break
   print("<Cliente>: " +msg +"\n")
   mensaje = input(">> ")
   conn.send(mensaje.encode('utf-8'))

conn.close()
servidor.close()
print("Conexión cerrada")