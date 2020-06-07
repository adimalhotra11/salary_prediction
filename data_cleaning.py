# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:44:53 2020

@author: Aditya
"""

import pandas as pd
df = pd.read_csv(r'C:\Users\Aditya\Documents\salary_prediction\glassdoor300.csv')

#salary parsing 
df = df[df['Salary Estimate']!='-1' ]
salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
minus_K = salary.apply(lambda x : x.replace('K','').replace('$',''))

df['min_salary'] = minus_K.apply(lambda x : int(x.split('-')[0]))
df['max_salary'] = minus_K.apply(lambda x : int(x.split('-')[1]))
df['average salary'] = ( df.min_salary + df.max_salary  )/2
df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)
df.columns
df['same_state'] = df.apply( lambda x : 1 if x.Location == x.Headquarters else 0,axis = 1)
df.Founded.dtype
df['age'] = df.Founded.apply(lambda x : x if x < 1 else 2020 - x ) 

#requirements for job

#PYTHON
df['python'] = df['Job Description'].apply(lambda x : 1 if 'python' in x.lower() else 0)
df.python.value_counts()

#Rstudio
df['rstudio'] = df['Job Description'].apply(lambda x : 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.rstudio.value_counts()

#AWS 
df['aws'] = df['Job Description'].apply(lambda x : 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#EXCEL
df['excel'] = df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#APACHE
df['spark'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#DOCKER/Kubernetes
df['kubernetes'] = df['Job Description'].apply(lambda x : 1 if 'docker' in x.lower() or 'kubernetes' in x.lower() else 0)
df.kubernetes.value_counts()

df_out = df.drop(['apache','docker'],axis=1)
#df.drop(['docker'],axis=1)

df_out.to_csv('clean_prediction.csv',index=False)

