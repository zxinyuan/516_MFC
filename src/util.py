import time
import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
from Cryptodome.Util.strxor import strxor
import phe
from phe import paillier
import math
from Value import Value


# Number Theory
field = (2**127)-1
g = Value(31861592127064796386922835392603281441)

def egcd(a, b):
    (x,s,y,t) = (0,1,1,0)
    while b != 0:
        k = a // b
        (a,b) = (b, a%b)
        (x,s,y,t) = (s-k*x,x,t-k*y,y)
    return (s,t)

def inv(a, m):
    if math.gcd(a, m) != 1:
        return None
    else:
        return (egcd(a, m)[0])%m


# OPRF   
def OPRF_Blind(x):
    r = Value()
    r.getRand()
    while math.gcd(r.value, field-1) != 1:
        r = Value()
        r.getRand()
    M = x**r
    return (r,M)

def OPRF_Evaluate(k, M):
    Z = M**k
    return Z

def OPRF_Finalize(r, Z):
    r_1 = r.powinv()
    y = Z**r_1
    return y


# Paillier
def KeyGen():
    (pk, sk) = paillier.generate_paillier_keypair()
    return (pk, sk)

def Enc(pk, m):
    return pk.encrypt(m)

def Dec(sk, c):
    return sk.decrypt(c)

