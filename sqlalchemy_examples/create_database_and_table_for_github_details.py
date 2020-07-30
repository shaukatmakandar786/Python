from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,MetaData
from sqlalchemy.ext.declarative import declarative_base

Engine=create_engine('sqlite:///githubrepo.sqlite')
BASE=declarative_base()

class GithubJobInfo(BASE):
    __tablename__='githubjobinfo'
    JobId=Column(String(200),primary_key=True)
    JobType=Column(String(200))
    CreatedAt=Column(String(200))
    UpdatedAt = Column(String(200))
    JobObject = Column(String(200))
    JobStatus = Column(String(200))
    JobLog = Column(String(200))
    PreviousJobId = Column(String(200))

    def __init__(self,JobId,JobType,CreatedAt,UpdatedAt,JobObject,JobStatus,JobLog,PreviousJobId):

        self.JobId=JobId
        self.JobType=JobType
        self.CreatedAt=CreatedAt
        self.UpdatedAt=UpdatedAt
        self.JobObject=JobObject
        self.JobStatus=JobStatus
        self.JobLog=JobLog
        self.PreviousJobId=PreviousJobId


BASE.metadata.create_all(Engine)