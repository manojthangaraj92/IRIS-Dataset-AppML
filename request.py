#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sepal_length':5, 'sepal_width':1.5, 'petal_length':1.5, 'petal_width':0.3})

print(r.json())

