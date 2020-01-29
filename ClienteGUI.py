#Interfaz Gráfica y comunicación por sockets
#Parte del cliente

import tkinter as tk
from tkinter import *
import socket
import threading

#Variables globales
mensajeCli="" #mensaje cliente
mensajeServidor=""


def escribirMensajesEspacio(msg):
	msg2="\n" +msg
	mensajesEspacio.config(state=NORMAL)
	mensajesEspacio.insert(END,msg2 )
	mensajesEspacio.config(state=DISABLED)

def recibirMensaje():
	while True:
		mensajeServidor=cliente.recv(1024).decode("utf-8")
		msg="<<Otro>>: "+mensajeServidor
		escribirMensajesEspacio(msg)


def mandarMensaje():
	mensajeCli=miMensaje.get()
	msg= "<Tú>: " +str(mensajeCli)
	escribirMensajesEspacio(msg)
	cliente.send(mensajeCli.encode("utf-8"))
	if(mensajeCli=='exit' or mensajeCli=='quit'):
		cliente.close()
		escribirMensajesEspacio("Conexión cerrada")
	miMensaje.delete(0, END)
	miMensaje.config(fg='black')
	#recibirMensaje()


def marcaAgua(event):
	#Marca de agua para espacio donde el cliente escribe mensajes
	textoCurrent=miMensaje.get()
	if textoCurrent=='Ingrese un mensaje':
		miMensaje.delete(0, END)
		miMensaje.config(fg='black')
	elif textoCurrent=='':
		miMensaje.insert(0, "Ingrese un mensaje")
		miMensaje.config(fg='grey')


#Ventana
ventana=tk.Tk()  #Crear una ventana
ventana.title("Chat: Cliente")
ventana.iconbitmap("aa.ico")  #Icono .ico para la interfaz grafica
ventana.geometry("490x340") #Tamaño de la ventana ancho x largo
ventana.resizable(width=FALSE, height=FALSE) #No cambiar tamaño ventana

#Espacio para ver la conversación
mensajesEspacio=Text(ventana, width=55,  height=15, bg="gray85")
mensajesEspacio.insert(END, "<<Esperando a que la otra persona se conecte al chat>>") #Mensaje inicial
#mensajesEspacio.config(state=DISABLED) #No modificar texto de aquí
mensajesEspacio.grid(row=0, column=0, padx=10, pady=10)


#barra de desplazamiento vertical con una araña como cursor
barra=tk.Scrollbar(ventana, width=28, activebackground="gray45", cursor="spider")
barra.config(command = mensajesEspacio.yview) #barra en sentido vertical que sirve para ver texto de 'mensajesEspacio'
barra.grid(row=0, column=1, sticky='nsew')
mensajesEspacio['yscrollcommand']=barra.set

#Espacio para mandar mensaje
miMensaje=Entry(ventana, width=50)
miMensaje.insert(0, "Ingrese un mensaje")
miMensaje.grid(row=1, column=0, padx=10, pady=10)
miMensaje.bind("<FocusIn>", marcaAgua)
miMensaje.bind("<FocusOut>", marcaAgua)

#Boton de enviar
boton=Button(ventana, text="Enviar", width=20, command=mandarMensaje)
boton.grid(row=2, column=0, padx=10, pady=10)


#Socket cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() # Es el localhost              
port = 9999
cliente.connect((host, port))
escribirMensajesEspacio("Conexión exitosa")


#Implemento un hilo para recibir los mensajes
t1=threading.Thread(name='hilo1', target=recibirMensaje) #Mando llamara la función recibirMensaje desde este hilo
t1.start() #hilo1 empieza

ventana.mainloop() #ejecuta código de la ventana (Interfaz gráfica)