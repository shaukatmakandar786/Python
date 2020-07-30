import requests
import calendar
import datetime
import datetime as dt
from datetime import date,timedelta
from sqlalchemy_examples.create_database_and_table_for_github_details import GithubJobInfo,Engine
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

Session=sessionmaker(bind=Engine)
session=Session()
#JobId,JobType,CreatedAt,UpdatedAt,JobObject,JobStatus,JobLog,PreviousJobId
class GitRepoApisDetails:

    def job_is_get_repo(self,query_url,jobid,createdat):


        headers = {'content-type': 'application/json'}
        self.response = requests.get(query_url, headers=headers)
        self.matched_repositories = self.response.json()
        if self.matched_repositories['total_count']==0:

            result=GithubJobInfo(jobid,'githubapis',createdat,'UpdatedAt','JobObject','completed',self.matched_repositories,'0')
            session.add(result)
            session.commit()
            print("inserted if")
        else:
            result = GithubJobInfo(jobid, 'githubapis', createdat,'UpdatedAt', 'JobObject', 'completed', 'got_ouput', '0')
            session.add(result)
            session.commit()
            print("inserted  else")

            all_repositories_details = []
            for repo in self.matched_repositories["items"]:
                repo_details = dict()
                repo_details["id"] = repo.get("id")
                repo_details["name"] = repo.get("name")
                repo_details["full_name"] = repo.get("full_name")
                repo_details["private"] = repo.get("private")
                repo_details["owner"] = dict()
                repo_details["owner"]["login"] = repo.get("owner").get("login")
                repo_details["owner"]["id"] = repo.get("owner").get("id")
                repo_details["owner"]["html_url"] = repo.get("owner").get("html_url")
                repo_details["html_url"] = repo.get("html_url")
                repo_details["description"] = repo.get("description")
                repo_details["url"] = repo.get("url")
                repo_details["contents_url"] = repo.get("contents_url")
                repo_details["created_at"] = repo.get("created_at")
                repo_details["updated_at"] = repo.get("updated_at")

                if repo.get("license"):
                    repo_details["license"] = dict()
                    repo_details["license"]["key"] = repo.get("key")
                    repo_details["license"]["name"] = repo.get("name")
                    repo_details["license"]["spdx_id"] = repo.get("spdx_id")
                    repo_details["license"]["url"] = repo.get("url")

                repo_details["forks"] = repo.get("forks")
                repo_details["watchers"] = repo.get("watchers")
                all_repositories_details.append(repo_details)

        #print("hi")
        print(all_repositories_details)
        return all_repositories_details

    def add_job_by_time(self,target_url,flag,nextTime,jobid):


        if flag == 1:
            dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")
            sched.add_job(obj.job_is_get_repo, 'date', run_date=dat, misfire_grace_time=10, args=[target_url,jobid,dat])
        else:
            dat = dt.datetime.strftime(nextTime, "%Y-%m-%d %H:%M:%S")
            sched.add_job(obj.job_is_get_repo, 'date', run_date=dat, misfire_grace_time=10, args=[target_url,jobid,dat])

    def get_repo_details_by_month(self,repo_name,year,month):


        total_days=calendar.monthrange(year,month)[1]
        flag=1
        nextTime=''
        count=0
        for days in range(1,total_days+1):

            count=count+1
            jobid="job_{number}".format(number=count)
            day_obj = datetime.date(year, month, days)
            target_url = "https://api.github.com/search/repositories?q={repo_name}+created:{date}".format(repo_name=repo_name,date=day_obj)
            if flag==1:
                nextTime = dt.datetime.now() + dt.timedelta(seconds=5)
                self.add_job_by_time(target_url,flag,nextTime,jobid)
                flag=0
            else:
                nextTime = nextTime + dt.timedelta(seconds=5)
                self.add_job_by_time(target_url, flag, nextTime,jobid)


obj=GitRepoApisDetails()
obj.get_repo_details_by_month("dockerfile",2020,4)
sched.start()