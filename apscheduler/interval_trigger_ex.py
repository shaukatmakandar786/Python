from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two seconds
#sched.add_job(job_function, 'interval', seconds=2)
# The same as before, but starts on 2010-10-10 at 9:30 and stops on 2014-06-15 at 11:00
sched.add_job(job_function, 'interval', seconds=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')


sched.start()