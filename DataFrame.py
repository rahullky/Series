#!/usr/bin/env python
# coding: utf-8

# # Data frame
# 

# In[9]:


import pandas as pd


# In[10]:


l = [2,5,6,8,7,9,6,3,5,6]

var = pd.DataFrame(l)

var


# In[11]:


d = {"a":[12,45,56,78],"b":[25,63,45,78],"c":[32,68,95,16]}

var2 = pd.DataFrame(d)


var2


# In[12]:


da = {"a":[12,45,56,78],"b":[25,63,45,78],"c":[32,68,95,16]}

var2 = pd.DataFrame(da,index=["2","2","2","2"])


var2                #updating index 


# In[15]:


k = {"x":[12,45,56,78],"y":[25,63,45,78],"z":[32,68,95,16]}

t = pd.DataFrame(k,columns=["y"])


t                        #slicing  with columns  


# In[19]:


w = {"x":[12,45,56,78],"y":[25,63,45,78]}

t = pd.DataFrame(w)

print (t["y"][2])                      # slicing with values


# In[21]:


l  = [[2,5,6,8,7,9,6,3,5,6],[2,5,3,9,7,5,3,6,1,7]]

l2 = pd.DataFrame(l)



print(l2)
print(type(l2))


       #we create nested list with Data Frame 



# In[23]:


d = {"a":pd.Series([2,5,6,8,7,3]),"b":pd.Series([2,3,4,6,4,7])}

dd = pd.DataFrame(d)

dd


#  {([]) } 


# In[ ]:




