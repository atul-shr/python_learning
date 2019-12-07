import pandas as pd
import cx_Oracle as cx

con = cx.connect('hr/HR@LAPTOP-21RC5VEQ:1521/XE')

df = pd.read_sql('select * from all_objects',con)

i=0

while True:
    i += 1
    df.to_csv('largefile.csv',mode='a',index=False)
    if i > 1000:
        break
    if i % 100 == 0 :
        print (i, 'rotation completed')
