from RSA import *
import socket

HEADERSIZE = 10

def readySend():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1241))
    s.listen(5)
    return s.accept()

def Send(msg,clientsocket, address):
    print(f"Connection from {address} has been established.")
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    print(msg)
    clientsocket.send(bytes(msg,"utf-8"))   

def readyRecive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1242))
    return s

def Recive(s):
    full_msg=''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            #print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        #print(f"full message length: {msglen}")
        full_msg += msg.decode("utf-8")
        if len(full_msg)-HEADERSIZE == msglen:
            print(full_msg[HEADERSIZE:])
            return full_msg[HEADERSIZE:]


P,Q=ReadfromFile()
e,n=GeneratePublicKey(P,Q)
clientsocket, address =readySend()
Send(str(e),clientsocket, address )
Send(str(n),clientsocket, address )

d,n=GeneratePrivateKey(P,Q,e)
s=readyRecive()
Cipher=Recive(s) #recive the Cipher text
#print(Cipher)
Message=Decrypt(Cipher,n,d)
print(f"Recived Message :{Message} ")



