import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import util
from Value import Value
from client import PSI_client, PSI_client_card, PSU_client_card
import time


def test():
    start_time = time.process_time()
    print(PSU_client_card(['1001', '0908', '1117']))
    end_time = time.process_time()
    print(end_time - start_time)
    start_time = time.process_time()
    print(PSI_client(['1001', '7']))
    end_time = time.process_time()
    print(end_time - start_time)
    
