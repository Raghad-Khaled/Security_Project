#from email.message import Message
from RSA import *
import socket
import sys

CHAT =1
FILE =2
# Tha Modes of operation 1)chat 2)file read and write 3)attack  
Mode =int(sys.argv[1])

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
# write the public key at file to be Public (can be reed by attacker)
f=open("publicData.txt",'w')
f.write(str(e_A)+"\n") # save the public key of Raghad
f.write(str(n_A)+"\n")

Doniaout=open("Doniaout.txt",'w')
Doniain=open("Doniain.txt",'r')

while True:
    if(Mode==CHAT):
        Message = input ("Donia :")
    elif(Mode ==FILE):
        Message=Doniain.readline()

    if(Message=="" or Message=="q"):
        Message="q"                  # when get q that mean end the chat or the end of file 
    Cipher, CipherInt=Encrypt(str(Message),n_A,e_A) # encript with the publick key of reciver

    if(Cipher != false):
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver
        f.write(str(ConvertToInt(Cipher)) + '\n')    
    else:                                             # can not encript as the message too large so send 0
        Cipher, CipherInt=Encrypt(str(0),n_A,e_A)
        Send(Cipher,clientsocket, address ) #send the cipher message to reciver

    if(Message=="q"):  #end the program as  q is typed
        break


    Cipher=Recive(s) #recive the Cipher text
    Message, MessageInt=Decrypt(Cipher,n,d)
    if(Message=="q"):  #end the program as  q is typed
        break
    elif(Message=='0'):
        print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it")
    elif(Mode==CHAT):
        print(f"Raghad :{Message} ")
    elif(Mode==FILE):
        Doniaout.write("Raghad :"+Message+"\n")         






