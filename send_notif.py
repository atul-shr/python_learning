import json
import urllib3
import logging
import argparse

def create_parser():
    # print("In create arg")
    parser = argparse.ArgumentParser(description='Get Cowin Appointment Details')
    parser.add_argument('--state_name', dest="state_name", help="State Name")
    parser.add_argument('--district_name', dest="district_name", help="District Name")
    parser.add_argument('--date', dest="date", help="Date for which appointment to be checked")
    return parser


def parse_arg():
    # print("In parse arg")
    parser = create_parser()
    args = parser.parse_args()
    if not args.state_name or not args.district_name:
        logger.error("Argument not available")
    logger.info("Input Params are " + '-' * 40)
    logger.info(args)
    logger.info("Input Params are " + '-' * 40)
    return args


try:
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
except ValueError:
    pass



def execute_main():
    logger.info("In Main")
    args = parse_arg()

    with open('config.json') as f:
        configs = json.load(f)
    pool_conn = urllib3.PoolManager()
    states_req = pool_conn.request(
        'GET', configs["main_api_url"] + configs["states_url"])
    states_res = json.loads(states_req.data.decode('utf-8'))
    mp_state_id = 0
    for states in states_res["states"]:
        # print(states)
        if states['state_name'] == args.state_name:
            mp_state_id = states['state_id']
    print(mp_state_id)

    districts_req = pool_conn.request(
        'GET', configs["main_api_url"] + configs["districts_url"] + str(mp_state_id))
    districts_res = json.loads(districts_req.data.decode('utf-8'))
    # print(districts_res)
    bhopal_id = 0
    for districts in districts_res["districts"]:
        # print(states)
        if districts['district_name'] == args.district_name:
            bhopal_id = districts['district_id']
    print(bhopal_id)

    appointment_req = pool_conn.request(
        'GET', configs["main_api_url"] + configs["find_by_districts"], fields={"district_id": bhopal_id, "date": "10-05-2021"})
    appointment_res = json.loads(appointment_req.data.decode('utf-8'))
    # print(appointment_res)

    var_center_name = ''
    var_age_limit_45 = 45
    var_age_limit_18 = 18
    counter = 0

    for center in appointment_res["sessions"]:
        # print(center['sessions'])
        if center['min_age_limit'] == var_age_limit_18:
            counter += 1
            print('center name == ',
                    center['name'], ' available_capacity ==', center['available_capacity'])

    if counter == 0:
        print("No Appointment found for today")

if __name__ == "__main__":
    execute_main()
