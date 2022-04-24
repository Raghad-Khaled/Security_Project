from email.message import Message
from RSA import *
import socket

def readySend():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1242))
    s.listen(5)
    return s.accept()

def Send(msg,clientsocket, address):
    #print(f"Connection from {address} has been established.")
    clientsocket.send(msg.encode()) 

def readyRecive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1241))
    return s

def Recive(s):
    full_msg=''
    new_msg = True
    while True:
        msg = s.recv(1024).decode()
        return msg

#recive public key from user A
s=readyRecive()
e_A=int(Recive(s)) #recive the public key for reciver
n_A=int(Recive(s))

#send public key to user A
P,Q=ReadfromFile('PQ2.txt')
e,n=GeneratePublicKey(P,Q)
d,n=GeneratePrivateKey(P,Q,e)
clientsocket, address =readySend()
Send(str(e),clientsocket, address )
Send(str(n),clientsocket, address )


while True:
    Message = input ("Donia :")
    Cipher=Encrypt(str(Message),n_A,e_A) # encript with the publick key of reciver
    if(Cipher != false):
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver
    else:
        Cipher=Encrypt(str(0),n_A,e_A)
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver

    Cipher=Recive(s) #recive the Cipher text
    Message=Decrypt(Cipher,n,d)
    if(Message=='0'):
        print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it")
    else:
        print(f"Raghad :{Message} ")    



