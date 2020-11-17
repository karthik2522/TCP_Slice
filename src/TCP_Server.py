import socket 
import select 
import sys 
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

if len(sys.argv) != 3: 
	print " script, IP address, port number"
	exit() 

IP_address = str(sys.argv[1]) 

Port = int(sys.argv[2]) 

server.bind((IP_address, Port)) 
server.listen(100) 

number_of_clients = [] 

def clientthread(conn, addr): 
	conn.send("Welcome to TCP Program!") 
	while True: 
			try: 
				msg = conn.recv(2048) 
				if msg: 

					print "<" + addr[0] + "> " + msg 
					msg_to_send = "<" + addr[0] + "> " + msg 
					broadcast(msg_to_send, conn) 

				else: 
					remove(conn) 

			except: 
				continue

def broadcast(msg, connection): 
	for client in number_of_clients: 
		if client!=connection: 
			try: 
				client.send(msg) 
			except: 
				client.close() 
				remove(client) 
def remove(connection): 
	if connection in number_of_clients: 
		number_of_clients.remove(connection) 

while True: 
	conn, addr = server.accept() 
	number_of_clients.append(conn) 
	print addr[0] + " connected"
	start_new_thread(clientthread,(conn,addr))	 

conn.close() 
server.close() 
