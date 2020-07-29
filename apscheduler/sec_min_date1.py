import schedule
import time

def job_by_sec():
    print("This job work on the every 3 second")


def job_by_min():
    print("This job work on every 1 min ")


def job_by_date():
    print("This job work on every day 11:00")


# call the task/job
schedule.every(1).seconds.do(job_by_sec)
schedule.every(1).minutes.do(job_by_min)
schedule.every().day.at("03:57").do(job_by_date)

while True:
        schedule.run_pending()
        time.sleep(5)