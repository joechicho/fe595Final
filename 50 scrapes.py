#!/usr/bin/env python
# coding: utf-8

# In[5]:


from newspaper import Article


# In[6]:


urlOne = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

articleOne = Article(urlOne)
articleOne.download()
articleOne.parse()

titleOne= articleOne.title
yearOne= '2021'
sourceOne= 'Yahoo'
textOne = articleOne.text


# In[7]:


urlTwo = 'https://finance.yahoo.com/news/december-2021-fomc-preview-federal-reserve-100713885.html'

articleTwo = Article(urlTwo)
articleTwo.download()
articleTwo.parse()

titleTwo= articleTwo.title
yearTwo= '2021'
sourceTwo= 'Yahoo'
textTwo = articleTwo.text


# In[8]:


urlThree = 'https://finance.yahoo.com/news/we-need-to-talk-about-2023-yes-already-morning-brief-101147700.html'

articleThree = Article(urlThree)
articleThree.download()
articleThree.parse()

titleThree= articleThree.title
yearThree= '2021'
sourceThree= 'Yahoo'
textThree = articleThree.text


# In[9]:


urlFour = 'https://finance.yahoo.com/news/hedge-funds-warm-up-to-crypto-as-institutional-involvement-expands-175512467.html'

articleFour = Article(urlFour)
articleFour.download()
articleFour.parse()

titleFour= articleFour.title
yearFour= '2021'
sourceFour= 'Yahoo'
textFour = articleFour.text


# In[10]:


urlFive = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-14-2021-232905142.html'

articleFive = Article(urlFive)
articleFive.download()
articleFive.parse()

titleFive= articleFive.title
yearFive= '2021'
sourceFive= 'Yahoo'
textFive = articleFive.text


# In[14]:


urlSix = 'https://www.apa.org/monitor/2021/01/top-journal-articles'

articleSix = Article(urlSix)
articleSix.download()
articleSix.parse()

titleSix= articleSix.title
yearSix= '2020'
sourceSix= 'American'
textSix = articleSix.text


# In[15]:


urlSeven = 'https://wrachelwrites.com/2020/04/20/unpopular-opinion-why-automating-your-savings-is-overrated/'

articleSeven = Article(urlSeven)
articleSeven.download()
articleSeven.parse()

titleSeven= articleSeven.title
yearSeven= '2020'
sourceSeven= 'Wrachel Writes'
textSeven = articleSeven.text


# In[16]:


urlEight = 'https://www.newsday.com/business/coronavirus/smart-shop-li-grocery-delivery-coronavirus-1.43709225'

articleEight = Article(urlEight)
articleEight.download()
articleEight.parse()

titleEight= articleEight.title
yearEight= '2020'
sourceEight= 'Newsday'
textEight = articleEight.text


# In[17]:


urlNine = 'https://www.juststartinvesting.com/when-to-max-out-401k/'

articleNine = Article(urlNine)
articleNine.download()
articleNine.parse()

titleNine= articleNine.title
yearNine= '2019'
sourceNine= 'Just Start Investing'
textNine = articleNine.text


# In[18]:


urlTen = 'https://www.campfirefinance.com/are-side-hustles-worth-it/'

articleTen = Article(urlTen)
articleTen.download()
articleTen.parse()

titleTen= articleTen.title
yearTen= '2019'
sourceTen= 'Camp Fire Finance'
textTen = articleTen.text


# In[19]:


url11 = 'https://finance.yahoo.com/news/this-week-in-bidenomics-build-back-later-182525299.html'

article11 = Article(url11)
article11.download()
article11.parse()

title11= article11.title
year11= '2021'
source11= 'Yahoo'
text11 = article11.text


# In[20]:


url12 = 'https://finance.yahoo.com/news/us-eyes-crypto-climate-among-potential-risks-to-financial-stability-175240868.html'

article12 = Article(url12)
article12.download()
article12.parse()

title12= article12.title
year12= '2021'
source12= 'Yahoo'
text12 = article12.text


# In[21]:


url13 = 'https://finance.yahoo.com/news/china-still-a-2022-worry-morning-brief-100607233.html'

article13 = Article(url13)
article13.download()
article13.parse()

title13= article13.title
year13= '2021'
source13= 'Yahoo'
text13 = article13.text


# In[22]:


url14 = 'https://finance.yahoo.com/news/what-biden-left-undone-in-2021-195601863.html'

article14 = Article(url14)
article14.download()
article14.parse()

title14= article14.title
year14= '2021'
source14= 'Yahoo'
text14 = article14.text


# In[23]:


url15 = 'https://finance.yahoo.com/news/bitcoin-crypto-boosted-by-relief-rally-as-investors-shrug-off-hawkish-fed-pivot-154950029.html'

article15 = Article(url15)
article15.download()
article15.parse()

title15= article15.title
year15= '2021'
source15= 'Yahoo'
text15 = article15.text


# In[24]:


url16 = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-17-2021-231504646.html'

article16 = Article(url16)
article16.download()
article16.parse()

title16= article16.title
year16= '2021'
source16= 'Yahoo'
text16 = article16.text


# In[25]:


url17 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-five-times-more-likely-reinfect-than-delta-study-says-2021-12-17/'

article17 = Article(url17)
article17.download()
article17.parse()

title17= article17.title
year17= '2021'
source17= 'Reuters'
text17 = article17.text


# In[26]:


url18 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-rewrites-covid-plan-2022-2021-12-17/'

article18 = Article(url18)
article18.download()
article18.parse()

title18= article18.title
year18= '2021'
source18= 'Reuters'
text18 = article18.text


# In[27]:


url19 = 'https://www.reuters.com/world/china/sp-dumps-chinese-property-giant-evergrande-into-default-2021-12-17/'

article19 = Article(url19)
article19.download()
article19.parse()

title19= article19.title
year19= '2021'
source19= 'Reuters'
text19 = article19.text


# In[28]:


url20 = 'https://www.reuters.com/world/russia-unveils-security-guarantees-says-western-response-not-encouraging-2021-12-17/'

article20 = Article(url20)
article20.download()
article20.parse()

title20= article20.title
year20= '2021'
source20= 'Reuters'
text20 = article20.text


# In[29]:


url21 = 'https://www.reuters.com/markets/commodities/kentucky-rain-turns-more-tornado-survivors-out-their-homes-2021-12-17/'

article21 = Article(url21)
article21.download()
article21.parse()

title21= article21.title
year21= '2021'
source21= 'Reuters'
text21 = article21.text


# In[30]:


url22 = 'https://www.reuters.com/world/us/roger-stone-appears-before-jan-6-committee-refuses-testify-2021-12-17/'

article22 = Article(url22)
article22.download()
article22.parse()

title22= article22.title
year22= '2021'
source22= 'Reuters'
text22 = article22.text


# In[31]:


url23 = 'https://www.reuters.com/world/china/amazon-partnered-with-china-propaganda-arm-win-beijings-favor-document-shows-2021-12-17/'

article23 = Article(url23)
article23.download()
article23.parse()

title23= article23.title
year23= '2021'
source23= 'Reuters'
text23 = article23.text


# In[32]:


url24 = 'https://www.reuters.com/world/europe-gears-up-more-restrictions-omicron-infections-rise-2021-12-17/'

article24 = Article(url24)
article24.download()
article24.parse()

title24= article24.title
year24= '2021'
source24= 'Reuters'
text24 = article24.text


# In[33]:


url25 = 'https://www.reuters.com/world/europe/italys-salvini-says-draghi-should-remain-pm-not-be-next-president-2021-12-17/'

article25 = Article(url25)
article25.download()
article25.parse()

title25= article25.title
year25= '2021'
source25= 'Reuters'
text25 = article25.text


# In[34]:


url26 = 'https://www.reuters.com/markets/commodities/after-voter-slap-switzerland-tries-again-with-plan-slash-emissions-2021-12-17/'

article26 = Article(url26)
article26.download()
article26.parse()

title26= article26.title
year26= '2021'
source26= 'Reuters'
text26 = article26.text


# In[35]:


url27 = 'https://www.reuters.com/markets/europe/dollar-climbs-risk-off-moves-omicron-rate-hike-talk-spread-2021-12-17/'

article27 = Article(url27)
article27.download()
article27.parse()

title27= article27.title
year27= '2021'
source27= 'Reuters'
text27= article27.text


# In[36]:


url28 = 'https://www.reuters.com/markets/us/bond-markets-dont-buy-hawkish-feds-view-how-high-us-rates-can-go-2021-12-17/'

article28 = Article(url28)
article28.download()
article28.parse()

title28= article28.title
year28= '2021'
source28= 'Reuters'
text28 = article28.text


# In[37]:


url29 = 'https://www.reuters.com/markets/us/feds-hawkish-pivot-includes-historically-bullish-view-us-job-market-2021-12-17/'

article29 = Article(url29)
article29.download()
article29.parse()

title29= article29.title
year29= '2021'
source29= 'Reuters'
text29 = article29.text


# In[38]:


url30 = 'https://www.reuters.com/markets/europe/stocks-slide-safe-havens-gain-omicron-worries-weigh-2021-12-17/'

article30 = Article(url30)
article30.download()
article30.parse()

title30= article30.title
year30= '2021'
source30= 'Reuters'
text30 = article30.text


# In[39]:


url31 = 'https://www.reuters.com/business/retail-consumer/pg-recalls-some-conditioner-shampoo-sprays-due-potential-cancer-risk-2021-12-17/'

article31 = Article(url31)
article31.download()
article31.parse()

title31= article31.title
year31= '2021'
source31= 'Reuters'
text31 = article31.text


# In[40]:


url32 = 'https://www.reuters.com/business/jpmorgan-securities-pay-125-mln-settle-sec-charges-record-keeping-lapses-2021-12-17/'

article32 = Article(url32)
article32.download()
article32.parse()

title32= article32.title
year32= '2021'
source32= 'Reuters'
text32 = article32.text


# In[41]:


url33 = 'https://www.reuters.com/world/europe/paris-judge-approves-10-million-euro-settlement-with-lvmh-spy-case-2021-12-17/'

article33 = Article(url33)
article33.download()
article33.parse()

title33= article33.title
year33= '2021'
source33= 'Reuters'
text33 = article33.text


# In[42]:


url34 = 'https://www.reuters.com/business/sustainable-business/exclusive-california-probes-googles-treatment-black-female-workers-2021-12-17/'

article34 = Article(url34)
article34.download()
article34.parse()

title34= article34.title
year34= '2021'
source34= 'Reuters'
text34 = article34.text


# In[43]:


url35 = 'https://www.reuters.com/world/europe/swiss-prosecutors-review-credit-suisse-chairmans-quarantine-breach-2021-12-17/'

article35 = Article(url35)
article35.download()
article35.parse()

title35= article35.title
year35= '2021'
source35= 'Reuters'
text35 = article35.text


# In[44]:


url36 = 'https://www.reuters.com/markets/europe/batteries-included-northvolt-goes-all-out-meet-2021-launch-goal-2021-12-17/'

article36 = Article(url36)
article36.download()
article36.parse()

title36= article36.title
year36= '2021'
source36= 'Reuters'
text36 = article36.text


# In[45]:


url37 = 'https://www.reuters.com/markets/europe/russias-richest-woman-rules-out-parting-with-slice-wildberries-pie-2021-12-17/'

article37 = Article(url37)
article37.download()
article37.parse()

title37= article37.title
year37= '2021'
source37= 'Reuters'
text37 = article37.text


# In[46]:


url38 = 'https://www.reuters.com/business/autos-transportation/rivian-warns-supply-issues-hit-2021-production-shares-fall-10-2021-12-17/'

article38 = Article(url38)
article38.download()
article38.parse()

title38= article38.title
year38= '2021'
source38= 'Reuters'
text38 = article38.text


# In[47]:


url39 = 'https://www.reuters.com/technology/boeing-wants-build-its-next-airplane-metaverse-2021-12-17/'

article39 = Article(url39)
article39.download()
article39.parse()

title39= article39.title
year39= '2021'
source39= 'Reuters'
text39 = article39.text


# In[48]:


url40 = 'https://www.reuters.com/technology/ftc-chief-says-considering-rule-makings-consumer-privacy-2021-12-17/'

article40 = Article(url40)
article40.download()
article40.parse()

title40= article40.title
year40= '2021'
source40= 'Reuters'
text40 = article40.text


# In[49]:


url41 = 'https://www.reuters.com/article/us-global-markets-2019-graphic/the-best-year-financial-markets-have-ever-had-idUSKBN1YO266'

article41 = Article(url41)
article41.download()
article41.parse()

title41= article41.title
year41= '2019'
source41= 'Reuters'
text41 = article41.text


# In[50]:


url42 = 'https://www.reuters.com/article/rpb-globalwebindex2019/reuters-ranked-as-second-most-trusted-news-brand-in-globalwebindex-report-idUSKCN1U62E2'

article42 = Article(url42)
article42.download()
article42.parse()

title42= article42.title
year42= '2019'
source42= 'Reuters'
text42 = article42.text


# In[51]:


url43 = 'https://www.reuters.com/article/us-global-markets-analysis/the-best-first-half-for-financial-markets-ever-idUSKCN1TT1OR'

article43= Article(url43)
article43.download()
article43.parse()

title43= article43.title
year43= '2019'
source43= 'Reuters'
text43 = article43.text


# In[52]:


url44 = 'https://www.insider.com/success-insider-poshmark-college-bob-iger-ben-and-jerrys-2020-2'

article44 = Article(url44)
article44.download()
article44.parse()

title44= article44.title
year44= '2020'
source44= 'Business Insider'
text44 = article44.text


# In[53]:


url45 = 'https://www.insider.com/venture-capital-career-ultimate-guides-break-in-get-hired-succeed'

article45 = Article(url45)
article45.download()
article45.parse()

title45= article45.title
year45= '2020'
source45= 'Business Insider'
text45 = article45.text


# In[54]:


url46 = 'https://www.insider.com/presenting-how-to-market-your-startup-company-grow-successful-business'

article46 = Article(url46)
article46.download()
article46.parse()

title46= article46.title
year46= '2020'
source46= 'Business Insider'
text46 = article46.text


# In[55]:


url47 = 'https://www.insider.com/entrepreneurship-toolkit-apps-services-and-docs-to-start-a-business'

article47 = Article(url47)
article47.download()
article47.parse()

title47= article47.title
year47= '2020'
source47= 'Business Insider'
text47 = article47.text


# In[56]:


url48 = 'https://www.insider.com/heres-the-latest-wework-news-2019-6'

article48 = Article(url48)
article48.download()
article48.parse()

title48= article48.title
year48= '2020'
source48= 'Business Insider'
text48 = article48.text


# In[57]:


url49 = 'https://www.businessinsider.com/sc/how-masienda-founder-kept-masa-business-alive-after-pandemic-layoffs-2021-11?utm_source=studios_onsite&utm_medium=NPU&utm_campaign=Capital+One'

article49 = Article(url49)
article49.download()
article49.parse()

title49= article49.title
year49= '2020'
source49= 'Business Insider'
text49 = article49.text


# In[58]:


url50 = 'https://www.insider.com/success-insider-coffee-creamer-tech-sneakerheads-goldman-sachs-2020-2'

article50 = Article(url50)
article50.download()
article50.parse()

title50= article50.title
year50= '2020'
source50= 'Business Insider'
text50 = article50.text


# In[ ]:




