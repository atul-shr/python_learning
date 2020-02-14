import pandas as pd
import argparse
import xlrd
import os

def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='Script to convert Excels to csv')
    parser.add_argument('--inpfile', dest='inpfile',
                        help='Input Excel file name')
    parser.add_argument('--outfile', dest='outfile',
                        help='Output CSV file name')
    parser.add_argument('--worksheet', dest='worksheet',
                        help='worksheet can be ALL, null or 1,2,3')
    return parser


def parse_arg():
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args()
    if not args.inpfile or not args.outfile:
        print("Argument not available")
    print("Input Params are " + '-' * 60)
    print(args)
    print("Input Params are " + '-' * 60)
    return args


args = parse_arg()


read_file = pd.read_excel (args.inpfile,sheet_name=[0,'Source_Existance'])
print(read_file)
# print(read_file['Source_Existance'])
# read_file = read_file.replace('\n','',regex=True)
# read_file.to_csv (args.outfile)
