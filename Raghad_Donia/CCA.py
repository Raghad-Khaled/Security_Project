#from email.message import Message
from email import message
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
############ used in the flask app
def CCA_Flask(cipher, e, n):
    e=int(e)
    n=int(n)
    s=readyRecive()
    clientsocket, address =readySend()
    Cipher= cipher
    r=Generater(n)
    
    Cipher_dash=ConvertToStr((int(Cipher) * PowMod(r,e,n))%n)
    Cipher=(int(Cipher) * PowMod(r,e,n))%n
    Send( str(Cipher) ,clientsocket, address ) #send the cipher message to reciver
    Y=ConvertToInt(Recive(s))
    Message =ConvertToStr( (Y * InvertModulo(r,n))%n )
    print(f"Donia Message Attacked :{Message} ") 
    return {"message_attacked":Message}
#recive public key from user A

# e_A=int(Recive(s)) #recive the public key for reciver
# n_A=int(Recive(s))
def runCCAFromConsole():
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





## uncomment in case you want to run from console

#runCCAFromConsole()










#CCA_Flask(150025913213568562613921942701247436154532459645391238581954041631015987544185740601806470459009566151393097481560749885740529816149269224958492393821496064445,
#2459639651678615325536389733720996173030525624791787152254618870348757764252197465774046323980696678414080006268647089707275956014734483888725255342514098121761,
#7682019348973114680000755378516891203511930863764635761888988440652451026611373091311745520207225288025429195215857834592026577549770197040351322157865717247);
# with open('CCA_Attack_Samples\MessagesToAttack.txt', 
#     'r') as plainTexts,open('CCA_Attack_Samples\ciphers.txt',
#     'w') as ciphers,  open('CCA_Attack_Samples\\n.txt', 
#     'w')as n_file,  open('CCA_Attack_Samples\\e.txt', 
#     'w')as e_file, open("CCA_Attack_Samples\PQ.txt", "w")as pq: 
#         ## reading ciphers
        
#         for plainText in plainTexts:
#             size_n=len(plainText.rstrip())*8+2               
#             p=generate_big_prime(size_n//2)
#             q=generate_big_prime(size_n - size_n//2)
#             pq.writelines(str(p)+'\n')
#             pq.writelines(str(q)+'\n')
#             e, n=GeneratePublicKey(p, q)
#             e_file.writelines(str(e)+'\n')
#             n_file.writelines(str(n)+'\n')
#             cipher, cipherInt= Encrypt(plainText.rstrip(),
#             n,
#             e
#             )
#             d, n=GeneratePrivateKey(p, q, e)

#             messageDec, messageInt= Decrypt(cipherInt, n, d, isInt=True)
#             print(messageDec)
#             ciphers.writelines(str(cipherInt)+'\n')
