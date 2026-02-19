#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


data = pd.read_csv("austin_weather.csv")
data


# In[3]:


data = data.drop(["Events","Date","SeaLevelPressureLowInches"], axis=1)


# In[4]:


data = data.replace("T",0.0)


# In[5]:


data = data.replace("-",0.0)


# In[6]:


data.to_csv("austin_weather_final.csv")


# In[7]:


import numpy as np
import pandas as pd 
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# In[8]:


data = pd.read_csv("austin_weather_final.csv")
data


# In[9]:


X = data.drop(["PrecipitationSumInches"], axis=1)


# In[10]:


Y = data["PrecipitationSumInches"]


# In[11]:


Y = Y.values.reshape(-1,1)


# In[16]:


Y


# In[17]:


day_index = 798
days = [i for i in range (Y.size)]


# In[18]:


clf = LinearRegression()
clf.fit(X,Y)


# In[24]:


print("The Precipitation trend Graph")
plt.scatter(days, Y, color='g')
plt.scatter(days[day_index], Y[day_index], color='r')
plt.title("Precipitation Level")
plt.xlabel("Days")
plt.ylabel("Precipitation in Inches")
plt.show()
x_vis = X.filter(["TempAvgF","DewPointAvgF", "HumidityAvgPercent", "SeaLevelPressureAvgInches", "VisibilityAvgMiles", "WindAvgMPH"])


# In[25]:


print("The Precipitation vs Attribution Trend Graph:")
for i in range(x_vis.columns.size):
    plt.subplot(3,2,i+1)
    plt.scatter(days, x_vis[x_vis.columns.values[i][:100]], color = 'g')
    plt.scatter(days[day_index], x_vis[x_vis.columns.values[i]][day_index], color = 'r')
    plt.title(x_vis.columns.values[i])
plt.show()


# In[ ]:




