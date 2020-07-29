from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

def my_job():
    print("hello")

# The job will be executed on November 6th, 2009
sched.add_job(my_job, 'date', run_date='2020-07-21 22:59:00')

sched.start()

"""# The 'date' trigger and datetime.now() as run_date are implicit
sched.add_job(my_job)"""
