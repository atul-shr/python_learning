import cx_Oracle as cx
import pandas as pd
import datetime
import numpy as np

con = cx.connect('hr/HR@LAPTOP-21RC5VEQ:1521/XE')

df_emp = pd.read_sql('select * from EMPLOYEES',con)

df_job = pd.read_sql('select * from JOB_HISTORY',con)

df_emp['JOB_ADD_ID'] = ''

# print(df_emp.head())

# print(df_job.head())

for i, o_row in df_emp.iterrows():
    for j, i_row in df_job.iterrows():
        if df_emp.at[i,'DEPARTMENT_ID'] ==  df_job.at[j,'DEPARTMENT_ID'] and df_emp.at[i,'EMPLOYEE_ID'] ==  df_job.at[j,'EMPLOYEE_ID'] :
            df_emp.at[i,'JOB_ADD_ID'] = df_job.at[j,'JOB_ID']

# df[(df.A == 1) & (df.D == 6)]

df_fil = df_emp[(df_emp.JOB_ADD_ID != '')]

print(df_fil)




