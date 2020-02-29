import cx_Oracle
import pandas as pd
import numpy as np
import sys
import configparser
import logging
import argparse
import os

def read_config(arg):
    config = configparser.ConfigParser()
    config.read(arg)
    return config

def readFile(file_name):
    return open(file_name,'r')

def config_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--process", help="Process Name")
    args = parser.parse_args()
    # if not args.process:
    #     logger.error("Error !! - Arguments Required , check help!!")
    #     sys.exit(1)
    return args

def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    if defaultType == cx_Oracle.CLOB:
        return cursor.var(cx_Oracle.LONG_STRING, arraysize=cursor.arraysize)
    if defaultType == cx_Oracle.BLOB:
        return cursor.var(cx_Oracle.LONG_BINARY, arraysize=cursor.arraysize)

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

def createSqlCon(dict):
    usr = dict['SQL']['usr']
    pwd = dict['SQL']['pwd']
    sid = dict['SQL']['sid']
    return  cx_Oracle.connect(usr,pwd,sid)
    

def getProcessDetails(con, sql, proc_name):
    # logger.info(sql)
    # logger.info(proc_name)
    con.outputtypehandler = OutputTypeHandler
    cur = con.cursor()
    if proc_name is None or proc_name=='ALL':
        cur.execute(sql)
    else:
        cur.execute(sql,[proc_name])
    res = cur.fetchall()
    return res    

def process_DB_TO_DB(param_list,conn):
    logger.info('In process_DB_TO_DB')
    src_output_file = "D:\\learning\\code\\utils\\VSS\\outbound\\" + param_list[1] + "_recon_src.txt"
    tgt_output_file = "D:\\learning\\code\\utils\\VSS\\outbound\\" + param_list[1] + "_recon_tgt.txt"
    diff_output_file = "D:\\learning\\code\\utils\\VSS\\outbound\\" + param_list[1] + "_recon_diff.txt"
    if os.path.exists(src_output_file):
        os.remove(src_output_file)
    if os.path.exists(tgt_output_file):
        os.remove(tgt_output_file)
    rf = open(diff_output_file,mode='w')
    # logger.info(param_list)
    src_sid = param_list[3]
    src_sql = param_list[4]
    src_key = param_list[6]
    tgt_sid = param_list[7]
    tgt_sql = param_list[8]
    tgt_key = param_list[10]
    logger.info('Source Database - ' + src_sid)
    logger.info('Source SQL - ' + src_sql)
    logger.info('Source Key on which comparison to be done - ' + src_key)
    logger.info('Target Database - ' + tgt_sid)
    logger.info('Target SQL - ' + tgt_sql)
    logger.info('Target Key on which comparison to be done - ' + tgt_key)
    src_con = cx_Oracle.connect(src_sid)
    src_cur = src_con.cursor()
    tgt_con = cx_Oracle.connect(tgt_sid)
    tgt_cur = tgt_con.cursor()
    # src_cur.execute(src_sql)
    # src_res = src_cur.fetchall()
    # tgt_cur.execute(tgt_sql)
    # tgt_res = tgt_cur.fetchall()
    src_data_df = pd.read_sql(src_sql,src_con)
    less_src_df = src_data_df[['OBJECT_NAME','OBJECT_ID','OBJECT_TYPE']]
    new_less_src_df = less_src_df.add_suffix('_LEFT')

    tgt_data_df = pd.read_sql(tgt_sql,tgt_con)
    less_tgt_df = tgt_data_df[['OBJECT_NAME','OBJECT_ID','OBJECT_TYPE']]
    new_less_tgt_df = less_tgt_df.add_suffix('_RIGHT')

    merge_df = new_less_src_df.merge(new_less_tgt_df, left_on=src_key+'_LEFT', right_on=tgt_key+'_RIGHT', how='outer')

    logger.info(merge_df)

    extra_tgt_df = merge_df[merge_df[src_key+'_LEFT'].isnull()]
    extra_src_df = merge_df[merge_df[tgt_key+'_RIGHT'].isnull()]
    # logger.info(extra_src_df)
    # logger.info(extra_tgt_df)
    
    # df = df1[df1.set_index(['A','B']).index.isin(df2.set_index(['A','B']).index)]

    additional_src_df = src_data_df[src_data_df.set_index([src_key]).index.isin(extra_src_df.set_index([src_key+'_LEFT']).index)]
    additional_tgt_df = tgt_data_df[tgt_data_df.set_index([tgt_key]).index.isin(extra_tgt_df.set_index([tgt_key+'_RIGHT']).index)]
    # logger.info(additional_src_df)
    # logger.info(additional_tgt_df)
    # rf.writelines("Additional Lines in Source")
    additional_src_df.to_csv(src_output_file,header=True,index=False,mode='w')
    # rf.writelines("\nAdditional Lines in Target")
    additional_tgt_df.to_csv(tgt_output_file,header=True,index=False,mode='w')
    logger.info((merge_df.columns))
    for rec in merge_df.index:
        for col_name in less_src_df.columns:
            # logger.info(str(merge_df[col_name+'_LEFT'][rec]) + str(merge_df[col_name+'_RIGHT'][rec]))
            if merge_df[col_name+'_LEFT'][rec] != merge_df[col_name+'_RIGHT'][rec]:
                rf.writelines("Key - " + src_key + " : " + col_name + " - " +  str(merge_df[col_name+'_LEFT'][rec]) + ":" + str(merge_df[col_name+'_RIGHT'][rec]) + "\n")


def process_DB_TO_FILE(param_list,conn):
    logger.info('process_DB_TO_FILE')


def process_FILE_TO_DB(param_list,conn):
    logger.info('In process_FILE_TO_DB')


def process_FILE_TO_FILE(param_list,conn):
    logger.info('In process_FILE_TO_FILE')

def getComparetype(type,all_proc,conn):
    if type == 'DB_TO_DB':
        process_DB_TO_DB(all_proc,conn)
    elif type == 'DB_TO_FILE':
        process_DB_TO_FILE(all_proc,conn)
    elif type == 'FILE_TO_DB':
        process_FILE_TO_DB(all_proc,conn)
    elif type == 'FILE_TO_FILE':
        process_FILE_TO_FILE(all_proc,conn)
    else:
        logger.info('Wrong Compare type setup in DB')


# -- Main function to start processing script --
def main():
    logger.info('Starting with Program')
    arg = config_arguments()
    logger.info('Creating Dictionary of Arguments')
    logger.info('-'*30)
    if arg.process is None:
        agg = 'Arguments are : None '
    else:
        agg = 'Arguments are : ' +  arg.process
    logger.info(agg)
    logger.info('-'*30)
    config_dict = createDictConfig(r"D:\learning\code\utils\VSS\config\file_compare_config.ini")
    # logger.info(config_dict)
    conn = createSqlCon(config_dict)
    
    if arg.process is None or  arg.process == 'ALL':
        sql = config_dict['DATA_CONFIG']['sql_all_config']
        data_config = getProcessDetails(conn, sql, arg.process)
        for all_proc in data_config:
            # logger.info(all_proc)
            logger.info('Processing for Process Name - ' + all_proc[1] + ' as ' +   all_proc[2] + ' Compare ')
            getComparetype(all_proc[2],all_proc,conn)
    else :
        sql = config_dict['DATA_CONFIG']['sql_config']
        data_config = getProcessDetails(conn, sql, arg.process)
        logger.info('Processing for Process Name - ' + arg.process + ' as ' +   data_config[0][2] + ' Compare ')
        getComparetype(data_config[0][2],data_config[0],conn)



# -- checking calling for within script or imported script --
logging.basicConfig(level='DEBUG',format='[%(name)s - %(levelname)s  : %(asctime)s ] - %(message)s')
logger = logging.getLogger(__name__)

 
if __name__ == '__main__':
    main()

