#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get('https://www.ncsl.org/research/energy/state-gas-pipelines.aspx')


# In[7]:


doc = BeautifulSoup(response.text, 'html.parser')
doc


# In[9]:


table = doc.find('table')
len(table)


# In[11]:


table


# In[17]:


trs = table.find_all('tr')
trs[4]


# In[21]:


table_data = []
for tr in trs[4:]:
    tds = tr.find_all('td')
    cells = []
    for td in tds:
        cells.append(td.text.strip())
    table_data.append(cells)
table_data


# In[24]:


df = pd.DataFrame(table_data[1:-4], columns = None)


# In[25]:


df


# In[26]:


df = df.rename(columns={
    0: 'jurisdiction',
    1:'harzardous_liquid',
    2:'gas_transmission',
    3:'gas_gathering',
    4:'gas_distribution',
    5:'total',
    6:'total_gas_pipeline_mileage'
})


# In[27]:





# In[28]:


df.to_csv('pipeline_mileage.csv')


# In[ ]:




