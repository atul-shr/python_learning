import ora_con as db
import pandas as pd
import numpy as np
import sys
import configparser
import logging
import argparse

def read_config(arg):
    config = configparser.ConfigParser()
    config.read(arg)
    return config

def readFile(file_name):
    return open(file_name,'r')

def config_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--config", help="provide the config to get db details")
    parser.add_argument("-t","--type", help="provide the type of comparison",choices=['SQL_EXE','FILE_COMP'])
    args = parser.parse_args()
    if not args.config or not args.type:
        logger.error("Error !! - Arguments Required , check help!!")
        sys.exit(1)
    return args


def executeSql(hr_con,fn):
    logger.info('In Execute SQL Function')
    sqlfile = readFile(fn)
    qstr = sqlfile.read()
    df = pd.read_sql(qstr,hr_con)
    # logger.info(df)
    sqlfile.close()
    return df


def compFile():
    logger.info('In Compare File Function')

def createDictConfig(cf):
    dict_cfg = {}
    cnfg = read_config(cf)
    for items in cnfg:
        if items != 'DEFAULT':
            dict_cfg[items] = {}
        for mt in cnfg[items]:
            dict_cfg[items][mt] = cnfg[items][mt]
    return dict_cfg

def createCon(dict):
    hr_usr = dict['LEARNING_CONFIG']['hr_usr']
    hr_pwd = dict['LEARNING_CONFIG']['hr_pwd']
    hr_sid = dict['LEARNING_CONFIG']['hr_sid']
    hr = db.dbCon(hr_usr,hr_pwd,hr_sid)
    return  hr.createConnection()


# -- Main function to start processing script --
def main():

    arg = config_arguments()
    config_dict = createDictConfig(arg.config)
    hr_con = createCon(config_dict)
    # logger.info(config_dict)
    

    if arg.type == 'SQL_EXE':
        sql_df = executeSql(hr_con,'D:\\learning\\code\\utils\\VSS\\sql\\user_tables.sql')
        sql_df.to_csv('D:\\learning\\code\\utils\\VSS\\sql\\sql_output.csv',index=False)

    elif arg.type == 'FILE_COMP':
        compFile()
    else:
        logger.info('Wrong Option !!')


# -- checking calling for within script or imported script --
logging.basicConfig(level='DEBUG',format='[%(name)s - %(levelname)s  : %(asctime)s ] - %(message)s')
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    main()

