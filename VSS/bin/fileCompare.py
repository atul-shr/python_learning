import pandas as pd
import os
import cx_Oracle
import datetime

con_str = 'pharma/pharma@LAPTOP-21RC5VEQ:1521/XE'

con = cx_Oracle.connect(con_str)


df = pd.read_sql('select * from all_objects',con)

print(len(df))

