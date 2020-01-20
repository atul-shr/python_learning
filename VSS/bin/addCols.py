import cx_Oracle
import pandas as pd
import numpy as np
import datetime
import os
import sqlalchemy as sa

def setLevel(num):
    level = ''
    if num < 0:
        level = 'Low'
    elif num > 0 and num < 50 :
        level = 'Medium'
    elif num > 50:
        level = 'Big'
    return level

# con = cx.connect('pharma/pharma@LAPTOP-21RC5VEQ:1521/XE')

oracle_db = sa.create_engine('oracle+cx_oracle://pharma:pharma@LAPTOP-21RC5VEQ:1521/XE')
con = oracle_db.connect()

now_time = datetime.datetime.now()
then_time = datetime.datetime.now()
no_of_rec = 0
try:
    os.remove('final_out.csv')
    print("File Removed!")
except:
    print("File Not Available!")     

for chunks in (pd.read_sql(sql='select * from inventory where rownum < 101',con=con,chunksize=100000)):
    # print(chunks.columns)
    now_time = datetime.datetime.now() - then_time
    chunks['type'] = chunks['remain_qty'].apply(setLevel)
    # chunks.to_csv('final_out.csv',mode='a',index=False,sep='|')
    # print(len(chunks),'done')
    print(chunks)
    chunks.to_sql(name='INVENTORY_WRITE',con=con,if_exists='append',index=False)
    no_of_rec += len(chunks)
    print('Processed file with - ', no_of_rec, 'in : ', now_time.total_seconds())
    then_time = datetime.datetime.now()
