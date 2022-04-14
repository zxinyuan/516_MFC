import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import util
from Value import Value
import server
import time
import math


def PSI_client(X, Y):
    X_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    r = Value()
    r.getRand()
    while math.gcd(r.value, util.field-1) != 1:
        r = Value()
        r.getRand()
    blinded_X = [util.OPRF_Blind(x, r) for x in X_]
    (Xrk, masked_Y) = server.PSI_server(Y, blinded_X)
    masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    pos = []
    for i in range(len(masked_X)):
        if masked_X[i] in masked_Y:
            pos.append(i)           
    return [X[p] for p in pos]


def PSI_client_card(X, Y):
    X = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    blinded_X = [util.OPRF_Blind(x) for x in X]
    r = blinded_X[0][0]
    M = []
    for bx in blinded_X:
        M.append(bx[1])
    (Xrk, masked_Y) = server.PSI_server(Y, M)
    masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    return len([i for i in masked_X if i in masked_Y]) 


def PSU_client_card(X, Y):
    X_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in X]
    blinded_X = [util.OPRF_Blind(x) for x in X_]
    r = blinded_X[0][0]
    M = []
    for bx in blinded_X:
        M.append(bx[1])
    (Xrk, masked_Y) = server.PSI_server(Y, M)
    size = len(X) + len(masked_Y)
    return size - PSI_client_card(X, Y)


def Average_client(Y):
    (pk, sk) = util.KeyGen()
    ret = util.Dec(sk, server.Average_server(Y, pk))
    return ret
