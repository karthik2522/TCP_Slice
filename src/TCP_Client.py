import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print " script, IP address, port number"
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

while True: 

	sockets_list = [sys.stdin, server] 
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			msg = socks.recv(2048) 
			print msg
		else: 
			msg = sys.stdin.readline() 
			server.send(msg) 
			sys.stdout.write("[--I am--]") 
			sys.stdout.write(msg) 
			sys.stdout.flush() 
server.close() 
