###############################
# Inclass 7_1
###############################


# coding: utf-8

# In[7]:

import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import xlrd
import datetime
import pylab as pl
import scipy


# In[8]:

olympics = pd.read_excel('OlympicAthletes_0.xlsx', encoding = 'utf-8')
olympics['Age'] = olympics['Age'].replace(np.nan, 0)


# In[9]:

pl.xlabel("Age")
pl.ylabel("Occurances")
pl.title("Olympic Athlete Ages: Histogram")
pl.hist(olympics['Age'])

plt.savefig('histogram.png') 


# In[10]:

pl.xlabel("Age")
pl.ylabel("Occurances")
pl.title("Olympic Athlete Ages: Density Plot")
olympics['Age'].plot(kind='kde')

plt.savefig('density_plot.png')


# In[12]:

bronze = olympics['Bronze Medals'] >= 1
silver = olympics['Silver Medals'] >= 1
gold = olympics['Gold Medals'] >= 1

usa = olympics.Country == "United States"
russia = olympics.Country == "Russia"
china = olympics.Country == "China"
japan = olympics.Country == "Japan"
germany = olympics.Country == "Germany"
greatBritain = olympics.Country == "Great Britain"

usaBronze = len(olympics[usa & bronze])
russiaBronze = len(olympics[russia & bronze])
chinaBronze = len(olympics[china & bronze])
japanBronze = len(olympics[japan & bronze])
germanyBronze = len(olympics[germany & bronze])
greatBritainBronze = len(olympics[greatBritain & bronze])

usaSilver = len(olympics[usa & silver])
russiaSilver = len(olympics[russia & silver])
chinaSilver = len(olympics[china & silver])
japanSilver = len(olympics[japan & silver])
germanySilver = len(olympics[germany & silver])
greatBritainSilver = len(olympics[greatBritain & silver])

usaGold = len(olympics[usa & gold])
russiaGold = len(olympics[russia & gold])
chinaGold = len(olympics[china & gold])
japanGold = len(olympics[japan & gold])
germanyGold = len(olympics[germany & gold])
greatBritainGold = len(olympics[greatBritain & gold])

bronzeCountries = {'USA' : usaBronze, 'Russia': russiaBronze, 'China': chinaBronze,
                   'Japan': japanBronze ,'Germany': germanyBronze, 'Great Britain': greatBritainBronze}

silverCountries = {'USA' : usaSilver, 'Russia': russiaSilver, 'China': chinaSilver,
                   'Japan': japanSilver , 'Germany': germanySilver, 'Great Britain': greatBritainSilver}

goldCountries = {'USA' : usaGold, 'Russia': russiaGold, 'China': chinaGold, 'Japan': japanGold , 'Germany': germanyGold,
        'Great Britain': greatBritainGold}

countryDF = pd.DataFrame.from_dict([bronzeCountries, silverCountries, goldCountries])
countryDF = pd.DataFrame(countryDF.transpose())
countryDF.columns = ['Bronze', 'Silver', 'Gold']

colors=['orange', 'silver', 'gold']
countryDF.plot(kind='bar', title="Total Medals", color=colors)

plt.savefig('bar1.png') 


# In[13]:

countryRel = countryDF.div(countryDF.sum(1).astype(float), axis=0)

colors=['orange', 'silver', 'gold']
countryRel.plot(kind='barh', stacked=True, title="Total Medals: Relative", color=colors)

plt.savefig('bar2.png') 


# In[14]:

plt.title("Gold Medals vs. Age : Scatterplot")
plt.xlabel("Age")
plt.ylabel("Gold Medals")
plt.scatter(olympics['Age'], olympics['Gold Medals'])

plt.savefig('scatter1.png') 



###############################
# Inclass 7_2
###############################


# coding: utf-8

# In[6]:

import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
get_ipython().magic(u'pylab inline')


# In[7]:

medical = pd.read_csv('Medical.csv') 

medical.replace(to_replace='HIGH',value=1, inplace=True)
medical.replace(to_replace='LOW',value=0, inplace=True)


# In[8]:

X = array(medical[['Age', 'HgA1C']])
y = array(medical['A Literacy Category'])


# In[9]:

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)


# In[10]:

scaler = StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


# In[11]:

clf = SGDClassifier()
clf.fit(x_train, y_train)


# In[12]:

print 'Classifier Equation: ' + str(clf.intercept_[0]) +' + (' + str(clf.coef_[0][0]) + ')* x1 + (' + str(clf.coef_[0][1]) + ')* x2 = 0'


# In[13]:

y_train_prediction = clf.predict(x_train)
print "{0:.2f}% accuray".format(metrics.accuracy_score(y_train, y_train_prediction) * 100)


# In[14]:

y_test_prediction = clf.predict(x_test)
print "{0:.2f}% accuray".format(metrics.accuracy_score(y_test, y_test_prediction) * 100)


# In[15]:

m1 = metrics.confusion_matrix(y_train, y_train_prediction)
m2 = metrics.confusion_matrix(y_test, y_test_prediction)


# In[16]:

print m1
print """The classifier incorrectly predicted LOW 0 times, and HIGH 4 times;
The classifier correctly predicted LOW 0 times, and HIGH 33 times."""


# In[17]:

print m2
print "The classifier correctly predicted 13 times."


# In[18]:

# The test sets classifier is very good because it "correctly" 
# identified 100% of the literacy levels given the age and HgA1C Level.



###############################
# Inclass 7_3
###############################


# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

import sklearn as sk
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt


## Principal Components Analysis

#### Dimensionality Reduction and Visualization

####### #Get the digits data

# In[3]:

from sklearn.datasets import load_digits
digits = load_digits()


####### #What does the digits dataset contain?

# In[4]:

print digits.keys()


####### #Each row of data in X_digits corresponds to one of the following digits:

# In[5]:

digits.target_names


# In[6]:

X_digits, y_digits = digits.data, digits.target


####### #What does the X matrix look like?

# In[7]:

X_digits.shape


####### #Get the first 10 principal components of the X_digits matrix

# In[8]:

from sklearn.decomposition import PCA

estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)


####### #What does the PCA matrix looks like

# In[9]:

X_pca.shape


# In[10]:

X_pca


####### #Visualize our data using the first two principal components in a scatterplot

# In[11]:

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')


# In[12]:

# 0, 1, and 6 are easiest to seperate.
# 3, 5, 8 and 9 are more easily confounded


# In[13]:

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 8][y_digits == i]
    py = X_pca[:, 9][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('Ninth Principal Component')
plt.ylabel('Tenth Principal Component')


# In[ ]:

# The new visualization makes it much harder to distinguish between images of digits.

