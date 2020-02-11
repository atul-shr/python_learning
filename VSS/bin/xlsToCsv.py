import pandas as pd
import argparse


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
    print("Input Params are " + '-' * 30)
    print(args)
    print("Input Params are " + '-' * 30)
    return args


args = parse_arg()


read_file = pd.read_excel ('D:\\learning\\code\\utils\\VSS\\outbound\\Excel_ObjectsList_' + args.type.lower() + '_' + args.name.lower() +'.xlsx')
read_file.to_csv ('D:\\learning\\code\\utils\\VSS\\outbound\\Csv_ObjectsList_' + args.type.lower() + '_' + args.name.lower() +'.csv')

