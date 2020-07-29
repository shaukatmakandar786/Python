import schedule
import time


# Functions setup

def job_by_hour():
    print("this job is running in every 1 hour")


def job_by_min():
    print("this job is running in every 1 min")


def job_by_sec():
    print("this job is running in every 3 sec")


def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")


def good_luck():
    print("Good Luck for Test")


def work():
    print("Study and work hard")


def bedtime():
    print("It is bed time go rest")


# Task scheduling
#After every 3 sec job_by_sec() is called.
schedule.every(3).seconds.do(job_by_sec)

# After every 1 mins job_by_min() is called.
schedule.every(1).minutes.do(job_by_min)

# After every hour job_by_hour() is called.
schedule.every().hour.do(job_by_hour)

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("00:00").do(bedtime)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)