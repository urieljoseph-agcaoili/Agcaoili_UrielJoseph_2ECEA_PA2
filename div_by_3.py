#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

A = np.arange(1,101)
np.shape(A)
squares = A.reshape(10,10)**2
divby3 = squares[squares%3==0]

print("Array 10 x 10: \n", squares)
print("Numbers that are divisible by 3: \n", divby3)

