import cx_Oracle as cx
import pandas as pd
import numpy as np
import datetime
import os

def setLevel(num):
    level = ''
    if num < 0:
        level = 'Low'
    elif num > 0 and num < 50 :
        level = 'Medium'
    elif num > 50:
        level = 'Big'
    return level

con = cx.connect('pharma/pharma@LAPTOP-21RC5VEQ:1521/XE')
now_time = datetime.datetime.now()
then_time = datetime.datetime.now()
no_of_rec = 0
try:
    os.remove('final_out.csv')
    print("File Removed!")
except:
    print("File Not Available!")    

for chunks in (pd.read_sql(sql='select * from inventory',con=con,chunksize=100000)):
    now_time = datetime.datetime.now() - then_time
    chunks['TYPE'] = chunks['REMAIN_QTY'].apply(setLevel)
    chunks.to_csv('final_out.csv',mode='a',index=False,sep='|')
    # print(len(chunks),'done')
    no_of_rec += len(chunks)
    print('Processed file with - ', no_of_rec, 'in : ', now_time.total_seconds())
    then_time = datetime.datetime.now()
