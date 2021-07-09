#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC

clf = SVC()
iris = datasets.load_iris()
clf.fit(iris.data, iris.target_names[iris.target])


# In[ ]:




