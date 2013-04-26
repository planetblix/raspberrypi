import socket

HOST = '192.168.0.4' #This is the I.P. Address of the machine this code is running on
PORT = 8000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) # Only accepts 1 x client connection
conn,addr = s.accept()

print "Connected by", addr

i = True

while i is True:
  
	data = conn.recv(1024)

	print 'Received', repr(data)
	if not data:
		break
	
	reply = raw_input("Reply: ")

	conn.sendall(reply)

conn.close()

