import ipywidgets as widgets
from ipywidgets import HBox, VBox
from IPython.display import display
import pandas as pd
import numpy as np


def limpiar():
    global df
    df = df.dropna()
    df = df.replace(-1,np.nan)
    df = df.replace(-1.0,np.nan)
    df = df.replace('-1',np.nan)
    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df['Easy Apply'] = df_new['easy_apply'].fillna(False).astype(bool)
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
    
    df_new = df.rename(columns={'Job Title': 'job_title',
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


    cols =['job_title','salary_estimate','salary_estimate_l1','salary_estimate_l2',
          'job_description','rating','company_name','location',
          'headquarters','size','founded',
          'type_ownership','industry','sector','revenue','competitors','easy_apply']
    
    df_new=df_new[cols]

    df=df_new  
     
    df_new.drop(['Salary Estimate'], axis = 1, inplace = True)
    df_new['Job Title'], df_new['Department'] = df_new['job_title'].str.split(',', 1).str
    
