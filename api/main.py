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
app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:80085700@localhost:5432/jobby"
#db = SQLAlchemy(app)

'''
class ProductsModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String())
    

    def __init__(self, product):
        self.product = product

    def __repr__(self):
        return f"<Product {self.product}>"


@app.route('/products', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        products = ProductsModel.query.all()
        results = [
            {
                "product": product.product,
                
            } for product in products]

        return {"count": len(results), "Products": results}


@app.route('/query', methods=['POST', 'GET'])
def handle_query():

    queryProducts ="select distinct(product) from products order by product asc"
    sql = text(queryProducts)
    result = db.engine.execute(sql)
    listaProducts = [row for row in result]

    print(listaProducts)

    if request.method == 'GET':
        lista = []
    if request.method == 'POST':
        product = request.form['product']
          
        sql = text("SELECT products.product,countries.country,currencies.abbreviation,ps.price, \
        (ps.price * currencies.us_equ) as USD \
        FROM \
        products inner join products_suppliers as ps on products.id = ps.product_id \
        inner join suppliers on ps.supplier_id = suppliers.id \
        inner join cities on cities.id = suppliers.city_id \
        inner join countries on countries.id = cities.country_id \
        inner join currencies on currencies.id = ps.currency_id\
        where  \
            products.product = '" + product + "' order by USD desc")
        result = db.engine.execute(sql)
        lista = [row for row in result]
    
        print(lista)

    context ={
        'lista': lista,
        'listaProducts':listaProducts,
       
    }

    #return 'hola'
    return render_template('consulta.html',**context)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response


'''
@app.route('/data')
def data():
    
    df = pd.read_csv('static/DataAnalyst.csv')

    '''
    df = df.dropna()
    df = df.replace(-1,np.nan)
    df = df.replace(-1.0,np.nan)
    df = df.replace('-1',np.nan)
    df['Job Title'], df['Department'] = df['Job Title'].str.split(',', 1).str
    df['Easy Apply'] = df['Easy Apply'].fillna(False).astype(bool)
    df.drop(['Salary Estimate'], axis = 1, inplace = True)
    df.drop(['Competitors'], axis = 1, inplace = True)
    df.drop(['Department'], axis = 1, inplace = True)
    '''
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

@app.route('/search/<keyword>')
def my_view_func(keyword):
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
    
    cols =['job_title','salary_estimate','salary_estimate_l1','salary_estimate_l2',
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