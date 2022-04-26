# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:30:43 2022

@author: Karuna Singh
"""


import pandas as pd
import numpy as np

data = pd.read_excel('<File Path>Example-4.xlsx')

data.dtypes # checking data types

data['Measure X'].mean()

data['Measure X'].var()

data['Measure X'].std()

import matplotlib.pyplot as plt

plt.hist(data) # data is not normally distributed, it is positively skewed

plt.boxplot(data['Measure X']) # data is positively skewed and there are outliers
