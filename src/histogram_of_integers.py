#!/usr/bin/env python
# coding: utf-8

# In[114]:


import numpy as np
import matplotlib.pyplot as plt

def hist(array : np.ndarray):
    """
    given array of integer values,
    returns the histogram of consecutive integer values without hole
    """
    bins = np.append(np.arange(0,array.max()+1)-0.5,array.max()+0.5)
    return np.histogram(array, bins = bins)[0]




