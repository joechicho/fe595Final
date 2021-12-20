#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Download pymysql package:
import sys
get_ipython().system('{sys.executable} -m pip install pymysql')


# In[2]:


# Import pymsql:
import pymysql


# In[3]:


# Connect our Workbench to python:
conn = pymysql.connect(host = 'final-project-fe595-group7.cz2xzj6pvabe.us-east-2.rds.amazonaws.com',
                      port = 3306,
                      user = 'admin',
                      password = 'group72021',
                      db = 'FinalprojectFE595Group7')


# In[6]:


# Create table in our workbench:
# DO NOT RUN AGAIN
cursor = conn.cursor()
create_table = """
create table ArticleData (title varchar(500), year int, source varchar(200), link varchar(500), text varchar(20000))"""
cursor.execute(create_table)


# In[7]:


# Function to query data
def get_data():
    cur=conn.cursor()
    cur.execute("SELECT * FROM ArticleData")
    data = cur.fetchall()
    return data


# In[8]:


# Test query:
get_data()


# In[ ]:




