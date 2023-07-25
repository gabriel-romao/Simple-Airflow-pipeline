# This is the last task the DAG will run
# It will run a query that joins orders and order_details, and create a csv with the result
import sqlite3, datetime, csv

# Connection to the database
try:
    connection = sqlite3.connect(f'/code/data/sqlite_database_{datetime.date.today()}.db')
    
    cur = connection.cursor()

    # Join query for showing orders and their details
    sql = '''SELECT *
    FROM orders AS a 
    INNER JOIN order_details AS b ON (a.order_id = b.order_id)'''

    cur.execute(sql)
    result = cur.fetchall()

    csv_pointer = open(f"/code/data/final_query.csv", 'w')
    csv_file = csv.writer(csv_pointer)
    csv_file.writerows(result)

    csv_pointer.close()
    connection.close()

except Exception as msg:
    print(msg)