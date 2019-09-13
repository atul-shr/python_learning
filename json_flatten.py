import json
import pyodbc
from datetime import datetime

#  datetime object containing current date and time
now = datetime.now()


# connection creation to SQL Server
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-21RC5VEQ;"
    "Database=json;"
    "Trusted_Connection=yes;"
)


# create raw data
def create(conn,ls):
    print("Create")
    cnt = 0
    cur = conn.cursor()
    cur.execute("delete from dbo.json_flatten_raw;")
    for rec in ls:
        cnt += 1
        cur.execute("insert into dbo.json_flatten_raw(item_no,item_name,item_value,insert_date) values (?,?,?,?);",
                    (cnt,rec[0],rec[1],now)
                    )
    conn.commit()


# creation of leaf records
def break_down_leaf(conn):
    print("Create Child Records")
    cnt = 0
    split_leaf_list = []
    split_leaf =[]
    cur_read = conn.cursor()
    #  cur_ins = conn1.cursor()
    cur_read.execute("select item_no , item_name , item_value  from dbo.json_flatten_raw;")
    for row in cur_read:
        split_leaf_list.append(row)

    for inner_row in split_leaf_list:
        #  print(row[0],row[1],row[2])
        split_leaf = inner_row[1].split(".")
        #  print(split_leaf)
        for child_rec in split_leaf:
            cnt += 1
            cur_read.execute("insert into dbo.json_flatten(item_no,item_name,parent_item_no,insert_date) values (?,?,?,?);",
                        (cnt, child_rec, inner_row[0],now)
                        )
        cnt = 0
    conn.commit()


# read json source file
with open("source.json", "r") as rj:
    response = rj.read()
res = json.loads(response)


# read json file into records

def flattenDict(d, result=None, index=None, Key=None):
    if result is None:
        result = {}
    if isinstance(d, (list, tuple)):
        for indexB, element in enumerate(d):
            if Key is not None:
                newkey = Key
            flattenDict(element, result, index=indexB, Key=newkey)
    elif isinstance(d, dict):
        for key in d:
            value = d[key]
            if Key is not None and index is not None:
                newkey = ".".join([Key, (str(key).replace(" ", "") + str(index))])
            elif Key is not None:
                newkey = ".".join([Key, (str(key).replace(" ", ""))])
            else:
                newkey = str(key).replace(" ", "")
            flattenDict(value, result, index=None, Key=newkey)
    else:
        result[Key] = d
    return result


raw_list =[]


# create list of records from json
for i in flattenDict(res).items():
    raw_list.append(i)


# call function of raw rec creation


create(conn,raw_list)

# call function of child rec creation

break_down_leaf(conn)

conn.close()
