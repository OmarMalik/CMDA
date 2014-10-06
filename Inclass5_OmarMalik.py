# Inclass5_1
# 2. Used import command to import the libraries
# 	 Used pandas.<tab>, numpy.<tab>, matplotlib.<tab> to see what functions each of them implemented
# 3. Used to pandas.<function>? to see info about 5 different functions
#	 Used pandas.exp*? to see all functions that started with exp
# 6. Used 'paste' to paste clipboard into iPython
# 7. Used %xdel?, str.split?, import re, re?, import matplotlib.pylab, matplotlib.pylab?
# 8. randn generates 'standard normal' numbers
# 9. cumsum returns an array with the cumulative sum in each index
# 10. 100 - 4.52 microseconds. 1000 - 37 microseconds. 10000 - 359 microseconds.

# Inclass5_2
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
a.shape
b.shape
type(a)
type(b)
c = a + b
d = a * b

e = np.identity(6)
e[[2]] = 5
e[e!=0] = 6

arr3 = np.zeros((2,3,4))
arr3.shape
type(arr3)
arr3[0,1,2] = 5

arr4 = np.zeros(50)
for i in range(50):
	arr4[i] = np.random.rand()
arr4.min()
arr4.max()
arr4.sum()
arr4.mean()
np.std(arr4)
arr4[np.where(arr4 < .5)] = 0
arr4[np.where(arr4 >= .5)] = 1
arr4.sort()
set(arr4)

# Output:
"""
In []:
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
In [3]:
a.shape
Out[3]:
(5L,)
In [4]:
b.shape
Out[4]:
(5L,)
In [5]:
type(a)
Out[5]:
numpy.ndarray
In [6]:
type(b)
Out[6]:
numpy.ndarray
In [9]:
a + b
In [10]:
a * b
In [12]:
e = np.identity(6)
In [13]:
e[[2]] = 5
In [14]:
e[e!=0] = 6
In [15]:
e
Out[15]:
array([[ 6.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  6.,  0.,  0.,  0.,  0.],
       [ 6.,  6.,  6.,  6.,  6.,  6.],
       [ 0.,  0.,  0.,  6.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  6.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  6.]])
In [16]:
arr3 = np.zeros((2,3,4))
In [17]:
arr3.shape
Out[17]:
(2L, 3L, 4L)
In [18]:
type(arr3)
Out[18]:
numpy.ndarray
In [19]:
arr3[0,1,2] = 5
In [20]:
arr3
Out[20]:
array([[[ 0.,  0.,  0.,  0.],
        [ 0.,  0.,  5.,  0.],
        [ 0.,  0.,  0.,  0.]],

       [[ 0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.]]])
In [21]:
arr4 = np.zeros(50)
In [22]:
for i in range(50):
	arr4[i] = np.random.rand()
In [23]:
arr4.min()
Out[23]:
0.045372300409473709
In [24]:
arr4.max()
Out[24]:
0.95446902549735657
In [25]:
arr4.sum()
Out[25]:
24.298038765429876
In [26]:
arr4.mean()
Out[26]:
0.48596077530859749
In [27]:
np.std(arr4)
Out[27]:
0.28923698109920037
In [28]:
arr4[np.where(arr4 < .5)] = 0
In [29]:
arr4[np.where(arr4 >= .5)] = 1
In [30]:
arr4.sort()
In [31]:
set(arr4)
Out[31]:
{0.0, 1.0}
In [32]:
arr4
Out[32]:
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])
In []:
"""

# Inclass5_3
# column names: Open	High	Low	Close	Volume (BTC)	Volume (Currency)	Weighted Price
# frequency: daily
# each ind object is displaying the DatetimeIndex


# coding: utf-8

# In[58]:

import pandas
import numpy
import Quandl


# In[59]:

bitstamp = Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2011-09-13", trim_end="2014-10-05", authtoken="eXX5tF9WAyuZNdvpVwQ4")


# In[60]:

bitfinex = Quandl.get("BCHARTS/BITFINEXUSD", trim_start="2013-03-31", trim_end="2014-10-05", authtoken="eXX5tF9WAyuZNdvpVwQ4")


# In[61]:

lake = Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-03-01", trim_end="2014-10-05", authtoken="eXX5tF9WAyuZNdvpVwQ4")


# In[62]:

lake.head()


# In[63]:

ind1 = bitstamp.index
ind2 = bitfinex.index
ind3 = lake.index


# In[64]:

ind1


# In[65]:

ind2


# In[66]:

ind3


# In[67]:

bitstamp.columns


# In[68]:

bitfinex.columns


# In[69]:

lake.columns


# In[70]:

bitstamp.drop('Volume (BTC)', axis=1, inplace=True)


# In[71]:

bitfinex.drop('Volume (BTC)', axis=1, inplace=True)


# In[72]:

lake.drop('Volume (BTC)', axis=1, inplace=True)


# In[ ]:



