import pandas as pd
import datetime
import numpy as np
import cx_Oracle as cx

# 1. trunc date 
# 2. footer removal
# 3. generic paths

con = cx.connect('hr/HR@LAPTOP-21RC5VEQ:1521/XE')
cur = con.cursor()

cur.execute("Truncate table test_chunks")

insStr = 'insert into test_chunks(col1,col2,col3,col4,col_date) values (:1,:2,:3,:4,:5)'

# for chunks in pd.read_csv('srcsmall.dat',delimiter="|",chunksize=50000,header=1):
#     chunks['coldate'] = datetime.datetime.now().date()
#     print(chunks.shape)
#     cur.executemany(insStr,chunks.where((pd.notnull(chunks)), None).values.tolist())
#     con.commit()
    
    
start = datetime.datetime.now()

want=[]

f = pd.read_csv('srcsmall.dat',delimiter="|",header=1,iterator = True)

go = True
while go:
    try:
        # want.append(f.get_chunk(50000))
        data_df = f.get_chunk(50000)
        data_df['coldate'] = datetime.datetime.now()
        # data_df = data_df[:-1]
        # df_last = data_df.tail(1)
        if data_df.tail(1).iloc[:,0].tolist()[0] == '[End of File]':
            data_df = data_df[:-1]
        print(data_df.shape)
        cur.executemany(insStr,data_df.where((pd.notnull(data_df)), None).values.tolist())
        con.commit()
    except Exception as e:
        print(type(e))
        go = False
    
print(len(want))

# df=pd.concat(want, ignore_index=True)

print(datetime.datetime.now()-start)

# print(df.shape)
# df.head(1)
