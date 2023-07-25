# Script for the third task the DAG will run
# This will load all the local csv files saved previously on our running mysql database
import pandas as pd
import sqlite3, datetime, csv
from table_data import extraction_tables, table_creation, table_insert

# SQLite pseudo connection. This creates a .db file without a running server, as sqlite does not need one
try:
    connection = sqlite3.connect(f'/code/data/sqlite_database_{datetime.date.today()}.db')
    cur = connection.cursor()

    # Filling the SQLite database with the data from PostgreSQL
    for name in extraction_tables:
        try:
            cur.execute(table_creation[name])
            csv_file = open(f"/code/data/postgres/{name}/{datetime.date.today()}/{name}.csv")
            data = csv.reader(csv_file)
            sql = table_insert[name]

            # This skips the header line on our .csv files
            next(data, None)

            for row in data:   
                cur.execute(sql, row)
        except Exception as msg:
            print(msg)

    # Loading the external CSV file into SQLite
    try:
        cur.execute(table_creation['order_details'])
        csv_file = open(f"/code/data/csv/order_details/{datetime.date.today()}/order_details.csv")
        data = csv.reader(csv_file)
        sql = table_insert['order_details']
        next(data, None)
        for row in data:   
                cur.execute(sql, row)
    except Exception as msg:
        print(msg)

    # Committing changes and closing connection
    connection.commit()
    connection.close()
except Exception as msg:
        print(msg)