#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sys
get_ipython().system('{sys.executable} -m pip install beautifulsoup4')

get_ipython().system('{sys.executable} -m pip install requests')


# In[19]:


from bs4 import BeautifulSoup
import urllib.request,sys,time
import requests
import pandas as pd
import re  


# In[20]:


#url of the page that we want to Scarpe
#+str() is used to convert int datatype of the page no. and concatenate that to a URL for pagination purposes.
url = r'https://finance.yahoo.com/news/billionaire-george-soros-loads-3-144712924.html'
#Use the browser to get the URL. This is a suspicious command that might blow up.
page = requests.get(url)


# In[21]:


#for this example, we will use 'Wall Street' to prompt us if we should scrape
#can be useful in front end if we wind up doing that

if "Wall Street" in page.text:
         print("Yes, Scarpe it")


# In[22]:


page.content


# In[23]:


print(re.findall(r'\$[0-9,.]+', page.text))


# In[24]:


soup = BeautifulSoup(page.text, "html.parser")


# In[25]:


links=soup.find_all('li',attrs={'class':'o-listicle__item'})


# In[26]:


print(len(links))


# In[32]:


links = soup.find_all('a')


# In[37]:


for j in links:
        Statement = j.find("div",attrs={'class':'m-statement__quote'}).text.strip()
        Link=st.find('a')['href'].strip()
        Date = j.find('div',attrs={'class':'m-statement__body'}).find('footer').text[-14:-1].strip()
        Source = j.find('div', attrs={'class':'m-statement__author'}).find('a').get('title').strip()
        Label = j.find('div', attrs ={'class':'m-statement__content'}).find('img',attrs={'class':'c-image__original'}).get('alt').strip()
        #frame.append([Statement,Link,Date,Source,Label])
upperframe.extend(frame)


# In[ ]:




