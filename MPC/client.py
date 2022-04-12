import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import util
from Value import Value
import server
import time


def PSI_client(X):
    X_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    blinded_X = [util.OPRF_Blind(x) for x in X_]
    r = blinded_X[0][0]
    M = []
    for bx in blinded_X:
        M.append(bx[1])
    (Xrk, masked_Y) = server.PSI_server(M)
    masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    pos = []
    for i in range(len(masked_X)):
        if masked_X[i] in masked_Y:
            pos.append(i)           
    return [X[p] for p in pos]


def PSI_client_card(X):
    X = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    blinded_X = [util.OPRF_Blind(x) for x in X]
    r = blinded_X[0][0]
    M = []
    for bx in blinded_X:
        M.append(bx[1])
    (Xrk, masked_Y) = server.PSI_server(M)
    masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    return len([i for i in masked_X if i in masked_Y]) 


def PSU_client_card(X):
    X_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    blinded_X = [util.OPRF_Blind(x) for x in X_]
    r = blinded_X[0][0]
    M = []
    for bx in blinded_X:
        M.append(bx[1])
    (Xrk, masked_Y) = server.PSI_server(M)
    size = len(X) + len(masked_Y)
    return size - PSI_client_card(X)


def Average_client():
    (pk, sk) = util.KeyGen()
    ret = util.Dec(sk, server.Average_server(pk))
    return ret

