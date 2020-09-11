from flask import Flask
from numpy import genfromtxt
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:root@localhost/Jobby', convert_unicode=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

app = Flask(__name__)
  
'''
def load_data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()
'''
class Jobs(Base):
    __tablename__ = 'jobs'

    job_id = Column(Integer, primary_key=True)
    job_title = Column(String(150))
    salary_estm = Column(String(50))
    job_desc = Column(String)    
    

class Companies(Base):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True)
    company_name = Column(String(150))
    ubi = Column(String(50))
    rating = Column(String(20))
    sz = Column(String(20))
    founded = Column(String(20))
    creator = Column(String, ForeignKey('users.id_user'))

class Users(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key = True)
    name = Column(String(30))
    username = Column(String(20))
    password = Column(String(20))
    creator = Column(Integer)

def jobs(pregunton):
    preg = db_session.query(Companies.ubi.ilike(f'%{pregunton}%')).all()
    for data in preg:
        print(data)

if __name__ == "__main__":
    jobs("Health")
    file_name = 'static/DataAnalyst.csv'
    '''
    data = load_data(file_name)
    
    for i in data:
        record = Companies(**{
            'company_id' : i[0],
            'company_name' : i[5]
        })
        db_session.add(record)
    '''

#.filter(JobTitle.job_desc.like(prueba +'%'))