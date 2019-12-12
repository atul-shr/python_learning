import pandas as pd
import cx_Oracle as cx
import datetime

con = cx.connect('pharma/pharma@LAPTOP-21RC5VEQ:1521/XE')

current_time = datetime.datetime.now()
old_time = datetime.datetime.now()
df_dur = pd.DataFrame()

for chunks in (pd.read_sql(sql='select * from inventory',con=con,chunksize=10000)):
    current_time = datetime.datetime.now()
    dur = current_time - old_time
    df_dur['DURATION'] = dur.total_seconds()
     
    # print('Duration time is : ',dur.total_seconds()) 
    chunks.to_csv('bigfile.csv',mode='a',index=False)
    old_time =  current_time

print(df_dur)
