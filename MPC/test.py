import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import util
from Value import Value
from client import PSI_client, PSI_client_card, PSU_client_card, Average_client
import time
import random


def get_client_input():
    index = [str(random.randint(1000,9999)) for i in range(1000)]
    age = [random.randint(1,120) for i in range(1000)]
    return (index,age)


def test():
    client_input = get_client_input()
    start_time = time.process_time()
    print(PSU_client_card(client_input[0]))
    end_time = time.process_time()
    print(end_time - start_time)
    start_time = time.process_time()
    print(PSI_client_card(client_input[0]))
    end_time = time.process_time()
    print(end_time - start_time)
    start_time = time.process_time()
    print(Average_client())
    end_time = time.process_time()
    print(end_time - start_time)
    
