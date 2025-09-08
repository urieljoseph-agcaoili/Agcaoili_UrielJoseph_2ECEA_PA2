#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

X = np.random.random((5,5))
STD = X.std()
M = X.mean()
W = (X - M)
Z = W/STD

print("Normal Array: \n", X)
print("Normalized Array: \n", Z)

