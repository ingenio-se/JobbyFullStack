from flask import Flask, request, make_response,redirect,render_template, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json
from flask import jsonify
import pandas as pd
import numpy as np
from pandasql import sqldf
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io

global df

df=[]
app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/plot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    load()
    limpiar()
    fig = Figure()
    axis_1 = fig.add_subplot(1,2,1)
    axis_2 = fig.add_subplot(1,2,2)
    x = jobby['salary_mean']
    y = jobby['ESTRELLAS'].astype(dtype=int).value_counts()

    axis_1.hist(x)
    axis_2.pie(y)
    return fig
    

'''
@app.route('/data')
def data():
    
    df = pd.read_csv('static/DataAnalyst.csv')
    head  = df.head()

    for r in head.iterrows():
        print(r)
    return render_template('data.html',df = df)
'''

@app.route('/locations')
def locations():
    load()
    limpiar()
    locations=sqldf("select distinct(Location) from df ")
    locations = locations.to_json()
    print(locations)
    
    return render_template('datos.html',datos =locations)

'''
@app.route('/get/<keyword>')
def getId(keyword):
    load()
    limpiar()
    jobs =sqldf("select * from df where job_number = " + keyword )
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
    return jsonify(jobsf)
'''
@app.route('/search/<keyword>')
def searchKey(keyword):
    global jobby
    load()
    limpiar()
    jobby =sqldf("select * from df where joined_search like '%" + keyword + "%' or Location like '%" + keyword + "%'")
    jobs = jobby.to_json()
    jobs = json.loads(jobs)
    jobsf = []
   
    
    for i in range(0,len(jobs['job_title'])):
        job=[]
        job.append(jobs['job_title'][str(i)])
        job.append(jobs['location'][str(i)])
        job.append(jobs['company_name'][str(i)])
        job.append(jobs['salary_estimate'][str(i)])
        job.append(jobs['ESTRELLAS'][str(i)])
        job.append(jobs['job_description'][str(i)])
        job.append(jobs['job_number'][str(i)])
        job.append(jobs['skills'][str(i)])
        jobsf.append(job)
    return jsonify(jobsf)
   # return render_template('datos.html',datos =jobs)
def word_finder(x):
    skills = {"data", "python", "SQL", "statistics", 'tableau', "big data", "excel", "machine learning", "databases", "r", "analyst", "microsoft", "leadership","ETL"}
    df_words = set(x.split(' '))
    extract_words =  skills.intersection(df_words)
    return ', '.join(extract_words)

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

    '''
    #df_new.drop(['Salary Estimate'], axis = 1, inplace = True)
    
    cols =['job_number','job_title','salary_estimate','salary_estimate_l1','salary_estimate_l2',
          'job_description','rating','company_name','location',
          'headquarters','size','founded',
          'type_ownership','industry','sector','revenue','competitors','easy_apply']
    df_new=df_new[cols]
    '''
    df=df_new
    
    #IMPLEMENTACION DEL SALARIO PROMEDIO
    col = df.loc[: , "salary_estimate_l1":"salary_estimate_l2"]
    df['salary_mean'] = col.mean(axis=1)

    #IMPLEMENTACION DE LAS ESTRELLAS
    df.rating = df.rating.fillna(1)
    df['rating_val'] = df['rating']*0.1
    df['salary_mean_val'] = df['salary_mean']*((1/10000000)*(4**2.85))
    df['ESTRELLAS'] = round(((df['salary_mean_val'] + df['rating_val'])/.255))

    #BEST SORTED BY
    df = df.sort_values('ESTRELLAS', ascending = False)

    #TIME TO ADD SKILLS
    df['joined_search'] = df['job_title'].str.lower() + str(" ") + df['job_description'].str.lower()
    df['joined_search'] = df['joined_search'].str.replace('\n',' ')
    
    df['skills'] = df['joined_search'].apply(word_finder)
    df['skills'] = df['skills'].apply(lambda x: x.replace('analyst', 'SQL, databases'))


def load():
    global df
    df = pd.read_csv('static/DataAnalyst.csv')
    print("Datos cargados")

if __name__ == '__main__':
   
    app.run(port = 5000, debug = True)
    