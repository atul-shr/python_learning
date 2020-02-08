import pandas as pd
import datetime
import numpy as np
import cx_Oracle as cx
import sys
import openpyxl
import argparse


con = cx.connect('hr/HR@LAPTOP-21RC5VEQ:1521/XE')
cur = con.cursor()

# cur.execute("Truncate table test_chunks")

# args = sys.argv[1:]

def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='Script to get the object and its dependencies list')
    parser.add_argument('--type', dest='type',
                        help='sum the integers (default: find the max)')
    parser.add_argument('--name', dest='name',
                        help='sum the integers (default: find the max)')
    return parser


def parse_arg():
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args()
    if not args.name:
        print("Argument not available")
    print("Input Params are " + '-' * 40)
    print(args)
    print("Input Params are " + '-' * 40)
    return args


args = parse_arg()

writer =  pd.ExcelWriter('D:\\learning\\code\\utils\\VSS\\outbound\\ObjectsList_' + args.type + '_' + args.name +'.xlsx')

if args.type == 'COLUMN':
    df_source = pd.read_sql("select * from all_source where upper(text) like '%{}%'".format(args.name),con=con)

    df_cols = pd.read_sql("select * from all_tab_cols where upper(column_name) like '%{}%'".format(args.name),con=con)
    
    df_source.to_excel(writer, sheet_name='Source_Existance',index=False)
    
    df_cols.to_excel(writer, sheet_name='Cols_in_Tables',index=False)


elif args.type == 'TABLE':
    df_depend = pd.read_sql("select * from all_dependencies where upper(REFERENCED_NAME) like '%{}%'".format(args.name),con=con)

    df_depend.to_excel(writer, sheet_name='Dependencies',index=False)

writer.close()
