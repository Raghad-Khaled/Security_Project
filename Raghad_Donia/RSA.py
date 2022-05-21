from ast import Str
import random
from sqlalchemy import false
import time
import matplotlib.pyplot as plt
from random import randint
import sys
sys.setrecursionlimit(5000)
tests_count= 10000
def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n-1)
        if is_prime_optimized(p, tests_count):
            return p
def is_prime_optimized(n, testsNumber):
    ## applying fermat's primality test
    if n == 1:
        return False
    if testsNumber >= n:
        testsNumber = n - 1
    for x in range(testsNumber):
        rand = randint(1, n - 1)
        if pow(rand, n-1, n) != 1:
            return False
    return True

def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)


def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n # we don't want -ve integers
    return b

def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)        

# this is an R2L recursive implementation that works for large integers
def PowMod(a, n, mod): 
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod    

def isprime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1)) 


def ReadfromFile(filename):
    with open(filename) as f:
        try:
            P =int(f.readline())
            Q = int(f.readline())
            return(P,Q)
        except ValueError:
            print("Can't generat keys as P and Q must be integers")


       


def GeneratePublicKey(P,Q):
    P= int(P)
    Q= int(Q)
    n=P*Q
    phain=(P-1)*(Q-1)
    e=random.randint(3, n-1)
    while GCD(e, phain) !=1:
        e=random.randint(3, n-1)    
    return(e,n)


def Generater(n):
    r=random.randint(3, n-1)
    while GCD(r, n) !=1:
        r=random.randint(3, n-1)    
    return r   


def GeneratePrivateKey(P,Q,e):
    P= int(P)
    Q= int(Q)
    n=P*Q
    phain=(P-1)*(Q-1)
    d=InvertModulo(e,phain)
    return(d,n)

def Encrypt(M, n, e):
    Messageint=ConvertToInt(M)
    if(Messageint > n):
        return false
    Cipherint=PowMod(Messageint,e,n)
    Cipher =ConvertToStr(Cipherint)
    return Cipher, Cipherint

def Decrypt(C, n, d, isInt=False):
    Chipherint=C
    if(isInt==False):
        Chipherint=ConvertToInt(C)
    MessageInt=PowMod(Chipherint,d,n)
    Message =ConvertToStr(MessageInt)
    return Message,MessageInt
 
