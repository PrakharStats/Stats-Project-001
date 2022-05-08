#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense


# In[21]:


from sklearn.preprocessing import MinMaxScaler


# In[22]:


import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")


# In[23]:


from datetime import datetime
import datetime as dt
#start = dt.datetime(2003,1,1)
#end = dt.datetime(2022,1,1)


# In[24]:


## Importing Dataset ##
Tata_df = pd.read_csv(r"D:\NSE-Tata-Global-Beverages-Limited\TATACONSUM.NS.csv")


# In[25]:


Tata_df.describe()


# In[26]:


Tata_df.head()


# In[27]:


Tata_df.tail()


# In[28]:


## Checking for null values ##
Tata_df.isnull().sum()
#Tata_df = Tata_df.dropna()
#Tata_df['Volume'][0] = Tata_df['Volume'].head(7).mean()


# In[29]:


Tata_df = Tata_df.dropna()


# In[30]:


Tata_df['Volume'][0] = Tata_df['Volume'].head(7).mean()


# In[31]:


Tata_df.isnull().sum()


# In[32]:


Tata_df.info()


# In[33]:


## Analysing the key attributes of our dataset ##


# In[34]:


Tata_df["Date"]=pd.to_datetime(Tata_df.Date,format="%Y-%m-%d")
Tata_df.index=Tata_df['Date']


# In[35]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot 
import cufflinks as cf
init_notebook_mode(connected=True)
cf.go_offline()


# In[36]:


Tata_df['Close'].iplot(kind = 'line',title = 'Close Price History')


# In[37]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Close"],label='Close Price history')


# In[38]:


Tata_df['Volume'].iplot(kind = 'line',title = 'Volume History')


# In[39]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Volume"],label='Volume history')


# In[40]:


Tata_df["Open"].iplot(kind = 'line',title = 'Open Price History')


# In[41]:


plt.figure(figsize=(16,8))
plt.plot(Tata_df["Open"],label='Open Price history')


# In[42]:


## Caculating the Moving Average of our Dataset ##


# In[43]:


ma_day = [10, 20, 50]

for ma in ma_day:
    
        column_name = f"MA for {ma} days"
        Tata_df[column_name] = Tata_df['Adj Close'].rolling(ma).mean()


# In[44]:


print(Tata_df)


# In[45]:


Tata_df.hist(figsize=(12, 12));


# In[46]:


## PLotting the Moving Average ##


# In[48]:



fig.set_figheight(8)
fig.set_figwidth(15)
Tata_df[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot().set_title('Tata Consumer Products Ltd')


# In[49]:


## Calculating Daily Return of the Stock on Average(Using Pandas) ##


# In[50]:


Tata_df['Daily Return'] = Tata_df['Adj Close'].pct_change()


# In[51]:


fig.set_figheight(8)
fig.set_figwidth(15)
Tata_df['Daily Return'].plot(legend=True, linestyle='--', marker='o').set_title('Tata Consumer Products Ltd')


# In[52]:


## Overall look at the average daily return using a histogram.(Using seaborn) ##


# In[53]:


plt.figure(figsize=(12, 7))
Tata_df['Daily Return'].hist(bins=50)
plt.ylabel('Daily Return')
plt.title('Tata Consumer Products Ltd')


# In[ ]:




