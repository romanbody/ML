#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:01:37 2019

@author: romanbody
"""
import pandas as pd
import numpy as np

url='https://tinyurl.com/titanic-csv'

dataframe=pd.read_csv(url)

print dataframe.head(5)


dataframe.head

time_index = pd.date_range('06/06/2017',periods=100000,freq='30s')

dataframe1=pd.DataFrame(index=time_index)


dataframe1=pd.DataFrame(index=time_index)

dataframe1['Sale_Amount']=np.random.randint(1,10,100000)

dataframe1.resample('2W').sum()
dataframe1.resample('M').sum()
print dataframe1.resample('M').count()


