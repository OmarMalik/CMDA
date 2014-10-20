
# coding: utf-8

# In[1]:

import pandas as pd
import xlrd
import matplotlib as mp
import matplotlib.pyplot as plt
import pylab as pl
import pickle
get_ipython().magic(u'pylab inline')


# In[2]:

olympics = pd.read_excel('OlympicAthletes_0.xlsx', encoding = 'utf-8')


# In[3]:

olympics.describe()


# In[4]:

olympics['Age'] = olympics['Age'].replace(np.nan, 0)
olympics['Athlete'] = olympics['Athlete'].replace(np.nan, "Missing")


# In[5]:

pl.xlabel("Age")
pl.ylabel("Occurances")
pl.title("Olympic Athlete Ages: Histogram")
pl.hist(olympics['Age'])
pl.show()


# In[6]:

usa_total = 0
russia_total = 0
china_total = 0

for x in olympics.itertuples():
    if x[3] == "United States":
        usa_total += x[10]
    if x[3] == "Russia":
        russia_total += x[10]
    if x[3] == "China":
        china_total += x[10]              

medal_totals = {'USA' : usa_total, 'Russia': russia_total, 'China': china_total }
countryDF = pd.DataFrame.from_dict([medal_totals])
countryDF = pd.DataFrame(countryDF.transpose())
countryDF.columns = ['Medals']
countryDF.plot(kind='bar', title="Total Medals", grid=False)


# In[7]:

tennis = 0
table_tennis = 0

for x in olympics.itertuples():
    if x[6] == "Tennis":
        tennis += x[10]
    if x[6] == "Table Tennis":
        table_tennis += x[10]

tennis_totals = {'Tennis' : tennis, 'Table Tennis': table_tennis}
tennisDF = pd.DataFrame.from_dict([tennis_totals])
tennisDF = pd.DataFrame(tennisDF.transpose())
tennisDF.columns = ['Medals']
tennisDF.plot(kind='bar', title="Total Medals Awarded", grid=False)


# In[8]:

olympics.to_pickle('olympics_pickle')