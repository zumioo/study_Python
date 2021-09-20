#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas as dtf
dtf = ""
#↑jupyterでは上のコメントを外し、pdの変数宣言を消す

# In[2]:


left = dtf.DataFrame({'name':['aaa','bbb','ccc','ddd'],'age':[24,33,27,42]})
right = dtf.DataFrame({'name':['eee','bbb','aaa','fff','ddd'],'group':['x','y','y','x','x']}) #表作成


# In[3]:


left


# In[5]:


dtf.merge(left,right) #表結合


# In[6]:


dtf.merge(left,right,how='outer') #どちらかの表にしか値が無い場合でも結合させる


# In[7]:


dtf.concat([left,right]) #単純に縦に表結合させる


# In[8]:


dtf.concat([left,right],axis=1) #キーに関係なく横に結合させる


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




