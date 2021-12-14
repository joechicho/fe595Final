#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install newspaper3k')


# In[12]:


from newspaper import Article


# In[13]:


urlOne = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

articleOne = Article(urlOne)
articleOne.download()
articleOne.parse()

titleOne= articleOne.title
yearOne= '2021'
sourceOne= 'Yahoo'
textOne = articleOne.text


# In[14]:


urlTwo = 'https://finance.yahoo.com/news/december-2021-fomc-preview-federal-reserve-100713885.html'

articleTwo = Article(urlTwo)
articleTwo.download()
articleTwo.parse()

titleTwo= articleTwo.title
yearTwo= '2021'
sourceTwo= 'Yahoo'
textTwo = articleTwo.text


# In[15]:


urlThree = 'https://finance.yahoo.com/news/we-need-to-talk-about-2023-yes-already-morning-brief-101147700.html'

articleThree = Article(urlThree)
articleThree.download()
articleThree.parse()

titleThree= articleThree.title
yearThree= '2021'
sourceThree= 'Yahoo'
textThree = articleThree.text


# In[16]:


urlFour = 'https://finance.yahoo.com/news/hedge-funds-warm-up-to-crypto-as-institutional-involvement-expands-175512467.html'

articleFour = Article(urlFour)
articleFour.download()
articleFour.parse()

titleFour= articleFour.title
yearFour= '2021'
sourceFour= 'Yahoo'
textFour = articleFour.text


# In[17]:


urlFive = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-14-2021-232905142.html'

articleFive = Article(urlFive)
articleFive.download()
articleFive.parse()

titleFive= articleFive.title
yearFive= '2021'
sourceFive= 'Yahoo'
textFive = articleFive.text


# In[19]:


urlSix = 'https://ournextlife.com/2020/03/25/future-of-fire/'

articleSix = Article(urlSix)
articleSix.download()
articleSix.parse()

titleSix= articleSix.title
yearSix= '2020'
sourceSix= 'Our Next Life'
textSix = articleSix.text


# In[20]:


urlSeven = 'https://wrachelwrites.com/2020/04/20/unpopular-opinion-why-automating-your-savings-is-overrated/'

articleSeven = Article(urlSeven)
articleSeven.download()
articleSeven.parse()

titleSeven= articleSeven.title
yearSeven= '2020'
sourceSeven= 'Wrachel Writes'
textSeven = articleSeven.text


# In[21]:


urlEight = 'https://www.newsday.com/business/coronavirus/smart-shop-li-grocery-delivery-coronavirus-1.43709225'

articleEight = Article(urlEight)
articleEight.download()
articleEight.parse()

titleEight= articleEight.title
yearEight= '2020'
sourceEight= 'Newsday'
textEight = articleEight.text


# In[22]:


urlNine = 'https://www.juststartinvesting.com/when-to-max-out-401k/'

articleNine = Article(urlNine)
articleNine.download()
articleNine.parse()

titleNine= articleNine.title
yearNine= '2019'
sourceNine= 'Just Start Investing'
textNine = articleNine.text


# In[23]:


urlTen = 'https://www.campfirefinance.com/are-side-hustles-worth-it/'

articleTen = Article(urlTen)
articleTen.download()
articleTen.parse()

titleTen= articleTen.title
yearTen= '2019'
sourceTen= 'Camp Fire Finance'
textTen = articleTen.text


# In[24]:


import pandas as pd


# In[40]:


titles = [titleOne,titleTwo,titleThree,titleFour,titleFive,titleSix,titleSeven,titleEight,titleNine,titleTen]
year = [yearOne,yearTwo,yearThree,yearFour,yearFive,yearSix,yearSeven,yearEight,yearNine,yearTen]
source = [sourceOne,sourceTwo,sourceThree,sourceFour,sourceFive,sourceSix,sourceSeven,sourceEight,sourceNine,sourceTen]
url = [urlOne,urlTwo,urlThree,urlFour,urlFive,urlSix,urlSeven,urlEight,urlNine,urlTen]
body = [textOne,textTwo,textThree,textFour,textFive,textSix,textSeven,textEight,textNine,textTen]


# In[51]:


df = pd.DataFrame({'Title': [ titles[0], titles[1], titles[2], titles[3], titles[4], titles[5], titles[6], titles[7], titles[8], titles[9] ],
                   'Year': [year[0], year[1], year[2], year[3], year[4], year[5], year[6], year[7], year[8], year[9] ],
                   'Source': [source[0], source[1], source[2], source[3], source[4], source[5], source[6], source[7], source[8], source[9]],
                   'URL': [url[0], url[1], url[2], url[3], url[4], url[5], url[6], url[7], url[8], url[9]],
                    'Body': [body[0], body[1], body[2], body[3], body[4], body[5], body[6], body[7], body[8], body[9]]})


# In[52]:


#df = pd.DataFrame({'Title': titleOne,titleTwo,titleThree,titleFour,titleFive,titleSix,titleSeven,titleEight,titleNine,titleTen,
                  # 'Year': {yearOne,yearTwo,yearThree,yearFour,yearFive,yearSix,yearSeven,yearEight,yearNine,yearTen},
                  # 'Source': {sourceOne,sourceTwo,sourceThree,sourceFour,sourceFive,sourceSix,sourceSeven,sourceEight,sourceNine,sourceTen},
                 #  'URL': {urlOne,urlTwo,urlThree,urlFour,urlFive,urlSix,urlSeven,urlEight,urlNine,urlTen},
                  #  'Body': {textOne,textTwo,textThree,textFour,textFive,textSix,textSeven,textEight,textNine,textTen}})


# In[53]:


file_name = 'Articles.xlsx'
df.to_excel(file_name)


# In[ ]:




