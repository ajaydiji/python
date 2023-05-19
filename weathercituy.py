#!/usr/bin/env python
# coding: utf-8

print("Hello world")


# In[3]:


import requests


# In[4]:


import json


# In[91]:


mycity = 'Kochi'


# In[92]:


url = 'http://api.weatherapi.com/v1/forecast.json?key=8565336e43f7432baa255530231905 &q=' + mycity + '&days=1&aqi=no&alerts=no'


# In[93]:


response = requests.get(url)


# In[94]:


print(response)


# In[95]:


weather_dict = json.loads(response.text)


# In[96]:


print(response.text)


# In[97]:


weather_dict


# In[80]:


weather_dict['forecast']['forecastday']


# In[90]:


for d in weather_dict['forecast']['forecastday']:
    print("The average temperature on " + d['date'] + " is " + str(d['day']['avgtemp_c']) + ' centigrade')
    print(" and chance of rain is " + str(d['day']['daily_will_it_rain']))


# In[68]:


for h in weather_dict['forecast']['forecastday']:
    print(h)


# In[ ]:




