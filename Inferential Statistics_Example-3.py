# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 03:02:32 2021

@author: Karuna Singh
"""

import numpy as np
import pandas as pd

data = pd.read_excel('<File Path>.Example-3.xlsx')

data.dtypes # checking data type of the dataset

data.duplicated().sum() # checking for duplicate records : found none

data.isna().sum() # checking for the missng values : found none

# First Moment Business Decesion

# since all the attributes are numeric, doing mean, median & mode for the entire dataset
data.mean() 
data.median()
data.mode() # NaN in mode value for Score is because it is a unimodal data

# Second Moment Business Decesion

data.var() 
# Points column has near zero variance, this data would not be of much help

data.std()

range_p = max(data.Points) - min(data.Points)
range_p

range_S = (max(data['Score']) - min(data['Score']))
range_S

range_W = (max(data['Weigh']) - min(data['Weigh']))
range_W

# Visualization

plt.hist(data.Points)
plt.hist(data.Score)
plt.hist(data.Weigh)
