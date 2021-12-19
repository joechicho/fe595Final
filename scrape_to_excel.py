#!/usr/bin/env python
# coding: utf-8

# In[1]:


from newspaper import Article


# In[2]:


urlOne = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

articleOne = Article(urlOne)
articleOne.download()
articleOne.parse()

titleOne= articleOne.title
yearOne= '2021'
sourceOne= 'Yahoo'
textOne = articleOne.text


# In[3]:


urlTwo = 'https://finance.yahoo.com/news/december-2021-fomc-preview-federal-reserve-100713885.html'

articleTwo = Article(urlTwo)
articleTwo.download()
articleTwo.parse()

titleTwo= articleTwo.title
yearTwo= '2021'
sourceTwo= 'Yahoo'
textTwo = articleTwo.text


# In[4]:


urlThree = 'https://finance.yahoo.com/news/we-need-to-talk-about-2023-yes-already-morning-brief-101147700.html'

articleThree = Article(urlThree)
articleThree.download()
articleThree.parse()

titleThree= articleThree.title
yearThree= '2021'
sourceThree= 'Yahoo'
textThree = articleThree.text


# In[5]:


urlFour = 'https://finance.yahoo.com/news/hedge-funds-warm-up-to-crypto-as-institutional-involvement-expands-175512467.html'

articleFour = Article(urlFour)
articleFour.download()
articleFour.parse()

titleFour= articleFour.title
yearFour= '2021'
sourceFour= 'Yahoo'
textFour = articleFour.text


# In[6]:


urlFive = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-14-2021-232905142.html'

articleFive = Article(urlFive)
articleFive.download()
articleFive.parse()

titleFive= articleFive.title
yearFive= '2021'
sourceFive= 'Yahoo'
textFive = articleFive.text


# In[7]:


urlSix = 'https://www.apa.org/monitor/2021/01/top-journal-articles'

articleSix = Article(urlSix)
articleSix.download()
articleSix.parse()

titleSix= articleSix.title
yearSix= '2020'
sourceSix= 'American'
textSix = articleSix.text


# In[8]:


urlSeven = 'https://wrachelwrites.com/2020/04/20/unpopular-opinion-why-automating-your-savings-is-overrated/'

articleSeven = Article(urlSeven)
articleSeven.download()
articleSeven.parse()

titleSeven= articleSeven.title
yearSeven= '2020'
sourceSeven= 'Wrachel Writes'
textSeven = articleSeven.text


# In[9]:


urlEight = 'https://www.newsday.com/business/coronavirus/smart-shop-li-grocery-delivery-coronavirus-1.43709225'

articleEight = Article(urlEight)
articleEight.download()
articleEight.parse()

titleEight= articleEight.title
yearEight= '2020'
sourceEight= 'Newsday'
textEight = articleEight.text


# In[10]:


urlNine = 'https://www.juststartinvesting.com/when-to-max-out-401k/'

articleNine = Article(urlNine)
articleNine.download()
articleNine.parse()

titleNine= articleNine.title
yearNine= '2019'
sourceNine= 'Just Start Investing'
textNine = articleNine.text


# In[11]:


urlTen = 'https://www.campfirefinance.com/are-side-hustles-worth-it/'

articleTen = Article(urlTen)
articleTen.download()
articleTen.parse()

titleTen= articleTen.title
yearTen= '2019'
sourceTen= 'Camp Fire Finance'
textTen = articleTen.text


# In[12]:


url11 = 'https://finance.yahoo.com/news/this-week-in-bidenomics-build-back-later-182525299.html'

article11 = Article(url11)
article11.download()
article11.parse()

title11= article11.title
year11= '2021'
source11= 'Yahoo'
text11 = article11.text


# In[13]:


url12 = 'https://finance.yahoo.com/news/us-eyes-crypto-climate-among-potential-risks-to-financial-stability-175240868.html'

article12 = Article(url12)
article12.download()
article12.parse()

title12= article12.title
year12= '2021'
source12= 'Yahoo'
text12 = article12.text


# In[14]:


url13 = 'https://finance.yahoo.com/news/china-still-a-2022-worry-morning-brief-100607233.html'

article13 = Article(url13)
article13.download()
article13.parse()

title13= article13.title
year13= '2021'
source13= 'Yahoo'
text13 = article13.text


# In[15]:


url14 = 'https://finance.yahoo.com/news/what-biden-left-undone-in-2021-195601863.html'

article14 = Article(url14)
article14.download()
article14.parse()

title14= article14.title
year14= '2021'
source14= 'Yahoo'
text14 = article14.text


# In[16]:


url15 = 'https://finance.yahoo.com/news/bitcoin-crypto-boosted-by-relief-rally-as-investors-shrug-off-hawkish-fed-pivot-154950029.html'

article15 = Article(url15)
article15.download()
article15.parse()

title15= article15.title
year15= '2021'
source15= 'Yahoo'
text15 = article15.text


# In[17]:


url16 = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-17-2021-231504646.html'

article16 = Article(url16)
article16.download()
article16.parse()

title16= article16.title
year16= '2021'
source16= 'Yahoo'
text16 = article16.text


# In[18]:


url17 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-five-times-more-likely-reinfect-than-delta-study-says-2021-12-17/'

article17 = Article(url17)
article17.download()
article17.parse()

title17= article17.title
year17= '2021'
source17= 'Reuters'
text17 = article17.text


# In[19]:


url18 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-rewrites-covid-plan-2022-2021-12-17/'

article18 = Article(url18)
article18.download()
article18.parse()

title18= article18.title
year18= '2021'
source18= 'Reuters'
text18 = article18.text


# In[20]:


url19 = 'https://www.reuters.com/world/china/sp-dumps-chinese-property-giant-evergrande-into-default-2021-12-17/'

article19 = Article(url19)
article19.download()
article19.parse()

title19= article19.title
year19= '2021'
source19= 'Reuters'
text19 = article19.text


# In[21]:


url20 = 'https://www.reuters.com/world/russia-unveils-security-guarantees-says-western-response-not-encouraging-2021-12-17/'

article20 = Article(url20)
article20.download()
article20.parse()

title20= article20.title
year20= '2021'
source20= 'Reuters'
text20 = article20.text


# In[22]:


url21 = 'https://www.reuters.com/markets/commodities/kentucky-rain-turns-more-tornado-survivors-out-their-homes-2021-12-17/'

article21 = Article(url21)
article21.download()
article21.parse()

title21= article21.title
year21= '2021'
source21= 'Reuters'
text21 = article21.text


# In[23]:


url22 = 'https://www.reuters.com/world/us/roger-stone-appears-before-jan-6-committee-refuses-testify-2021-12-17/'

article22 = Article(url22)
article22.download()
article22.parse()

title22= article22.title
year22= '2021'
source22= 'Reuters'
text22 = article22.text


# In[24]:


url23 = 'https://www.reuters.com/world/china/amazon-partnered-with-china-propaganda-arm-win-beijings-favor-document-shows-2021-12-17/'

article23 = Article(url23)
article23.download()
article23.parse()

title23= article23.title
year23= '2021'
source23= 'Reuters'
text23 = article23.text


# In[25]:


url24 = 'https://www.reuters.com/world/europe-gears-up-more-restrictions-omicron-infections-rise-2021-12-17/'

article24 = Article(url24)
article24.download()
article24.parse()

title24= article24.title
year24= '2021'
source24= 'Reuters'
text24 = article24.text


# In[26]:


url25 = 'https://www.reuters.com/world/europe/italys-salvini-says-draghi-should-remain-pm-not-be-next-president-2021-12-17/'

article25 = Article(url25)
article25.download()
article25.parse()

title25= article25.title
year25= '2021'
source25= 'Reuters'
text25 = article25.text


# In[27]:


url26 = 'https://www.reuters.com/markets/commodities/after-voter-slap-switzerland-tries-again-with-plan-slash-emissions-2021-12-17/'

article26 = Article(url26)
article26.download()
article26.parse()

title26= article26.title
year26= '2021'
source26= 'Reuters'
text26 = article26.text


# In[28]:


url27 = 'https://www.reuters.com/markets/europe/dollar-climbs-risk-off-moves-omicron-rate-hike-talk-spread-2021-12-17/'

article27 = Article(url27)
article27.download()
article27.parse()

title27= article27.title
year27= '2021'
source27= 'Reuters'
text27= article27.text


# In[29]:


url28 = 'https://www.reuters.com/markets/us/bond-markets-dont-buy-hawkish-feds-view-how-high-us-rates-can-go-2021-12-17/'

article28 = Article(url28)
article28.download()
article28.parse()

title28= article28.title
year28= '2021'
source28= 'Reuters'
text28 = article28.text


# In[30]:


url29 = 'https://www.reuters.com/markets/us/feds-hawkish-pivot-includes-historically-bullish-view-us-job-market-2021-12-17/'

article29 = Article(url29)
article29.download()
article29.parse()

title29= article29.title
year29= '2021'
source29= 'Reuters'
text29 = article29.text


# In[31]:


url30 = 'https://www.reuters.com/markets/europe/stocks-slide-safe-havens-gain-omicron-worries-weigh-2021-12-17/'

article30 = Article(url30)
article30.download()
article30.parse()

title30= article30.title
year30= '2021'
source30= 'Reuters'
text30 = article30.text


# In[32]:


url31 = 'https://www.reuters.com/business/retail-consumer/pg-recalls-some-conditioner-shampoo-sprays-due-potential-cancer-risk-2021-12-17/'

article31 = Article(url31)
article31.download()
article31.parse()

title31= article31.title
year31= '2021'
source31= 'Reuters'
text31 = article31.text


# In[33]:


url32 = 'https://www.reuters.com/business/jpmorgan-securities-pay-125-mln-settle-sec-charges-record-keeping-lapses-2021-12-17/'

article32 = Article(url32)
article32.download()
article32.parse()

title32= article32.title
year32= '2021'
source32= 'Reuters'
text32 = article32.text


# In[34]:


url33 = 'https://www.reuters.com/world/europe/paris-judge-approves-10-million-euro-settlement-with-lvmh-spy-case-2021-12-17/'

article33 = Article(url33)
article33.download()
article33.parse()

title33= article33.title
year33= '2021'
source33= 'Reuters'
text33 = article33.text


# In[35]:


url34 = 'https://www.reuters.com/business/sustainable-business/exclusive-california-probes-googles-treatment-black-female-workers-2021-12-17/'

article34 = Article(url34)
article34.download()
article34.parse()

title34= article34.title
year34= '2021'
source34= 'Reuters'
text34 = article34.text


# In[36]:


url35 = 'https://www.reuters.com/world/europe/swiss-prosecutors-review-credit-suisse-chairmans-quarantine-breach-2021-12-17/'

article35 = Article(url35)
article35.download()
article35.parse()

title35= article35.title
year35= '2021'
source35= 'Reuters'
text35 = article35.text


# In[37]:


url36 = 'https://www.reuters.com/markets/europe/batteries-included-northvolt-goes-all-out-meet-2021-launch-goal-2021-12-17/'

article36 = Article(url36)
article36.download()
article36.parse()

title36= article36.title
year36= '2021'
source36= 'Reuters'
text36 = article36.text


# In[38]:


url37 = 'https://www.reuters.com/markets/europe/russias-richest-woman-rules-out-parting-with-slice-wildberries-pie-2021-12-17/'

article37 = Article(url37)
article37.download()
article37.parse()

title37= article37.title
year37= '2021'
source37= 'Reuters'
text37 = article37.text


# In[39]:


url38 = 'https://www.reuters.com/business/autos-transportation/rivian-warns-supply-issues-hit-2021-production-shares-fall-10-2021-12-17/'

article38 = Article(url38)
article38.download()
article38.parse()

title38= article38.title
year38= '2021'
source38= 'Reuters'
text38 = article38.text


# In[40]:


url39 = 'https://www.reuters.com/technology/boeing-wants-build-its-next-airplane-metaverse-2021-12-17/'

article39 = Article(url39)
article39.download()
article39.parse()

title39= article39.title
year39= '2021'
source39= 'Reuters'
text39 = article39.text


# In[41]:


url40 = 'https://www.reuters.com/technology/ftc-chief-says-considering-rule-makings-consumer-privacy-2021-12-17/'

article40 = Article(url40)
article40.download()
article40.parse()

title40= article40.title
year40= '2021'
source40= 'Reuters'
text40 = article40.text


# In[42]:


url41 = 'https://www.reuters.com/article/us-global-markets-2019-graphic/the-best-year-financial-markets-have-ever-had-idUSKBN1YO266'

article41 = Article(url41)
article41.download()
article41.parse()

title41= article41.title
year41= '2019'
source41= 'Reuters'
text41 = article41.text


# In[43]:


url42 = 'https://www.reuters.com/article/rpb-globalwebindex2019/reuters-ranked-as-second-most-trusted-news-brand-in-globalwebindex-report-idUSKCN1U62E2'

article42 = Article(url42)
article42.download()
article42.parse()

title42= article42.title
year42= '2019'
source42= 'Reuters'
text42 = article42.text


# In[44]:


url43 = 'https://www.reuters.com/article/us-global-markets-analysis/the-best-first-half-for-financial-markets-ever-idUSKCN1TT1OR'

article43= Article(url43)
article43.download()
article43.parse()

title43= article43.title
year43= '2019'
source43= 'Reuters'
text43 = article43.text


# In[45]:


url44 = 'https://www.insider.com/success-insider-poshmark-college-bob-iger-ben-and-jerrys-2020-2'

article44 = Article(url44)
article44.download()
article44.parse()

title44= article44.title
year44= '2020'
source44= 'Business Insider'
text44 = article44.text


# In[46]:


url45 = 'https://www.insider.com/venture-capital-career-ultimate-guides-break-in-get-hired-succeed'

article45 = Article(url45)
article45.download()
article45.parse()

title45= article45.title
year45= '2020'
source45= 'Business Insider'
text45 = article45.text


# In[47]:


url46 = 'https://www.insider.com/presenting-how-to-market-your-startup-company-grow-successful-business'

article46 = Article(url46)
article46.download()
article46.parse()

title46= article46.title
year46= '2020'
source46= 'Business Insider'
text46 = article46.text


# In[48]:


url47 = 'https://www.insider.com/entrepreneurship-toolkit-apps-services-and-docs-to-start-a-business'

article47 = Article(url47)
article47.download()
article47.parse()

title47= article47.title
year47= '2020'
source47= 'Business Insider'
text47 = article47.text


# In[49]:


url48 = 'https://www.insider.com/heres-the-latest-wework-news-2019-6'

article48 = Article(url48)
article48.download()
article48.parse()

title48= article48.title
year48= '2020'
source48= 'Business Insider'
text48 = article48.text


# In[50]:


url49 = 'https://www.businessinsider.com/sc/how-masienda-founder-kept-masa-business-alive-after-pandemic-layoffs-2021-11?utm_source=studios_onsite&utm_medium=NPU&utm_campaign=Capital+One'

article49 = Article(url49)
article49.download()
article49.parse()

title49= article49.title
year49= '2020'
source49= 'Business Insider'
text49 = article49.text


# In[51]:


url50 = 'https://www.insider.com/success-insider-coffee-creamer-tech-sneakerheads-goldman-sachs-2020-2'

article50 = Article(url50)
article50.download()
article50.parse()

title50= article50.title
year50= '2020'
source50= 'Business Insider'
text50 = article50.text


# In[52]:


import pandas as pd


# In[58]:


title = [titleOne,titleTwo,titleThree,titleFour,titleFive,titleSix,titleSeven,titleEight,titleNine,titleTen,title11,title12,title13,title14,title15,title16,title17,title18,title19,title20,title21,title22,title23,title24,title25,title26,title27,title28,title29,title30,title31,title32,title33,title34,title35,title36,title37,title38,title39,title40,title41,title42,title43,title44,title45,title46,title47,title48,title49,title50]
year = [yearOne,yearTwo,yearThree,yearFour,yearFive,yearSix,yearSeven,yearEight,yearNine,yearTen,year11,year12,year13,year14,year15,year16,year17,year18,year19,year20,year21,year22,year23,year24,year25,year26,year27,year28,year29,year30,year31,year32,year33,year34,year35,year36,year37,year38,year39,year40,year41,year42,year43,year44,year45,year46,year47,year48,year49,year50]
source = [sourceOne,sourceTwo,sourceThree,sourceFour,sourceFive,sourceSix,sourceSeven,sourceEight,sourceNine,sourceTen,source11,source12,source13,source14,source15,source16,source17,source18,source19,source20,source21,source22,source23,source24,source25,source26,source27,source28,source29,source30,source31,source32,source33,source34,source35,source36,source37,source38,source39,source40,source41,source42,source43,source44,source45,source46,source47,source48,source49,source50]
url = [urlOne,urlTwo,urlThree,urlFour,urlFive,urlSix,urlSeven,urlEight,urlNine,urlTen,url11,url12,url13,url14,url15,url16,url17,url18,url19,url20,url21,url22,url23,url24,url25,url26,url27,url28,url29,url30,url31,url32,url33,url34,url35,url36,url37,url38,url39,url40,url41,url42,url43,url44,url45,url46,url47,url48,url49,url50]
text = [textOne,textTwo,textThree,textFour,textFive,textSix,textSeven,textEight,textNine,textTen,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,text24,text25,text26,text27,text28,text29,text30,text31,text32,text33,text34,text35,text36,text37,text38,text39,text40,text41,text42,text43,text44,text45,text46,text47,text48,text49,text50]


# In[60]:


df = pd.DataFrame({'Title': [ title[0], title[1], title[2], title[3], title[4], title[5], title[6], title[7], title[8], title[9],title[10],title[11],title[12],title[13],title[14],title[15],title[16],title[17],title[18],title[19],title[20],title[21],title[22],title[23],title[24],title[25],title[26],title[27],title[28],title[29],title[30],title[31],title[32],title[33],title[34],title[35],title[36],title[37],title[38],title[39],title[40],title[41],title[42],title[43],title[44],title[45],title[46],title[47],title[48],title[49] ],
                   'Year': [year[0], year[1], year[2], year[3], year[4], year[5], year[6], year[7], year[8], year[9],year[10],year[11],year[12],year[13],year[14],year[15],year[16],year[17],year[18],year[19],year[20],year[21],year[22],year[23],year[24],year[25],year[26],year[27],year[28],year[29],year[30],year[31],year[32],year[33],year[34],year[35],year[36],year[37],year[38],year[39],year[40],year[41],year[42],year[43],year[44],year[45],year[46],year[47],year[48],year[49] ],
                   'Source': [source[0], source[1], source[2], source[3], source[4], source[5], source[6], source[7], source[8], source[9],source[10],source[11],source[12],source[13],source[14],source[15],source[16],source[17],source[18],source[19],source[20],source[21],source[22],source[23],source[24],source[25],source[26],source[27],source[28],source[29],source[30],source[31],source[32],source[33],source[34],source[35],source[36],source[37],source[38],source[39],source[40],source[41],source[42],source[43],source[44],source[45],source[46],source[47],source[48],source[49]],
                   'URL': [url[0], url[1], url[2], url[3], url[4], url[5], url[6], url[7], url[8], url[9],url[10],url[11],url[12],url[13],url[14],url[15],url[16],url[17],url[18],url[19],url[20],url[21],url[22],url[23],url[24],url[25],url[26],url[27],url[28],url[29],url[30],url[31],url[32],url[33],url[34],url[35],url[36],url[37],url[38],url[39],url[40],url[41],url[42],url[43],url[44],url[45],url[46],url[47],url[48],url[49]],
                    'Body': [text[0], text[1], text[2], text[3], text[4], text[5], text[6], text[7],text[8], text[9],text[10],text[11],text[12],text[13],text[14],text[15],text[16],text[17],text[18],text[19],text[20],text[21],text[22],text[23],text[24],text[25],text[26],text[27],text[28],text[29],text[30],text[31],text[32],text[33],text[34],text[35],text[36],text[37],text[38],text[39],text[40],text[41],text[42],text[43],text[44],text[45],text[46],text[47],text[48],text[49]]})


# In[61]:


file_name = 'Articles.xlsx'
df.to_excel(file_name)


# In[ ]:




