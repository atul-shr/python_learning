import pyodbc
import pandas as pd

def fields(cursor):
    column = []
    for d in cursor.description:
        column.append(d[0])
    return column

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\learning\code\utils\VSS\inbound\Campaign_Template.mdb;')
cursor = conn.cursor()
cursor.execute('select * from campaign_table')

header = fields(cursor)

# print(header)

data = []

for rec in cursor.fetchall():
    data.append(list(rec))

# print (data)

df_data = pd.DataFrame(data,columns=header)

# print (df_data)

writer = pd.ExcelWriter('output_excel.xlsx')
df_data.to_excel(writer, sheet_name='Sheet1',index=False)
writer.save()






