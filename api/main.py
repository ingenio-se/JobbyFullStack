from flask import Flask, request, make_response,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json
from flask import jsonify
import pandas as pd
import numpy as np
import math
from pandasql import sqldf
from tabulate import tabulate


global df

df=[]
app = Flask(__name__, static_folder='../build', static_url_path='/')

ENV = 'prod'

if ENV == 'dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:80085700@localhost:5432/jobby"
    
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://kypjuimrppxber:789b0622e2c424a26fbb46ec4da0347904b0c8c9caf204543bc0bcc835b553d3@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dau09psmsu0vp7"
    
db = SQLAlchemy(app)



#------------------------------ROUTES----------------------------------


@app.route('/')
def index():
    return app.send_static_file('index.html')


#--------------------USERS-------------------------------------
class UsersModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password= db.Column(db.String())

    def __init__(self, user_id,first_name,last_name,email,password):
        self.user_id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

def maxId(table):
    if table == "users":
        queryId ="select max(user_id) as max from " + table
    else:
        queryId ="select max(id) as max from " + table
    sql = text(queryId)
    result = db.engine.execute(sql)
  
    id= [row for row in result]
    if isinstance(id[0][0], int):
        return int(id[0][0])+1
    else:
        return 1

@app.route('/registerUser', methods=['POST'])
def register():
    
        
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    email= request.form['email']
    password= request.form['password']

    user_id=maxId('users')

    query ="insert into users values ("+ str(user_id) + ",'" + str(email) + "','" +  str(first_name) + "','" + str(last_name) + "','" + str(password) +"')"
    sql = text(query)
    result = db.engine.execute(sql)
        
    return jsonify("User created")

@app.route('/createJob', methods=['POST'])
def createJob():
    
    title= request.form['title']
    location= request.form['location']
    company= request.form['company']
    salary= request.form['salary']
    ratio= request.form['ratio']
    description= request.form['description']

    salary= salary.replace(" ","").split("-")
    l1 = salary[0]
    l1= l1.replace('K','000')
    l1 = int(l1.replace('$',''))

    l2 = salary[1]
    l2= l2.replace('K','000')
    l2 = int(l2.replace('$',''))

    id=maxId('jobs')

    query ="insert into jobs (id,job_title,salary_estimate_l1,salary_estimate_l2,job_description,rating,company_name,location) values ("+str(id)+",'"+title+"',"+str(l1)+","+str(l2)+",'"+description+"',"+str(ratio)+",'" + company + "','"+ location+"')"
    print(query)
    sql = text(query)
    result = db.engine.execute(sql)
        
    return jsonify("Job created")

@app.route('/loginUser', methods=['POST'])
def login():
    email= request.form['email']
    password= request.form['password']


    query ="select * from users where email ='"+ str(email) +"'"
    sql = text(query)
    result = db.engine.execute(sql)

    #results=[]
    for row in result:
        #l =[row[0],row[1],row[2],row[3],currencyName(row[4])]
        #results.append(l)
        print(row[4])
        if row[4] == password:
            return jsonify("Bienvenido "+row[2])
        else:
            return jsonify("Password incorrect")
    return jsonify("User not found")

@app.route('/data')
def data():
    
    df = pd.read_csv('static/DataAnalyst.csv')
    head  = df.head()

    for r in head.iterrows():
        print(r)
    return render_template('data.html',df = df)



@app.route('/hello')
def hello():
    return 'hola'

@app.route('/locations')
def locations():
    load()
    limpiar()
    locations=sqldf("select distinct(Location) from df ")
    locations = locations.to_json()
    print(locations)
    
    return render_template('datos.html',datos =locations)

@app.route('/salary/<keyword>')
def salary(keyword):
    #load()
    #limpiar()
    salary = keyword.split("-")
    l1 = str(int(salary[0])*1000)
    l2 = str(int(salary[1])*1000)
    print(l1)
    print(l2)

    query ="select * from jobs where  salary_estimate_l1 < "+l1+" and salary_estimate_l2 > "+l2
    sql = text(query)
    result = db.engine.execute(sql)
    jobsf = getArrayBD(result)
    print(jobsf)
    return jsonify(jobsf)

    '''
    jobs =sqldf("select * from df where  salary_estimate_l1 < "+l1+" and salary_estimate_l2 > "+l2)
    #jobs =sqldf("select * from df where (salary_estimate_l1 > "+l1+" and salary_estimate_l2 > "+l2+") or (salary_estimate_l1 < "+l1+" and salary_estimate_l2 > "+l2+") or (salary_estimate_l1 < "+l1+" and salary_estimate_l2 < "+l2)
    jobsf = getArray(jobs)
    #print(jobsf)
    return jsonify(jobsf)
    '''

@app.route('/top/<keyword>')
def top(keyword):
    #load()
    #limpiar()

    query ="select * from jobs order by salary_estimate_l2 desc limit " + keyword
    sql = text(query)
    result = db.engine.execute(sql)
    jobsf = getArrayBD(result)
    print(sql)
    return jsonify(jobsf)

    '''
    jobs =sqldf("select * from df order by salary_estimate_l2 desc limit " + keyword)
    print(jobs)
    jobsf = getArray(jobs)
    #print(jobsf)
    return jsonify(jobsf)
    '''

@app.route('/get/<keyword>')
def getId(keyword):
    #load()
    #limpiar()

    query ="select * from jobs where id = " + keyword
    sql = text(query)
    result = db.engine.execute(sql)
    jobsf = getArrayBD(result)
    #print(jobsf)
    return jsonify(jobsf)
    '''
    jobs =sqldf("select * from df where job_number = " + keyword )
    jobsf = getArray(jobs)
    return jsonify(jobsf)
    '''

@app.route('/search/<keyword>')
def searchKey(keyword):
    #load()
    #limpiar()

    query ="select * from jobs where job_title like '%" + keyword + "%' or location like '%" + keyword + "%'"
    sql = text(query)
    result = db.engine.execute(sql)
    jobsf = getArrayBD(result)
    print(query)
    return jsonify(jobsf)

    '''
    jobs =sqldf("select * from df where job_title like '%" + keyword + "%' or Location like '%" + keyword + "%'")
    jobsf = getArray(jobs)
    
    return jsonify(jobsf)
    '''
   # return render_template('datos.html',datos =jobs)

@app.route('/uploadToDb')
def upload():
    load()
    limpiar()
    cont=0
    remove = ["'","´",","]
    for row in df.job_number:
        if cont !=1860:
            description = df.job_description[cont]
            for c in remove:
                description=description.replace(c," ")
            if ( df.rating[cont]== np.nan):
                df.rating[cont] =0

            query = "INSERT INTO jobs(id, job_title, salary_estimate_l1, salary_estimate_l2, job_description, \
                    rating, company_name, location) VALUES ("+ str(cont) +",'" + df.job_title[cont] +"'," + str(df.salary_estimate_l1[cont]) +", " + str(df.salary_estimate_l2[cont]) +", '" + description + "', \
                    " + str(df.rating[cont]) +",'" + df.company_name[cont] +"', '" + df.location[cont] +"');"
            sql = text(query)
            result = db.engine.execute(sql)
            print(sql)
        cont+=1
    return str(cont)



#---------------------------AUXILIAR FUNCTIONS --------------------------
def getArrayBD(jobs):
    jobsf = []
    for row in jobs:
        job=[]
        salary = "$" + str(row[2]/1000) + "K - $" + str(row[3]/1000) + "K"
        job.append(row[1])
        job.append(row[7])
        job.append(row[6])
        job.append(salary)
        job.append(row[5])
        job.append(row[4])
        job.append(row[0])
        jobsf.append(job)
    
    return jobsf

    
def getArray(jobs):
    jobs = jobs.to_json()
    jobs = json.loads(jobs)
    jobsf = []
   
 
    for i in range(0,len(jobs['job_title'])):
        job=[]
        job.append(jobs['job_title'][str(i)])
        job.append(jobs['location'][str(i)])
        job.append(jobs['company_name'][str(i)])
        job.append(jobs['salary_estimate'][str(i)])
        job.append(jobs['rating'][str(i)])
        job.append(jobs['job_description'][str(i)])
        job.append(jobs['job_number'][str(i)])
        jobsf.append(job)
    return jobsf


def limpiar():
    global df
    df = df.dropna()
    df = df.replace(-1,np.nan)
    df = df.replace(-1.0,np.nan)
    df = df.replace('-1',np.nan)
    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df['Easy Apply'] = df['Easy Apply'].fillna(False).astype(bool)
    new=df["Salary Estimate"].str.split(" ", n = 1, expand = True)
    sal_range=new[0].str.split('-',n=1,expand=True)
    df['salary_estimate_l1'] = sal_range[0]
    df['salary_estimate_l2'] = sal_range[1]
    
    df['salary_estimate_l1']=df['salary_estimate_l1'].str.replace('K','000')
    df['salary_estimate_l1']=df['salary_estimate_l1'].str.replace('$','')
    df['salary_estimate_l1'] = df['salary_estimate_l1'].fillna(0)
    df['salary_estimate_l1']=df['salary_estimate_l1'].astype(str).astype(int)
    df['salary_estimate_l2']=df['salary_estimate_l2'].str.replace('K','000')
    df['salary_estimate_l2']=df['salary_estimate_l2'].str.replace('$','')
    df['salary_estimate_l2'] = df['salary_estimate_l2'].fillna(0)
    df['salary_estimate_l2']=df['salary_estimate_l2'].astype(str).astype(int)
    df['Founded']=df['Founded'].fillna(0).astype(int)
    df['job_number'] = df.index
    
    df_new = df.rename(columns={'Job Title': 'job_title',
                                'Salary Estimate':'salary_estimate',
                                'Job Description' : 'job_description',
                                'Rating' : 'rating',
                                'Company Name' : 'company_name',
                                'Company Name' : 'company_name',
                                'Location' : 'location',
                                'Company Name' : 'company_name',
                                'Headquarters' : 'headquarters',
                                'Size' : 'size',
                                'Founded' : 'founded',
                                'Type of ownership' : 'type_ownership',
                                'Industry' : 'industry',
                                'Sector' : 'sector',
                                'Revenue' : 'revenue',
                                'Competitors' : 'competitors',
                                'Easy Apply' : 'easy_apply',
                                } )
    
    #df_new.drop(['Salary Estimate'], axis = 1, inplace = True)
    
    cols =['job_number','job_title','salary_estimate','salary_estimate_l1','salary_estimate_l2',
          'job_description','rating','company_name','location',
          'headquarters','size','founded',
          'type_ownership','industry','sector','revenue','competitors','easy_apply']
    
    df_new=df_new[cols]

    df=df_new

    print("Datos limpios")

def load():
    global df
    df = pd.read_csv('static/DataAnalyst.csv')
    print("Datos cargados")


if __name__ == '__main__':  
    app.run(port = 5000, debug = True)

