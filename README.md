# 516project

## Dependencies:  
- [gmpy2](https://gmpy2.readthedocs.io/en/latest/mpz.html#examples) 
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html) 
- [phe](https://pypi.org/project/phe/)

## Synthetic data generation
```
python data_generation.py
```

## Create relational db model in postgreSQL
1. Create table:
```
python db_schema.py create_table
```
2. Insert generated data:
```
python db_schema.py insert_instance
```
