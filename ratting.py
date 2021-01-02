#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pandas import DataFrame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import numpy as np

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# In[3]:


jul_raw = pd.read_csv('datasets/jul_2020.csv', engine = 'python')
aug_raw = pd.read_csv('datasets/aug_2020.csv', engine = 'python')
sep_raw = pd.read_csv('datasets/sep_2020.csv', engine = 'python')
oct_raw = pd.read_csv('datasets/oct_2020.csv', engine = 'python')
nov_raw = pd.read_csv('datasets/nov_2020.csv', engine = 'python')
dec_raw = pd.read_csv('datasets/dec_2020.csv', engine = 'python')


# In[4]:


frames = [jul_raw, aug_raw, sep_raw, oct_raw, nov_raw, dec_raw]
raw_data = pd.concat(frames)
print(len(raw_data))
raw_data[['Star Rating', 'Review Text']][:10]


# In[5]:


raw_data['Star Rating'].value_counts().plot(kind='bar')


# In[6]:


is_bad_rating = raw_data['Star Rating'] <= 4
is_review_available = pd.notnull(raw_data['Review Text'])
bad_ratting = raw_data[is_bad_rating]
bad_ratting_with_review = raw_data[is_bad_rating & is_review_available]
print(len(bad_ratting_with_review))


# In[8]:


bad_ratting_with_review[['Star Rating', 'Review Text', 'App Version Name']][:30]


# In[ ]:




