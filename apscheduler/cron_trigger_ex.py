from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print ("Hello World")

sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='7-8', day='1-31', minute ='0-1')

sched.start()