#!/usr/bin/python
import cx_Oracle
import logging
import argparse


def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='File name for the HC')
    parser.add_argument('--name', dest="name", help="Give the name of the file to validate")
    return parser


def parse_arg():
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args()
    if not args.name:
        logger.error("Argument not available")
    logger.info("Input Params are " + '-' * 40)
    logger.info(args)
    logger.info("Input Params are " + '-' * 40)
    return args


def get_rows(own, obj_nm):
    # print("in get rows")
    con = cx_Oracle.connect(own + '/HR@XE')
    cur = con.cursor()
    name = []
    querystring = "select count(1) from all_objects where object_name ='" + obj_nm + "' and owner = '" + own + "'"
    # print(querystring)
    cur.execute(querystring)
    for row in cur:
        # print(row, end="\n")
        name.append(row[0])
    return name


try:
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
except ValueError:
    pass


def main():
    # row_name = []
    # print("In main")

    logger.info("In Main")
    args = parse_arg()
    # print(args.name)
    with open(args.name, "r") as ins:
        for line in ins:
            try:
                # print(line)
                arr_line = line.split("/")
                # print(arr_line[1])
                ob_nm = arr_line[3].split(":")
                # print(ob_nm)
                tab_name = ob_nm[0].split(".")
                # print(arr_line[1] + "--" + tab_name[0])
                row_name = get_rows(arr_line[1], tab_name[0])
                # print(row_name[0] + " and " + row_name[1])
                if row_name[0] >= 1:
                    logger.info(arr_line[1] + " and " + tab_name[0] + ":[OK]")
                else:
                    logger.error(arr_line[1] + " and " + tab_name[0] + ":[FAIL]")
            except:
                logger.error("Fetch for the given Object :[FAIL]")


if __name__ == '__main__':
    main()
