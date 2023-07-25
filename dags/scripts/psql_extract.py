# Script for the first task the DAG will run
# Extracts all tables' data from our PostgreSQL database, and saves them locally as .csv files

import psycopg2, csv, os, datetime
from table_data import table_columns, extraction_tables

# Connection to PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname = 'northwind',
        user = 'northwind_user', 
        host = 'postgres', 
        password = 'thewindisblowing')
    cur = connection.cursor()

# Folder and CSV creation
    for name in extraction_tables:
        try:
            sql = f"SELECT * FROM {name}"
            cur.execute(sql)
            result = cur.fetchall()
            os.makedirs(f"/code/data/postgres/{name}/{datetime.date.today()}")
            csv_pointer = open(f"/code/data/postgres/{name}/{datetime.date.today()}/{name}.csv", 'w')
            csv_file = csv.writer(csv_pointer)
            csv_file.writerow(table_columns[name])
            csv_file.writerows(result)
            csv_pointer.close()
        except OSError as read_msg:
            print(read_msg)

    cur.close()
    
except OSError as connect_msg:
    print(connect_msg)