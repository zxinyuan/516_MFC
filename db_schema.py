import psycopg2
import numpy as np
from psycopg2 import Error
import sys

'''
local data schema: 
students: student_id (PK), age, first_name, last_name
healthcenters: center_id (PK), location_id
activity: actitvity_id (PK), location_id, date
participation: participationid (PK), activity_id, student_id
location: location_id (PK), address, city
testlog: test_id (PK), result, date, student_id
vaccination: brand_id (PK)
vaccinationhistory: history_id (PK), brand_id, student_id, dose_number, date
'''


def create_schema(username, password, database):

    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        # SQL query to create tables
        create_table_query = '''CREATE TABLE STUDENTS
          (studentid DECIMAL(7) PRIMARY KEY  NOT NULL,
          age INTEGER NOT NULL,
          firstname VARCHAR(20) NOT NULL,
          lastname  VARCHAR(20) NOT NULL); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE LOCATION
          (locationid DECIMAL(9) PRIMARY KEY  NOT NULL,
          address VARCHAR(100) NOT NULL,
          city VARCHAR(20) NOT NULL); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE HEALTHCENTERS
          (centerid DECIMAL(3) PRIMARY KEY  NOT NULL,
          locationid DECIMAL(9) NOT NULL,
          FOREIGN KEY (locationid) REFERENCES LOCATION(locationid)); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE ACTIVITY
          (activityid DECIMAL(5) PRIMARY KEY  NOT NULL,
          locationid DECIMAL(9) NOT NULL,
          date DATE NOT NULL,
          FOREIGN KEY (locationid) REFERENCES LOCATION(locationid)); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE PARTICIPATION
          (participationid DECIMAL(9) PRIMARY KEY  NOT NULL,
          activityid DECIMAL(5) NOT NULL,
          studentid DECIMAL(7) NOT NULL,
          FOREIGN KEY (studentid) REFERENCES STUDENTS(studentid),
          FOREIGN KEY (activityid) REFERENCES ACTIVITY(activityid)); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE TESTLOG
          (testid DECIMAL(9) PRIMARY KEY  NOT NULL,
          result BOOLEAN NOT NULL,
          date DATE NOT NULL,
          studentid DECIMAL(7) NOT NULL,
          FOREIGN KEY (studentid) REFERENCES STUDENTS(studentid)); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE VACCINATION
          (brandid DECIMAL(5) PRIMARY KEY  NOT NULL); '''
        cursor.execute(create_table_query)

        create_table_query = '''CREATE TABLE VACCINATIONHISTORY
          (historyid DECIMAL(9) PRIMARY KEY  NOT NULL,
          brandid DECIMAL(5) NOT NULL,
          studentid DECIMAL(7) NOT NULL,
          dosenumber DECIMAL(1) NOT NULL,
          date DATE NOT NULL,
          FOREIGN KEY (brandid) REFERENCES VACCINATION(brandid),
          FOREIGN KEY (studentid) REFERENCES STUDENTS(studentid)); '''
        cursor.execute(create_table_query)

        connection.commit()
        print("8 tables created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_data(username, password, database, table, data_instance):
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      database=database)

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

        # SQL query to insert instances into table
        for i in range(len(data_instance)):
            a = 'INSERT INTO Article (pubkey'
            b = ') VALUES (\'' + Article[i]['pubkey'] + "\'"
            c = ')'
            if 'title' in Article[i].keys():
                a = a + ', title'
                b = b + ', \'' + Article[i]['title'].replace('\'', '') + "\'"
            if 'journal' in Article[i].keys():
                a = a + ', journal'
                b = b + ', \'' + Article[i]['journal'].replace('\'', '') + "\'"
            if 'year' in Article[i].keys():
                a = a + ', year'
                b = b + ', ' + Article[i]['year']
            insert_query = a + b + c
            print(insert_query)
            cursor.execute(insert_query)
            print('==> inserted one instance into Article')
        connection.commit()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':

  username = 'mfcuser'
  password = '12345678'
  database = 'mfcdb'

  args = sys.argv[1]
  if args == 'create_table':
    create_schema(username, password, database)
  elif args == 'insert_instances':
    insert_instances(username, password, database)
  else:
    print('==> no such argument!')
