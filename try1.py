# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:06:26 2020

@author: Aditya
"""

import glassdoor_data as gs
import pandas as pd
path = "C:/Users/Aditya/Documents/salary_prediction/chromedriver"
df = gs.get_jobs('data scientist',300,False,path,15)

df.to_csv('glassdoor300.csv',index=False)