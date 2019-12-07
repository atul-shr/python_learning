import ora_con as db
import pandas as pd
import configparser
import sys
# import argparse

arg = sys.argv[1:]

print(arg)

def read_config(arg):
    config = configparser.ConfigParser()
    config.read(arg[0])
    return config

def setCon(read_config):
    config = read_config()
    hr = db.dbCon(config['LEARNING_CONFIG']['hr_usr'],config['LEARNING_CONFIG']['hr_pwd'],config['LEARNING_CONFIG']['hr_sid'])
    pharma = db.dbCon(config['LEARNING_CONFIG']['pharma_usr'],config['LEARNING_CONFIG']['pharma_pwd'],config['LEARNING_CONFIG']['pharma_sid'])

    hr_con = hr.createConnection()
    pharma_con = pharma.createConnection()

    # hr_curr = hr.createCursor(hr.createConnection())
    # pharma_curr = pharma.createCursor(pharma.createConnection())


    qstr = 'select * from user_tables'

    hr_df = pd.read_sql(qstr,hr_con)

    pharma_df = pd.read_sql(qstr,pharma_con)

# print(hr_df.TABLE_NAME) 

# print(pharma_df.TABLE_NAME)



