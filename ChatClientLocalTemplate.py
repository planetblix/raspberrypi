from socket import *

HOST = '192.168.0.4' #This is the I.P. Address of the other machine
PORT = 8000 

def encrypt(message):
        encoded_message = message.upper()
        return encoded_message

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST,PORT))
while True:
        message = raw_input("Your message:")
        e_message = encrypt(message)
        s.send(e_message)
        print 'Awaiting reply...'
        reply = s.recv(1024)
        print "Received", repr(reply)

s.close()

