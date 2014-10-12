###########################################
# INCLASS 6_1
###########################################

# coding: utf-8

# In[39]:

import pandas as pd
import json
import requests


# In[40]:

work_tab = pd.read_table('work_tab.txt', sep='\s+')


# In[41]:

work_commas = pd.read_csv('work_comma.csv')


# In[42]:

stress2_1 = pd.read_table('stress2_1.txt', sep='\s+')


# In[43]:

work_tab


# In[44]:

work_commas


# In[45]:

stress2_1


# In[46]:

r = requests.get('https://api.github.com/events')


# In[47]:

fields = ['id', 'public', 'type', 'created_at']


# In[48]:

data_fr = pd.DataFrame(r.json(), columns=fields)


# In[49]:

data_fr


# In[50]:

data_fr.to_pickle('dframe_pickle')


# In[51]:

pd.read_pickle('dframe_pickle')


# In[52]:

store = pd.HDFStore('git_data.h5')


# In[53]:

store['obj1'] = data_fr


# In[54]:

store['obj1']



###########################################
# INCLASS 6_2
###########################################


# coding: utf-8

# In[36]:

import pandas as pd
import numpy as np
import xlrd
import datetime


# In[37]:

olympics = pd.read_excel('OlympicAthletes_0.xlsx', encoding = 'utf-8')


# In[38]:

olympics.describe()


# In[39]:

bins = [0, 15, 20, 25, 30, 100]


# In[40]:

olympics['ages'] = pd.cut(olympics['Age'], bins)


# In[41]:

ages = olympics['ages']


# In[42]:

pd.value_counts(ages)


# In[43]:

age_groups = {'(0, 15]': 'youth', '(15, 20]' : 'teen', '(20, 25]' : 'early-twenties', '(25, 30]' : 'late-twenties', '(30, 100]' : 'thirty-over'}


# In[44]:

olympics['age_groups'] = olympics['ages'].map(age_groups)


# In[45]:

olympics = olympics.rename(columns = {'Gold Medals' : 'Gold', 'Silver Medals' : 'Silver'})


# In[46]:

trainer_set1 = olympics.take(np.random.permutation(len(olympics))[0:(len(np.random.permutation(len(olympics)))/2)])


# In[47]:

trainer_set2 = olympics.take(np.random.permutation(len(olympics))[0:(len(np.random.permutation(len(olympics)))/2)])


# In[48]:

trainer_set3 = trainer_set1.append(trainer_set2)


# In[49]:

trainer_set3 = trainer_set3.drop_duplicates()


# In[50]:

print(np.float64(((len(trainer_set3) * 100) / len(trainer_set1.append(trainer_set2)))))