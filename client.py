import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host,port))
message = input("--> ")
while message!="quit":
	s.send(message.encode())
	data = s.recv(1024)
	print ('Server Received message! ')
	message = input("-->")
s.close()    