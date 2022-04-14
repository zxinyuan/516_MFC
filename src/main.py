from db_schema import create_schema, insert_instance, query_sql_avg_age, query_sql_intersect, query_sql_union
from client import *
from server import *
import util
from Value import Value

import time
import os
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import math


all_usernames = ["mfcuser", "mfcuser2"]
all_passwords = ["12345678", "12345678"]
all_databases = ["mfcdb", "mfcdb2"]


def setup():
    for i in range(2):
        username = all_usernames[i]
        password = all_passwords[i]
        database = all_databases[i]

        create_schema(username, password, database)
        insert_instance(username, password, database, 0.7)


def query1():
    """
    SELECT S.age
    FROM STUDENTS S
    JOIN TESTLOG T ON S.studentid = T.studentid
    WHERE T.result = TRUE
    """
    start_time = time.time()
    # get query result
    res = []
    for i in range(2):
        username = all_usernames[i]
        password = all_passwords[i]
        database = all_databases[i]
        res.append(query_sql_avg_age(username, password, database))
    res1 = res[0]
    res2 = res[1]
    sql_time = time.time()

    for i in range(len(res1)):
        res1[i] = int(res1[i][0])
    for i in range(len(res2)):
        res2[i] = int(res2[i][0])
    # encrypt
    (pk1, sk1) = util.KeyGen()
    enc_res1 = [util.Enc(pk1, y) for y in res1]
    (pk2, sk2) = util.KeyGen()
    enc_res2 = [util.Enc(pk2, y) for y in res2]
    # decrpyt
    avg1 = util.Dec(sk1, sum(enc_res1)/len(res1))
    avg2 = util.Dec(sk2, sum(enc_res2)/len(res2))
    # avg
    avg_enc = (avg1 * len(enc_res1) + avg2 * len(enc_res2)) / (len(enc_res2) + len(enc_res2))
    end_time = time.time()

    sum_ans = 0
    for tmp in res1 + res2:
        sum_ans += tmp
    avg_ans = sum_ans / (len(res1) + len(res2))

    return avg_enc, avg_ans, sql_time - start_time, end_time - start_time


def query2():
    """
    SELECT A.locationid
    FROM ACTIVITY A, PARTICIPATION P, TESTLOG T
    WHERE A.activityid = P.activityid AND P.studentid = T.studentid
        AND T.result = true AND T.date <= A.date
    """
    start_time = time.time()
    res = []
    for i in range(2):
        username = all_usernames[i]
        password = all_passwords[i]
        database = all_databases[i]
        res.append(query_sql_union(username, password, database))
    res1 = res[0]
    res2 = res[1]
    sql_time = time.time()
    for i in range(len(res1)):
        res1[i] = '0' * (7-len(str(res1[i][0]))) + str(res1[i][0])
    for i in range(len(res2)):
        res2[i] = '0' * (7-len(str(res2[i][0]))) + str(res2[i][0])
    # encrypt res2
    r = Value()
    r.getRand()
    while math.gcd(r.value, util.field-1) != 1:
        r = Value()
        r.getRand()
    res2_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in res2]
    res2_ = [util.OPRF_Blind(x, r) for x in res2_]
    # encrypt res1
    k = Value()
    k.getRand()
    Xrk = [util.OPRF_Evaluate(k, m) for m in res2_]
    res1_ = [Value(bytes_to_long(bytes(y,'utf-8'))) for y in res1]
    masked_Y = [util.OPRF_Evaluate(k, y) for y in res1_]
    # encrypt res2
    r = Value()
    r.getRand()
    while math.gcd(r.value, util.field-1) != 1:
        r = Value()
        r.getRand()
    masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    pos = []
    for i in range(len(masked_X)):
        if masked_X[i] not in masked_Y:
            pos.append(i)
    # get union
    union_enc_ = [res2[p] for p in pos] + res1
    union_enc = []
    [union_enc.append(x) for x in union_enc_ if x not in union_enc]

    end_time = time.time()

    dict = {}
    for tmp in res1 + res2:
        dict[tmp] = 1
    union_ans = list(dict.keys())

    return union_enc, union_ans, sql_time - start_time, end_time - start_time


def query3():
    """
    SELECT A.activity_id
    FROM ACTIVITY A
    WHERE NOT EXISTS(
        SELECT *
        FROM PARTICIPATION P, TESTLOG T
        WHERE A.activityid = P.activityid AND P.studentid = T.studentid
            AND T.result = true and T.date <= A.date
    )
    """
    start_time = time.time()
    # get query result
    res = []
    for i in range(2):
        username = all_usernames[i]
        password = all_passwords[i]
        database = all_databases[i]
        res.append(query_sql_intersect(username, password, database))
    res1 = res[0]
    res2 = res[1]
    sql_time = time.time()
    for i in range(len(res1)):
        res1[i] = '0' * (7-len(str(res1[i][0]))) + str(res1[i][0])
    for i in range(len(res2)):
        res2[i] = '0' * (7-len(str(res2[i][0]))) + str(res2[i][0])
    # encrypt res2
    # res2_ = [Value(bytes_to_long(bytes(x,'utf-8'))) for x in res2]
    # res2_ = [util.OPRF_Blind(x) for x in res2_]
    # r = res2_[0][0]
    # M = []
    # for bx in res2_:
    #     M.append(bx[1])
    # # encrypt res1
    # k = Value()
    # k.getRand()
    # Xrk = [util.OPRF_Evaluate(k, m) for m in M]
    # res1_ = [Value(bytes_to_long(bytes(y,'utf-8'))) for y in res1]
    # masked_Y = [util.OPRF_Evaluate(k, y) for y in res1_]
    # print(masked_Y)
    # # encrypt res2
    # masked_X = [util.OPRF_Finalize(r, xrk) for xrk in Xrk]
    # print(masked_X)
    # pos = []
    # for i in range(len(masked_X)):
    #     if masked_X[i] in masked_Y:
    #         pos.append(i)
    # # get intersect
    # intersect_enc = [res2[p] for p in pos]

    intersect_enc = PSI_client(res1, res2)

    end_time = time.time()   

    dict = {}
    for tmp in res1:
        dict[tmp] = 1
    intersect_ans = []
    for tmp in res2:
        if tmp in dict:
            intersect_ans.append(tmp)

    return intersect_enc, intersect_ans, sql_time - start_time, end_time - start_time


if __name__ == "__main__":
    setup()

    print('===================== Q1 ======================')
    avg_enc, avg_ans, sql_time, tot_time = query1()
    print('--- MPC result ---')
    print(avg_enc)
    print('--- Answer ---')
    print(avg_ans)
    print('--- Same? ---')
    print(avg_enc == avg_ans)
    print('--- SQL Time/Total Time (in secs) ---')
    print(f'{sql_time}/{tot_time}')

    print('===================== Q2 ======================')
    union_enc, union_ans, sql_time, tot_time = query2()
    union_enc.sort()
    union_ans.sort()
    print('--- MPC result ---')
    print(union_enc)
    print('--- Answer ---')
    print(union_ans)
    print('--- Same? ---')
    flag = True
    if len(union_enc) != len(union_ans):
        flag = False
    for i in range(len(union_enc)):
        if union_enc[i] != union_ans[i]:
            flag = False
            break
    print(flag)
    print('--- SQL Time/Total Time (in secs) ---')
    print(f'{sql_time}/{tot_time}')

    print('===================== Q3 ======================')
    intersect_enc, intersect_ans, sql_time, total_time = query3()
    intersect_enc.sort()
    intersect_ans.sort()
    print('--- MPC result ---')
    print(intersect_enc)
    print('--- Answer ---')
    print(intersect_ans)
    print('--- Same? ---')
    flag = True
    if len(intersect_enc) != len(intersect_ans):
        flag = False
    for i in range(len(intersect_enc)):
        if intersect_enc[i] != intersect_ans[i]:
            flag = False
            break
    print(flag)
    print('--- SQL Time/Total Time (in secs) ---')
    print(f'{sql_time}/{total_time}')
