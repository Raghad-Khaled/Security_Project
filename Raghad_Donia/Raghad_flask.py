from ast import Mod
from os import system
from RSA import *
import socket
import sys

CHAT =1
FILE =2
ATTACK=3
# Tha Modes of operation 1)chat 2)file read and write 3)attack  
#Mode =int(sys.argv[1])

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
        msg = s.recv(8000).decode()
        return msg
def CorrectOut(msgReceivd):
    correctedMsg=''
    i=0
    while(i<len(str(msgReceivd)) and str(msgReceivd[i]).isdigit()):
        correctedMsg+=msgReceivd[i]
        i+=1
    print("recived not corrected",msgReceivd)
    print("recived corrected",correctedMsg)
    return correctedMsg
def getKeys(genPQ=True,p=0,q=0):
    #send public key to user B
    if(genPQ==True):
        P,Q=ReadfromFile('PQ.txt')
    else:
        P,Q=p,q
    e,n=GeneratePublicKey(P,Q)
    d,n=GeneratePrivateKey(P,Q,e)
    data= {
            "raghad_PUe":str(e),
            "raghad_n":str(n),
            "raghad_PRd":str(d),
            "P_raghad":P,
            "Q_raghad":Q
        }
    return data

###############for flask#####################
def initRaghad(message="dummy",genPQ=True,p=0,q=0,reciever=True):
    #send public key to user B
    if(genPQ==True):
        P,Q=ReadfromFile('PQ.txt')
    else:
        P,Q=p,q
    e,n=GeneratePublicKey(P,Q)

    d,n=GeneratePrivateKey(P,Q,e)
    if(reciever):
        clientsocket, address =readySend()
        Send(str(e),clientsocket, address )
        Send(str(n),clientsocket, address )
        
        #recive public key from user B
        s=readyRecive()
        e_B=int((Recive(s))) #recive the public key for reciver
        n_B=int((Recive(s)))
        RecCipher=Recive(s) #recive the Cipher text
        print("testttt",RecCipher)
        RecMessage, recMsgInt=Decrypt(RecCipher,n,d)
        if(RecMessage=='0'):
            print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it") #message lenth can be up to 66
        else:
            print(f"Donia :{RecMessage} ")
        data= {
            "message_recieved_encrypted":repr(RecCipher),
            "message_recieved_decrypted":RecMessage,
            "raghad_PUe":e,
            "raghad_n":n,
            "raghad_PRd":d,
            "donia_PUn":n_B,
            "donia_PUe":e_B,
        }
    else: ## sender
        #recive public key from user B
        s=readyRecive()
        e_B=int((Recive(s))) 
        n_B=int((Recive(s)))
    
        clientsocket, address =readySend()
        Send(str(e),clientsocket, address )
        Send(str(n),clientsocket, address )
        print("n: ",str(n))
        Message = message
        CipherSent, CipherSentInt=Encrypt(str(Message),n_B,e_B) # encript with the publick key of reciver
        if(CipherSent != false):
            Send(CipherSent,clientsocket, address ) #send the cipher message to reciver
        else:
            CipherSent, CipherSentInt=Encrypt(str(0),n_B,e_B)
            Send(CipherSent,clientsocket, address ) #send the cipher message to reciver
    
        data= {
            "message_sent_encrypted":repr(CipherSent),
            "message_sent":Message,
            "raghad_PUe":e,
            "raghad_n":n,
            "raghad_PRd":d,
            "donia_PUn":n_B,
            "donia_PUe":e_B,
        }
    return data

#######################################################
## only comment the following if you want to run from console
#######################################################

def initRaghadForAttack(index):
    index=int(index)
    e_file_cca=open("CCA_Attack_Samples\e.txt", 'r')
    n_file_cca=open("CCA_Attack_Samples\\n.txt", 'r')
    pq_CCA= open("CCA_Attack_Samples\PQ.txt",'r')
    e_CCA=[]
    n_CCA=[]
    P_CCA=[]
    Q_CCA=[]

    for n_line_cca in n_file_cca:

        e_CCA.append(int(e_file_cca.readline().rstrip()))
        n_CCA.append(int(n_line_cca.rstrip()))
        P_CCA.append(int(pq_CCA.readline().rstrip()))
        Q_CCA.append(int(pq_CCA.readline().rstrip()))
        
        #send public key to user B
    print(len(e_CCA))
    print(len(n_CCA))
    print(len(P_CCA))
    print(len(Q_CCA))

    P=P_CCA[index]
    Q=Q_CCA[index]
    e=e_CCA[index]
    n=n_CCA[index]
    print("P: ",P)
    print("Q: ",Q)

    d,n=GeneratePrivateKey(P,Q,e)

    clientsocket, address =readySend()

    #recive public key from user B
    s=readyRecive()

    while True:
        Cipher=Recive(s) #recive the Cipher Int
        print("recieved cipher",Cipher)
        Message, MessageInt=Decrypt(int(Cipher),n,d, isInt=True)
        if(Message=='0'):
            print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it") #message lenth can be up to 66
        
        Send(Message,clientsocket, address ) #send the meaasege to attaker after decreption
        return {"res": 1}
     
#############################################
#runFromConsole()
#############################################