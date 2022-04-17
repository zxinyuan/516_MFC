# 516project

## Dependencies:  
- [gmpy2](https://gmpy2.readthedocs.io/en/latest/mpz.html#examples) 
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html) 
- [phe](https://pypi.org/project/phe/)
- [psycopg2](https://pypi.org/project/psycopg2/)

## Demo test

There are 2 steps: 1. synthetic data generation; 2. testing 3 queries.

### Synthetic data generation
```
python ./src/data_generation.py
```

### Test 3 queries (avg, intersection, union)

Before running ```./src/main.py```, please create 2 dbusers: 'mfcuser' and 'mfcuser2' and 2 databases: 'mfcdb' and 'mfcdb2' in the local postgres (using the same password '12345678').

```
python ./src/main.py
```
