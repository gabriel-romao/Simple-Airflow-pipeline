# Script for the second task the DAG will run
# This will copy the .csv file from our local system into a proper folder with datetime

import shutil, os, datetime

os.makedirs(f"/code/data/csv/order_details/{datetime.date.today()}")
shutil.copyfile("/code/data/order_details.csv", f"/code/data/csv/order_details/{datetime.date.today()}/order_details.csv")