import pandas as pd
import datetime
import numpy as np
import cx_Oracle as cx
import sys
import openpyxl
import os
import argparse
import configparser as cfg


# con = cx.connect('hr/manager@LAPTOP-21RC5VEQ:1521/XE')
# cur = con.cursor()


# cur.execute("Truncate table test_chunks")

# args = sys.argv[1:]

def get_db_conn(cnfg):
    script_path = os.path.abspath(__file__)
    if os.name == 'nt':
        config_path = '\\'.join(script_path.split('\\')[:-2]) + '\\config\\etl_config.ini'
    elif os.name == 'posix':
        config_path = '/'.join(script_path.split('/')[:-2]) + '/configs/etl_config.ini'
    print(config_path)
    cnfg.read(config_path)
    con = cx.connect(
        cnfg.get('DB_CONNECTION', 'SCHEMA_NAME') + "/" + cnfg.get('DB_CONNECTION', 'PASSWORD') + "@" + cnfg.get(
            'DB_CONNECTION', 'DB_HOST') + ":" + cnfg.get('DB_CONNECTION', 'DB_PORT') + "/" + cnfg.get('DB_CONNECTION',
                                                                                                      'SERVICE_NAME'))
    return con


def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='Script to get the object and its dependencies list')
    parser.add_argument('--stack', dest='stack',
                        help='Type of Tech Stack')
    parser.add_argument('--search_type', dest='search_type',
                        help='Type of artifact to be searched')
    parser.add_argument('--name', dest='name',
                        help='name of the artifact to be searched')
    parser.add_argument('--outfile', dest='outfile',
                        help='Outfile to be created')
    return parser


def parse_arg(arguments):
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args(arguments)
    if not args.name or not args.stack or not args.search_type:
        parser.error("Check all the arguments are passed, use -h for help")
    print("Input Params are " + '-' * 40)
    print(args)
    print("Input Params are " + '-' * 40)
    return args


def main():
    argv = sys.argv
    args = parse_arg(argv[1:])
    config = cfg.RawConfigParser()
    conn = get_db_conn(config)

    writer = pd.ExcelWriter(
        'D:\\learning\\code\\utils\\VSS\\outbound\\Excel_ObjectsList_' + args.search_type.lower() + '_' + args.name.lower() + '.xlsx')

    if args.search_type.upper() != 'COLUMN':
        df_depend = pd.read_sql(
            "select * from all_dependencies where upper(REFERENCED_NAME) like '%{}%'".format(args.name.upper()),
            con=conn)
        df_depend.to_excel(writer, sheet_name='Dependencies', index=False)

    if args.search_type.upper() == 'COLUMN':
        df_cols = pd.read_sql(
            "select * from all_tab_cols where upper(column_name) like '%{}%'".format(args.name.upper()), con=conn)
        df_cols.to_excel(writer, sheet_name='Cols_in_Tables', index=False)

    df_source = pd.read_sql("select * from all_source where upper(text) like '%{}%'".format(args.name.upper()),
                            con=conn)
    df_source.to_excel(writer, sheet_name='Source_Existance', index=False)

    writer.close()


if __name__ == '__main__':
    main()

