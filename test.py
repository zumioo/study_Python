#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas as pd
pd = ""
#↑jupyterでは上のコメントを外し、pdの変数宣言を消す

# In[28]:


df_population_data = pd.read_csv('data.csv')


# In[29]:


df_population_data


# In[4]:


type(df_population_data)


# In[ ]:


pd.set_option('dysplay.max_rows',1000) #最大表示行数変更


# In[ ]:


pd.reset_option('dysplay.max_rows') #上の設定をリセット


# In[ ]:


pd.set_option('dysplay.max_colums',5) #表示する行数を５列に制限


# In[ ]:


pd.reset_option('dysplay.max_colums') #上の設定をリセット


# In[ ]:


df_population_data.tail(10) #下から１０行表示


# In[16]:


df_population_data.sample(10) #ランダムに１０行表示


# In[17]:


df_population_data.info() #各行のデータ型などを表示する


# In[23]:


df_population_data.describe()


# In[24]:


df_population_data.describe().round(0) #桁数を丸めることができる


# In[21]:


df_population_data.describe(include="all")


# In[25]:


df_population_data.info()


# In[30]:


df_population_data['人口（総数）'].astype(int)


# In[31]:


df_population_data.info()


# In[32]:


df_population_data['都道府県コード'].astype(int)
#csvファイルの項目について型変換ができる


# In[33]:


df_population_data.describe(include="all")


# In[34]:


df_population_data.describe().round(0)


# In[35]:


df_population_mean = df_population_data.groupby(by='都道府県名').mean()[['人口（総数）','人口（男）','人口（女）']].round(0)


# In[36]:


df_population_data.groupby(by='都道府県名').mean()[['人口（総数）','人口（男）','人口（女）']].round(0)


# In[40]:


df_population_mean.sort_values(by='人口（総数）',ascending=False) #ソートする


# In[42]:


df_population_data[df_population_data['都道府県名']=='東京都'][['人口（男）','人口（女）']].plot(color=['skyblue','pink']) #表を作成


# In[44]:


df_population_data[df_population_data['都道府県名']=='東京都'][['人口（男）','人口（女）']].plot(kind='bar',color=['skyblue','pink']) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




