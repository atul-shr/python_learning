import cx_Oracle
import logging
import argparse


def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='Sum the salary dept wise.')
    parser.add_argument('--pattern', dest="pattern", help="Give the name to search")
    return parser


def parse_arg():
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args()
    if not args.pattern:
        logger.error("Argument not available")
    logger.info("Input Params are " + '-' * 80)
    logger.info(args)
    logger.info("Input Params are " + '-' * 80)
    return args


def get_rows():
    # print("in get rows")
    con = cx_Oracle.connect('HR/HR@XE')
    cur = con.cursor()
    name = []
    querystring = "select first_name , last_name from employees"
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
    row_name = get_rows()
    # print(row_name)
    if args.pattern in row_name:
        print("Found :" + args.pattern)
        logger.info("Found")
    else:
        print("Didn't Found :" + args.pattern)
        logger.error("Not Found")


if __name__ == '__main__':
    main()
