import os
import util
from Value import Value
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import math
import random


def get_PSI_server_input():
    index = [str(random.randint(1000,9999)) for i in range(1000)]
    age = [random.randint(1,120) for i in range(1000)]
    return (index,age)

    
def PSI_server(M):
    Y = get_PSI_server_input()[0]
    k = Value()
    k.getRand()
    res = [util.OPRF_Evaluate(k, m) for m in M]
    Y = [Value(bytes_to_long(bytes(y,'utf-8'))) for y in Y]
    ret = [util.OPRF_Evaluate(k, y) for y in Y]
    return (res, ret)


def Average_server(pk):
    Y = get_PSI_server_input()[1]
    enc_Y = [util.Enc(pk, y) for y in Y]
    total= sum(enc_Y)
    size = len(Y)
    return total/size
