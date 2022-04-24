from RSA import *
import socket

def readySend():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1241))
    s.listen(5)
    return s.accept()

def Send(msg,clientsocket, address):
    #print(f"Connection from {address} has been established.")
    clientsocket.send(msg.encode())   

def readyRecive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1242))
    return s

def Recive(s):
    full_msg=''
    new_msg = True
    while True:
        msg = s.recv(1024).decode()
        return msg


#send public key to user B
P,Q=ReadfromFile('PQ.txt')
e,n=GeneratePublicKey(P,Q)
d,n=GeneratePrivateKey(P,Q,e)
clientsocket, address =readySend()
Send(str(e),clientsocket, address )
Send(str(n),clientsocket, address )

#recive public key from user B
s=readyRecive()
e_B=int(Recive(s)) #recive the public key for reciver
n_B=int(Recive(s))



while True:
    Cipher=Recive(s) #recive the Cipher text
    Message=Decrypt(Cipher,n,d)
    if(Message=='0'):
        print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it") #message lenth can be up to 66
    else:
        print(f"Donia :{Message} ")

    Message = input ("Raghad :")
    Cipher=Encrypt(str(Message),n_B,e_B) # encript with the publick key of reciver
    if(Cipher != false):
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver
    else:
        Cipher=Encrypt(str(0),n_B,e_B)
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver
    





