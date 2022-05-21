from RSA import *
filePath='\EncEfficiency\\'
def CalcTime(Message, n_len_start, n_len_end, step):
    Y= []

    with open(filePath+'efficiency.txt','w') as times, open(filePath+'n.txt','w') as n_file:
        for i in range(n_len_start, n_len_end, step):
            
            P= generate_big_prime(i//2)
            Q= generate_big_prime(i-i//2)
            while(Q==P):
                Q=generate_big_prime(i-int(i/2))
            e,n=GeneratePublicKey(P,Q)
            n_file.writelines(Str(n)+'\n')
            start = time.time()
            CipherSent=Encrypt(str(Message),n,e)
            end=time.time()
            times.writelines(str(end-start)+'\n')
            print("len of n:", n.bit_length())
            print(end-start)
            Y.append(end-start)
    return Y

def generateRandomN(n_len_start, n_len_end, step):
    n_All= []
    P_all=[]
    Q_all=[]
    e_ALL=[]
    with open(filePath+'n.txt', 
    'w') as n_file,open(filePath+"e.txt", 
    'w') as e_file, open(filePath+"q.txt", 'w') as q_file, open(filePath+'p.txt', 
    'w') as p_file, open(filePath+'msgs.txt', 
    'r')as messages, open(filePath+'ciphers.txt', 
    'w')as ciphers, open(filePath+'ciphersInt.txt', 'w') as ciphersInt:        
        for i in range(n_len_start, n_len_end, step):
            P= generate_big_prime(i//2)
            p_file.writelines(str(P)+'\n')
            print(P)
            P_all.append(P)
            Q= generate_big_prime(i-i//2)
            print(Q)

            while(Q==P):
                Q=generate_big_prime(i-int(i/2))
            Q_all.append(Q)
            q_file.writelines(str(Q)+'\n')
            e,n=GeneratePublicKey(P,Q)
            e_ALL.append(e)
            e_file.writelines(str(e)+'\n')
            n_All.append(n)
            n_file.writelines(str(n)+'\n')
            msg=str(messages.readline()).rstrip()
            print(msg)
            c, c_int= Encrypt(msg, n, e)
            ciphers.writelines(repr(c)+'\n')
            ciphersInt.writelines(str(c_int)+'\n')
       
    return n_All, e_ALL, P_all, Q_all

def mathematicalBFAttack(n, e, c):
    n=int(n)
    e=int(e)
    c=int(c)
    start = time.time() 
    if n % 2 == 0:
        p = 2
        q = n // 2
        d, n_temp= GeneratePrivateKey(p, q, e)
        decipheredtext, decipheredtextInt= Decrypt(c, n, d, True)
        end=time.time()
        print(end-start)
        return {
            "attacked_message":decipheredtext, 
            "attacked_message_int":decipheredtextInt}
    else:
        for i in range(3, int(n**0.5)+1,2):
                #print(i)
            if n % i == 0:
                p = i
                q = n // i
                end=time.time()
                print(end-start)
                d, n_temp= GeneratePrivateKey(p, q, e)
                decipheredtext, decipheredtextInt= Decrypt(c, n, d, True)
                return {
            "attacked_message":decipheredtext, 
            "attacked_message_int":decipheredtextInt}
                
def attack_BF():
    filePath='BF_Attack_Samples\hacked\\'
    with open(filePath+'n.txt', 
    'r') as n_file,open(filePath+"e.txt", 
    'r') as e_file,open(filePath+'ciphersInt.txt', 'r') as ciphersInt, open(filePath+'times.txt', 
    'w') as execTimes,open(filePath+'p_hacked.txt', 
    'w') as p_hacked,open(filePath+'q_hacked.txt', 
    'w') as q_hacked,open(filePath+'AttackedMsgs.txt', 
    'w') as AttackedMsgs: 
        decipheredtext = 'failed to attack'
        decipheredtextInt= None
        ## reading ciphers
        start_bit_size=8
        for n_line in n_file:
            n=int(n_line.rstrip())
            e= int(e_file.readline().rstrip())
            c = int(ciphersInt.readline().rstrip())
            print(c)
            print(start_bit_size)
            start_bit_size+=2
            start = time.time() 
            if n % 2 == 0:
                p = 2
                q = n // 2
                end=time.time()
                print(end-start)
                d, n_temp= GeneratePrivateKey(p, q, e)
                decipheredtext, decipheredtextInt= Decrypt(c, n, d, True)
                execTimes.writelines(str(end-start)+'\n')
                p_hacked.writelines(str(p)+'\n')
                q_hacked.writelines(str(q)+'\n')
                print(decipheredtext)
                print(decipheredtextInt)
                AttackedMsgs.writelines(str(decipheredtext)+'\n')
                #return decipheredtext, decipheredtextInt
            else:
                for i in range(3, int(n**0.5)+1,2):
                        #print(i)
                    if n % i == 0:
                        p = i
                        q = n // i
                        print(p)
                        print(q)
                        end=time.time()
                        print(end-start)
                        d, n_temp= GeneratePrivateKey(p, q, e)
                        decipheredtext, decipheredtextInt= Decrypt(c, n, d, True)
                        
                        execTimes.writelines(str(end-start)+'\n')
                        p_hacked.writelines(str(p)+'\n')
                        q_hacked.writelines(str(q)+'\n')
                        print(decipheredtext)
                        AttackedMsgs.writelines(str(decipheredtext)+'\n')
                        break
                    #return decipheredtext, decipheredtextInt
    #return decipheredtext, decipheredtextInt
def plotBruteForceAttackEfficiency():
    filePath='BF_Attack_Samples\hacked\\'
    n_values=[]
    timeValues=[]
    with open(filePath+'n.txt', 'r') as n_file, open(filePath+'times.txt', 
    'r') as execTimes: 
        n_bits=8
        n_sizes=[]
        for n_line in n_file:
            
            time=execTimes.readline().rstrip()
            if(time==''):
                break
            n_sizes.append(n_bits)
            n=int(n_line.rstrip())
            n_values.append(n)
            timeValues.append(float(time))
            n_bits+=2
        fig, ax = plt.subplots()
        ax.set_xticklabels(n_values)
        ax.plot(n_sizes, timeValues, linewidth=2.0)
        plt.xlabel("Key Values (decimal)")
        plt.ylabel("Execution Time (decimal)")
        plt.show()
        
#n_All, e_ALL, P_all, Q_all= generateRandomN(8, 76, 2)
#attack_BF()

# Y= CalcTime("Hi01222", 64, 2049, 256)
# X=  list(range(64, 2049,256))
# print(len(X))
# print(Y)
# # #plt.style.use('_mpl-gallery')
# fig, ax = plt.subplots()
# ax.plot(X, Y, linewidth=2.0)
# plt.show()

plotBruteForceAttackEfficiency()



#P,Q=ReadfromFile()
#print(GeneratePublicKey(P,Q))   

# exponent = 23917
# modulo = 1000000007 * 1000000009
# ciphertext = Encrypt("HiDonia", modulo, exponent)
# message = Decrypt(ciphertext,modulo , InvertModulo(exponent,(1000000006)*(1000000008)))
# print(message)    
