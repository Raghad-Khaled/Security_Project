#from email.message import Message
from RSA import *
import socket
import sys

CHAT =1
FILE =2
# Tha Modes of operation 1)chat 2)file read and write 3)attack  
#Mode =int(sys.argv[1])

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
        msg = s.recv(8000).decode()
        # if(correctOut):
        #     correctedMsg=''
        #     i=0
        #     while(i<len(str(msg)) and str(msg[i]).isdigit()):
        #         correctedMsg+=msg[i]
        #         i+=1
        #     print("recived not corrected",msg)
        #     print("recived corrected",correctedMsg)
        #     return correctedMsg
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
#########################################
def getKeys(genPQ=True,p=0,q=0):
    #send public key to user B
    if(genPQ==True):
        P,Q=ReadfromFile('E:\cryptography\project\Security_Project4\Raghad_Donia\PQ2.txt')
    else:
        P,Q=p,q
    e,n=GeneratePublicKey(P,Q)
    d,n=GeneratePrivateKey(P,Q,e)
    data= {
           "donia_PUe":str(e),
            "donia_n":str(n),
            "donia_PRd":str(d),
            "P_donia":P,
            "Q_donia":Q
        }
    return data

###############for flask#####################
def initDonia(message="dummy",genPQ=True,p=0,q=0,reciever=False):
    #send public key to user A
    if(genPQ==True):
        P,Q=ReadfromFile('PQ2.txt')
    else:
        P,Q= p,q
    e,n=GeneratePublicKey(P,Q)
    d,n=GeneratePrivateKey(P,Q,e)
    print("Donia:%d",n)
    if(not reciever):
        #recive public key from user A
        s=readyRecive()
        e_A=int((Recive(s))) #recive the public key for reciver
        n_A=int((Recive(s)))

        
        clientsocket, address =readySend()
        Send(str(e),clientsocket, address )
        Send(str(n),clientsocket, address )

        Message = message
        CipherSent,CipherSentInt=Encrypt(str(Message),n_A,e_A) # encrypt with the public key of reciver
        print("CS", CipherSent)
        if(CipherSent != false):
            Send(CipherSent,clientsocket, address ) #send the cipher message to reciver
        else:
            CipherSent=Encrypt(str(0),n_A,e_A)
            Send(CipherSent,clientsocket, address ) #send the cipher message to reciver
        data= {
        "message_sent_encrypted":repr(CipherSent),
        "message_sent":Message,
        "donia_PUe":e,
        "donia_n":n,
        "donia_PRd":d,
        "raghad_PUn":n_A,
        "raghad_PUe":e_A,
        }
    
    else: ## receiver
        clientsocket, address =readySend()
        Send(str(e),clientsocket, address )
        Send(str(n),clientsocket, address )

        #recive public key from user A
        s=readyRecive()
        e_A=int((Recive(s))) #recive the public key for reciver
        n_A=int((Recive(s)))
        
        RecCipher=Recive(s) #recive the Cipher text
        RecMessage, recMsgInt=Decrypt(RecCipher,n,d)
        if(RecMessage=='0'):
            print("The Message Sended is too long, please incerase P & Q and resend the public key to can recive it")
        else:
            print(f"Raghad :{RecMessage} ")    

        data= {
        "message_recieved_encrypted":repr(RecCipher),
        "message_recieved_decrypted":RecMessage,
        "donia_PUe":e,
        "donia_n":n,
        "donia_PRd":d,
        "raghad_PUn":n_A,
        "raghad_PUe":e_A,
        }
    return data     
######################################################

#######################################################
