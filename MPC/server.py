import os
import util
from Value import Value
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import math


def get_PSI_server_input():
    return ['1001', '0908', '1117']

    
def PSI_server(M):
    Y = get_PSI_server_input()
    k = Value()
    k.getRand()
    res = [util.OPRF_Evaluate(k, m) for m in M]
    Y = [Value(bytes_to_long(bytes(y,'utf-8'))) for y in Y]
    ret = [util.OPRF_Evaluate(k, y) for y in Y]
    return (res, ret)


def Average_server(pk, Y):
    enc_Y = [util.Enc(pk, y) for y in Y]
    total= sum(Y)
    size = len(Y)
    return total/size
