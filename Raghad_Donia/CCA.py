#from email.message import Message
from RSA import *
import socket
import codecs

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

# e_A=int(Recive(s)) #recive the public key for reciver
# n_A=int(Recive(s))
s=readyRecive()
#send public key to user A
# P,Q=ReadfromFile('PQ2.txt')
# e,n=GeneratePublicKey(P,Q)
# d,n=GeneratePrivateKey(P,Q,e)
clientsocket, address =readySend()


# Send(str(e),clientsocket, address )
# Send(str(n),clientsocket, address )

#e,n=ReadfromFile("publicData.txt")

f=open("publicData.txt")
try:
    e =int(f.readline())
    n = int(f.readline())
except ValueError:
    print("Can't read public key for Donia")    
            


while True:
    Cipher= f.readline()
    
    if(Cipher==""):
        Send( "end" ,clientsocket, address ) #send the cipher message to reciver
        print("\n No more messages")
        break

    r=Generater(n)
    Cipher_dash=ConvertToStr((int(Cipher) * PowMod(r,e,n))%n)
    Send( Cipher_dash ,clientsocket, address ) #send the cipher message to reciver
    Y=ConvertToInt(Recive(s))
    Message =ConvertToStr( (Y * InvertModulo(r,n))%n )
    print(f"Donia Message Attacked :{Message} ")    



