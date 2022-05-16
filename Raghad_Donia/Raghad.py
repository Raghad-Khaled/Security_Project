from ast import Mod
from os import system
from RSA import *
import socket
import sys

CHAT =1
FILE =2
ATTACK=3
# Tha Modes of operation 1)chat 2)file read and write 3)attack  
Mode =int(sys.argv[1])
int 
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
if(Mode != ATTACK): # NOT Send key to attacker
    e,n=GeneratePublicKey(P,Q)
else:
    e,n=ReadfromFile("publicData.txt")    
d,n=GeneratePrivateKey(P,Q,e)

clientsocket, address =readySend()
if(Mode != ATTACK): # NOT Send key to attacker
    Send(str(e),clientsocket, address )
    Send(str(n),clientsocket, address )

#recive public key from user B
s=readyRecive()
if(Mode != ATTACK): # NOT recived key from attacker
    e_B=int(Recive(s)) #recive the public key for reciver
    n_B=int(Recive(s))

Raghadout=open("Raghadout.txt",'w')
Raghadin=open("Raghadin.txt",'r')

while True:
    Cipher=Recive(s) #recive the Cipher text
    if(Cipher == "end"):       # CCA end
        break
    Message=Decrypt(Cipher,n,d)
    if(Message=="q"):  #end the program as  q is typed
        break
    elif(Message=='0'):
        print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it") #message lenth can be up to 66
    elif(Mode == CHAT):
        print(f"Donia :{Message} ")
    elif(Mode == FILE):
        Raghadout.write("Donia :"+Message+"\n")    
    if(Mode ==ATTACK ):
        Send(Message,clientsocket, address ) #send the meaasege to attaker after decreption
    else:
        if(Mode ==CHAT ):
            Message = input ("Raghad :")
        elif (Mode == FILE):
            Message=Raghadin.readline() 

        if(Message=="" or Message=="q"):
            Message="q"                  # when get q that mean end the chat or the end of file

        Cipher=Encrypt(str(Message),n_B,e_B) # encript with the publick key of reciver
        if(Cipher != false):
            Send(Cipher,clientsocket, address ) #send the cipher message to reciver
        else:
            Cipher=Encrypt(str(0),n_B,e_B)
            Send(Cipher,clientsocket, address ) #send the cipher message to reciver

        if(Message=="q"):  #end the program as  q is typed
            break
    
    





