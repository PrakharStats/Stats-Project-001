#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense


# In[2]:


from sklearn.preprocessing import MinMaxScaler


# In[3]:


import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")


# In[4]:


from datetime import datetime
import datetime as dt
#start = dt.datetime(2003,1,1)
#end = dt.datetime(2022,1,1)


# In[5]:


## Importing Dataset ##
Tata_df = pd.read_csv(r"D:\NSE-Tata-Global-Beverages-Limited\TATACONSUM.NS.csv")


# In[6]:


Tata_df.describe()


# In[7]:


Tata_df.head()


# In[8]:


Tata_df.tail()


# In[9]:


## Checking for null values ##
Tata_df.isnull()


# In[10]:


Tata_df.info()


# In[13]:


## Analysing the key attributes of our dataset ##


# In[11]:


Tata_df["Date"]=pd.to_datetime(Tata_df.Date,format="%Y-%m-%d")
Tata_df.index=Tata_df['Date']


# In[12]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Close"],label='Close Price history')


# In[14]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Volume"],label='Volume history')


# In[15]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Open"],label='Open Price history')


# In[16]:


## Caculating the Moving Average of our Dataset ##


# In[17]:


ma_day = [10, 20, 50]

for ma in ma_day:
    
        column_name = f"MA for {ma} days"
        Tata_df[column_name] = Tata_df['Adj Close'].rolling(ma).mean()


# In[18]:


print(Tata_df)


# In[19]:


Tata_df.hist(figsize=(12, 12));


# In[20]:


## PLotting the Moving Average ##


# In[26]:


fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(8)
fig.set_figwidth(15)
Tata_df[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot().set_title('Tata Consumer Products Ltd')


# In[27]:


## Calculating Daily Return of the Stock on Average(Using Pandas) ##


# In[28]:


Tata_df['Daily Return'] = Tata_df['Adj Close'].pct_change()


# In[29]:


fig.set_figheight(8)
fig.set_figwidth(15)
Tata_df['Daily Return'].plot(legend=True, linestyle='--', marker='o').set_title('Tata Consumer Products Ltd')


# In[30]:


## Overall look at the average daily return using a histogram.(Using seaborn) ##


# In[31]:


plt.figure(figsize=(12, 7))
Tata_df['Daily Return'].hist(bins=50)
plt.ylabel('Daily Return')
plt.title('Tata Consumer Products Ltd')


# In[ ]:




