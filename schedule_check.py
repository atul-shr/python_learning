import schedule
import time
import send_notif
import os


def job():
    os.system('python send_notif.py --state_name "Madhya Pradesh" --district_name Bhopal --date 11-05-2021 --age_grp 18 --type W')


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
