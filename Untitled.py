#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r'C:\Users\theja\Downloads\Bos3d_ModelCatalog_20210830.csv',low_memory=False)
pd.set_option('display.max_columns', None)
data_top = df.head() 
    
# display 
data_top 
df.count()


# In[38]:


result_df = pd.DataFrame()
df.dropna()
result_df = df[df['Centr_Lat'] >= 42.3253972]
result_df1 = result_df[result_df['Centr_Lat'] <= 42.3543828]
result_df2 = result_df1[result_df1['Centr_Lon'] >= -71.107075]
result_df3 = result_df2[result_df2['Centr_Lon'] <= -71.070445]
result_df35 = result_df3[result_df3['StructType'] == "Building"]
result_df4 = result_df4[result_df4['Height_Ft'] >= 60]

print("Results of Buildings within a 1 Mile Radius of Richards Hall and Greater than 60ft")
result_df4.count()


# In[ ]:




