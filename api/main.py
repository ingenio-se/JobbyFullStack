from flask import Flask, request, make_response,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import json
from flask import jsonify
import pandas as pd
import numpy as np
from pandasql import sqldf
from tabulate import tabulate

global df

df=[]
app = Flask(__name__, static_folder='../build', static_url_path='/')


#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:80085700@localhost:5432/jobby"
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

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

@app.route('/search/<keyword>')
def searchKey(keyword):
    load()
    limpiar()
    jobs =sqldf("select * from df where job_title like '%" + keyword + "%' or Location like '%" + keyword + "%'")
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
   # return render_template('datos.html',datos =jobs)

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
    '''
    #AQUI SE ASIGNAN LAS ESTRELLAS
    df['rating_val'] = df['rating']*0.1
    df['salary_mean_val'] = df['salary_mean']*((1/10000000)*(4**3))
    df['ESTRELLAS'] = round(((df['salary_mean_val'] + df['rating_val'])/.255),1)

    #DATASET ORDENADO POR ESTRELLAS
    df = df.sort_values('ESTRELLAS', ascending = False)
    '''

    print("Datos limpios")

def rango_de_salarios():
    range_slider = widgets.FloatRangeSlider(
                                            value=[0., +100.],
                                            min=10., max=+150., step=5,
                                            description='\$ - $$$:',
                                            readout_format='.1f',
                                            )
    range_slider
    x,y = range_slider.value
    a = int(x*1000)
    b = int(y*1000)
    rango = b-a

    df_final1 = df.drop(df[df['salary_estimate_l1'] <= a].index)
    df_final2 = df.drop(df[df['salary_estimate_l2'] <= (a+rango)].index)

    df_salary = pd.concat([df_final1,df_final2]).drop_duplicates(keep=False)
    df_salary.head()
def calificacion_empleo():
    df_fun = df_salary
    df_fun.rating = df_fun.rating.fillna(1)
    col = df_fun.loc[: , "salary_estimate_l1":"salary_estimate_l2"]
    df_fun['salary_mean'] = col.mean(axis=1)
    
    #AQUI SE ASIGNAN LAS ESTRELLAS
    df_fun['rating_val'] = df_fun['rating']*0.1
    df_fun['salary_mean_val'] = df_fun['salary_mean']*((1/10000000)*(4**3))
    df_fun['ESTRELLAS'] = round(((df_fun['salary_mean_val'] + df_fun['rating_val'])/.255),1)

    #DATASET ORDENADO POR ESTRELLAS
    df_fun_s = df_fun.sort_values('ESTRELLAS', ascending = False)
    df_fun_s.drop(['easy_apply'], axis = 1, inplace = True)
    #df_fun_s.drop(['salary_mean'], axis = 1, inplace = True)
    df_fun_s.drop(['rating_val'], axis = 1, inplace = True)
    df_fun_s.drop(['salary_mean_val'], axis = 1, inplace = True)
    df_fun_s.tail()

def grafica_empleo():
    not_now = df_fun_s[["job_title","job_description","ESTRELLAS", 'salary_mean']]

    ## INSERTAR BUSQUEDA ##

    not_now['job_description'] = not_now['job_description']
    not_now['joined_search'] = not_now['job_title'].str.lower() + str(" ") + not_now['job_description'].str.lower()
    busqueda = title_textbox.value
    not_now = not_now[not_now['joined_search'].str.contains(busqueda)]
    not_now["ESTRELLAS"] = not_now["ESTRELLAS"].astype(dtype = int)
    graph_estrella = not_now["ESTRELLAS"].value_counts()
    graph_estrella = graph_estrella.sort_index()
    graph_estrella.plot.pie()
    graph_salario = not_now[['salary_mean',"ESTRELLAS"]]
    graph_salario = graph_salario.sort_values(by =  'salary_mean')
    graph_salario.plot.kde(x='ESTRELLAS', y = 'salary_mean')

def skills():
    new_clean = df
    new_clean['job_description'] = new_clean['job_description'].str.replace('\n',' ')

    ##EL DATAFRAME xx NOS DARA LAS PALABRAS MAS REPETIDAS
    xx= pd.Series(' '.join(new_clean['job_description']).lower().split()).value_counts()[:1000]
    ####################################################### 

    skills = {"python", "python,", "sql", "SQL", "statistics", 'tableau', "big data", "excel", "machine learning", "databases", "r", "analyst", "microsoft", "leadership","ETL"}
    def word_finder(x):
        df_words = set(x.split(' '))
        extract_words =  skills.intersection(df_words)
        return ', '.join(extract_words)
    
    new_clean['skills'] = new_clean["job_description"].apply(word_finder)
    new_clean.head()


def load():
    global df
    df = pd.read_csv('static/DataAnalyst.csv')
    print("Datos cargados")

if __name__ == '__main__':
   
    app.run(port = 5000, debug = True)
    