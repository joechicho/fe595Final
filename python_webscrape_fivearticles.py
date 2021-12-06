#!/usr/bin/env python
# coding: utf-8

# In[1]:


##### scraping FIVE articles

from newspaper import Article


# In[2]:


urlOne = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

#download/parse
articleOne = Article(urlOne)
articleOne.download()
articleOne.parse()

#print articleOne text
print(articleOne.text)


# In[3]:


urlTwo = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-6-2021-124642597.html'

#download/parse
articleTwo = Article(urlTwo)
articleTwo.download()
articleTwo.parse()

#print articleTwo text
print(articleTwo.text)


# In[4]:


urlThree = 'https://finance.yahoo.com/news/electric-car-maker-lucid-receives-112719438.html'

#download/parse
articleThree = Article(urlThree)
articleThree.download()
articleThree.parse()

#print articleThree text
print(articleThree.text)


# In[6]:


urlFour = 'https://finance.yahoo.com/m/68edce04-b4f4-367d-9321-a78f6f033888/bitcoin-plunges-here%E2%80%99s-why-.html'

#download/parse
articleFour = Article(urlFour)
articleFour.download()
articleFour.parse()

#print articleFour text
print(articleFour.text)


# In[7]:


urlFive = 'https://finance.yahoo.com/news/morgan-stanley-gave-overweight-rating-150000437.html'

#download/parse
articleFive = Article(urlFive)
articleFive.download()
articleFive.parse()

#print articleFive text
print(articleFive.text)


# In[ ]:




