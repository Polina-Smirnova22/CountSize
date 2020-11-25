#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
    def CountSize(path):
        dirs = os.listdir(path)
        size = 0
            for file in dirs:
                size += os.path.getsize(path)
        print(size)


# In[4]:


CountSize("C://Windows/")

