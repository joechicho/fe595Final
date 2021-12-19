#!/usr/bin/env python
# coding: utf-8

# In[69]:


from newspaper import Article


# In[70]:


urlOne = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

articleOne = Article(urlOne)
articleOne.download()
articleOne.parse()

titleOne= articleOne.title
yearOne= '2021'
sourceOne= 'Yahoo'
textOne = articleOne.text


# In[71]:


urlTwo = 'https://finance.yahoo.com/news/december-2021-fomc-preview-federal-reserve-100713885.html'

articleTwo = Article(urlTwo)
articleTwo.download()
articleTwo.parse()

titleTwo= articleTwo.title
yearTwo= '2021'
sourceTwo= 'Yahoo'
textTwo = articleTwo.text


# In[72]:


urlThree = 'https://finance.yahoo.com/news/we-need-to-talk-about-2023-yes-already-morning-brief-101147700.html'

articleThree = Article(urlThree)
articleThree.download()
articleThree.parse()

titleThree= articleThree.title
yearThree= '2021'
sourceThree= 'Yahoo'
textThree = articleThree.text


# In[73]:


urlFour = 'https://finance.yahoo.com/news/hedge-funds-warm-up-to-crypto-as-institutional-involvement-expands-175512467.html'

articleFour = Article(urlFour)
articleFour.download()
articleFour.parse()

titleFour= articleFour.title
yearFour= '2021'
sourceFour= 'Yahoo'
textFour = articleFour.text


# In[74]:


urlFive = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-14-2021-232905142.html'

articleFive = Article(urlFive)
articleFive.download()
articleFive.parse()

titleFive= articleFive.title
yearFive= '2021'
sourceFive= 'Yahoo'
textFive = articleFive.text


# In[75]:


urlSix = 'https://www.apa.org/monitor/2021/01/top-journal-articles'

articleSix = Article(urlSix)
articleSix.download()
articleSix.parse()

titleSix= articleSix.title
yearSix= '2020'
sourceSix= 'American'
textSix = articleSix.text


# In[76]:


urlSeven = 'https://wrachelwrites.com/2020/04/20/unpopular-opinion-why-automating-your-savings-is-overrated/'

articleSeven = Article(urlSeven)
articleSeven.download()
articleSeven.parse()

titleSeven= articleSeven.title
yearSeven= '2020'
sourceSeven= 'Wrachel Writes'
textSeven = articleSeven.text


# In[77]:


urlEight = 'https://www.newsday.com/business/coronavirus/smart-shop-li-grocery-delivery-coronavirus-1.43709225'

articleEight = Article(urlEight)
articleEight.download()
articleEight.parse()

titleEight= articleEight.title
yearEight= '2020'
sourceEight= 'Newsday'
textEight = articleEight.text


# In[78]:


urlNine = 'https://www.juststartinvesting.com/when-to-max-out-401k/'

articleNine = Article(urlNine)
articleNine.download()
articleNine.parse()

titleNine= articleNine.title
yearNine= '2019'
sourceNine= 'Just Start Investing'
textNine = articleNine.text


# In[79]:


urlTen = 'https://www.campfirefinance.com/are-side-hustles-worth-it/'

articleTen = Article(urlTen)
articleTen.download()
articleTen.parse()

titleTen= articleTen.title
yearTen= '2019'
sourceTen= 'Camp Fire Finance'
textTen = articleTen.text


# In[80]:


url11 = 'https://finance.yahoo.com/news/this-week-in-bidenomics-build-back-later-182525299.html'

article11 = Article(url11)
article11.download()
article11.parse()

title11= article11.title
year11= '2021'
source11= 'Yahoo'
text11 = article11.text


# In[81]:


url12 = 'https://finance.yahoo.com/news/us-eyes-crypto-climate-among-potential-risks-to-financial-stability-175240868.html'

article12 = Article(url12)
article12.download()
article12.parse()

title12= article12.title
year12= '2021'
source12= 'Yahoo'
text12 = article12.text


# In[82]:


url13 = 'https://finance.yahoo.com/news/china-still-a-2022-worry-morning-brief-100607233.html'

article13 = Article(url13)
article13.download()
article13.parse()

title13= article13.title
year13= '2021'
source13= 'Yahoo'
text13 = article13.text


# In[83]:


url14 = 'https://finance.yahoo.com/news/what-biden-left-undone-in-2021-195601863.html'

article14 = Article(url14)
article14.download()
article14.parse()

title14= article14.title
year14= '2021'
source14= 'Yahoo'
text14 = article14.text


# In[84]:


url15 = 'https://finance.yahoo.com/news/bitcoin-crypto-boosted-by-relief-rally-as-investors-shrug-off-hawkish-fed-pivot-154950029.html'

article15 = Article(url15)
article15.download()
article15.parse()

title15= article15.title
year15= '2021'
source15= 'Yahoo'
text15 = article15.text


# In[85]:


url16 = 'https://finance.yahoo.com/news/stock-market-news-live-updates-december-17-2021-231504646.html'

article16 = Article(url16)
article16.download()
article16.parse()

title16= article16.title
year16= '2021'
source16= 'Yahoo'
text16 = article16.text


# In[86]:


url17 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-five-times-more-likely-reinfect-than-delta-study-says-2021-12-17/'

article17 = Article(url17)
article17.download()
article17.parse()

title17= article17.title
year17= '2021'
source17= 'Reuters'
text17 = article17.text


# In[87]:


url18 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/omicron-rewrites-covid-plan-2022-2021-12-17/'

article18 = Article(url18)
article18.download()
article18.parse()

title18= article18.title
year18= '2021'
source18= 'Reuters'
text18 = article18.text


# In[88]:


url19 = 'https://www.reuters.com/world/china/sp-dumps-chinese-property-giant-evergrande-into-default-2021-12-17/'

article19 = Article(url19)
article19.download()
article19.parse()

title19= article19.title
year19= '2021'
source19= 'Reuters'
text19 = article19.text


# In[89]:


url20 = 'https://www.reuters.com/world/russia-unveils-security-guarantees-says-western-response-not-encouraging-2021-12-17/'

article20 = Article(url20)
article20.download()
article20.parse()

title20= article20.title
year20= '2021'
source20= 'Reuters'
text20 = article20.text


# In[90]:


url21 = 'https://www.reuters.com/markets/commodities/kentucky-rain-turns-more-tornado-survivors-out-their-homes-2021-12-17/'

article21 = Article(url21)
article21.download()
article21.parse()

title21= article21.title
year21= '2021'
source21= 'Reuters'
text21 = article21.text


# In[91]:


url22 = 'https://www.reuters.com/world/us/roger-stone-appears-before-jan-6-committee-refuses-testify-2021-12-17/'

article22 = Article(url22)
article22.download()
article22.parse()

title22= article22.title
year22= '2021'
source22= 'Reuters'
text22 = article22.text


# In[92]:


url23 = 'https://www.reuters.com/world/china/amazon-partnered-with-china-propaganda-arm-win-beijings-favor-document-shows-2021-12-17/'

article23 = Article(url23)
article23.download()
article23.parse()

title23= article23.title
year23= '2021'
source23= 'Reuters'
text23 = article23.text


# In[93]:


url24 = 'https://www.reuters.com/world/europe-gears-up-more-restrictions-omicron-infections-rise-2021-12-17/'

article24 = Article(url24)
article24.download()
article24.parse()

title24= article24.title
year24= '2021'
source24= 'Reuters'
text24 = article24.text


# In[94]:


url25 = 'https://www.reuters.com/world/europe/italys-salvini-says-draghi-should-remain-pm-not-be-next-president-2021-12-17/'

article25 = Article(url25)
article25.download()
article25.parse()

title25= article25.title
year25= '2021'
source25= 'Reuters'
text25 = article25.text


# In[95]:


url26 = 'https://www.reuters.com/markets/commodities/after-voter-slap-switzerland-tries-again-with-plan-slash-emissions-2021-12-17/'

article26 = Article(url26)
article26.download()
article26.parse()

title26= article26.title
year26= '2021'
source26= 'Reuters'
text26 = article26.text


# In[96]:


url27 = 'https://www.reuters.com/markets/europe/dollar-climbs-risk-off-moves-omicron-rate-hike-talk-spread-2021-12-17/'

article27 = Article(url27)
article27.download()
article27.parse()

title27= article27.title
year27= '2021'
source27= 'Reuters'
text27= article27.text


# In[97]:


url28 = 'https://www.reuters.com/markets/us/bond-markets-dont-buy-hawkish-feds-view-how-high-us-rates-can-go-2021-12-17/'

article28 = Article(url28)
article28.download()
article28.parse()

title28= article28.title
year28= '2021'
source28= 'Reuters'
text28 = article28.text


# In[98]:


url29 = 'https://www.reuters.com/markets/us/feds-hawkish-pivot-includes-historically-bullish-view-us-job-market-2021-12-17/'

article29 = Article(url29)
article29.download()
article29.parse()

title29= article29.title
year29= '2021'
source29= 'Reuters'
text29 = article29.text


# In[99]:


url30 = 'https://www.reuters.com/markets/europe/stocks-slide-safe-havens-gain-omicron-worries-weigh-2021-12-17/'

article30 = Article(url30)
article30.download()
article30.parse()

title30= article30.title
year30= '2021'
source30= 'Reuters'
text30 = article30.text


# In[100]:


url31 = 'https://www.reuters.com/business/retail-consumer/pg-recalls-some-conditioner-shampoo-sprays-due-potential-cancer-risk-2021-12-17/'

article31 = Article(url31)
article31.download()
article31.parse()

title31= article31.title
year31= '2021'
source31= 'Reuters'
text31 = article31.text


# In[101]:


url32 = 'https://www.reuters.com/business/jpmorgan-securities-pay-125-mln-settle-sec-charges-record-keeping-lapses-2021-12-17/'

article32 = Article(url32)
article32.download()
article32.parse()

title32= article32.title
year32= '2021'
source32= 'Reuters'
text32 = article32.text


# In[102]:


url33 = 'https://www.reuters.com/world/europe/paris-judge-approves-10-million-euro-settlement-with-lvmh-spy-case-2021-12-17/'

article33 = Article(url33)
article33.download()
article33.parse()

title33= article33.title
year33= '2021'
source33= 'Reuters'
text33 = article33.text


# In[103]:


url34 = 'https://www.reuters.com/business/sustainable-business/exclusive-california-probes-googles-treatment-black-female-workers-2021-12-17/'

article34 = Article(url34)
article34.download()
article34.parse()

title34= article34.title
year34= '2021'
source34= 'Reuters'
text34 = article34.text


# In[104]:


url35 = 'https://www.reuters.com/world/europe/swiss-prosecutors-review-credit-suisse-chairmans-quarantine-breach-2021-12-17/'

article35 = Article(url35)
article35.download()
article35.parse()

title35= article35.title
year35= '2021'
source35= 'Reuters'
text35 = article35.text


# In[105]:


url36 = 'https://www.reuters.com/markets/europe/batteries-included-northvolt-goes-all-out-meet-2021-launch-goal-2021-12-17/'

article36 = Article(url36)
article36.download()
article36.parse()

title36= article36.title
year36= '2021'
source36= 'Reuters'
text36 = article36.text


# In[106]:


url37 = 'https://www.reuters.com/markets/europe/russias-richest-woman-rules-out-parting-with-slice-wildberries-pie-2021-12-17/'

article37 = Article(url37)
article37.download()
article37.parse()

title37= article37.title
year37= '2021'
source37= 'Reuters'
text37 = article37.text


# In[107]:


url38 = 'https://www.reuters.com/business/autos-transportation/rivian-warns-supply-issues-hit-2021-production-shares-fall-10-2021-12-17/'

article38 = Article(url38)
article38.download()
article38.parse()

title38= article38.title
year38= '2021'
source38= 'Reuters'
text38 = article38.text


# In[108]:


url39 = 'https://www.reuters.com/technology/boeing-wants-build-its-next-airplane-metaverse-2021-12-17/'

article39 = Article(url39)
article39.download()
article39.parse()

title39= article39.title
year39= '2021'
source39= 'Reuters'
text39 = article39.text


# In[109]:


url40 = 'https://www.reuters.com/technology/ftc-chief-says-considering-rule-makings-consumer-privacy-2021-12-17/'

article40 = Article(url40)
article40.download()
article40.parse()

title40= article40.title
year40= '2021'
source40= 'Reuters'
text40 = article40.text


# In[110]:


url41 = 'https://www.reuters.com/article/us-global-markets-2019-graphic/the-best-year-financial-markets-have-ever-had-idUSKBN1YO266'

article41 = Article(url41)
article41.download()
article41.parse()

title41= article41.title
year41= '2019'
source41= 'Reuters'
text41 = article41.text


# In[111]:


url42 = 'https://www.reuters.com/article/rpb-globalwebindex2019/reuters-ranked-as-second-most-trusted-news-brand-in-globalwebindex-report-idUSKCN1U62E2'

article42 = Article(url42)
article42.download()
article42.parse()

title42= article42.title
year42= '2019'
source42= 'Reuters'
text42 = article42.text


# In[112]:


url43 = 'https://www.reuters.com/article/us-global-markets-analysis/the-best-first-half-for-financial-markets-ever-idUSKCN1TT1OR'

article43= Article(url43)
article43.download()
article43.parse()

title43= article43.title
year43= '2019'
source43= 'Reuters'
text43 = article43.text


# In[113]:


url44 = 'https://www.insider.com/success-insider-poshmark-college-bob-iger-ben-and-jerrys-2020-2'

article44 = Article(url44)
article44.download()
article44.parse()

title44= article44.title
year44= '2020'
source44= 'Business Insider'
text44 = article44.text


# In[114]:


url45 = 'https://www.insider.com/venture-capital-career-ultimate-guides-break-in-get-hired-succeed'

article45 = Article(url45)
article45.download()
article45.parse()

title45= article45.title
year45= '2020'
source45= 'Business Insider'
text45 = article45.text


# In[115]:


url46 = 'https://www.insider.com/presenting-how-to-market-your-startup-company-grow-successful-business'

article46 = Article(url46)
article46.download()
article46.parse()

title46= article46.title
year46= '2020'
source46= 'Business Insider'
text46 = article46.text


# In[116]:


url47 = 'https://www.insider.com/entrepreneurship-toolkit-apps-services-and-docs-to-start-a-business'

article47 = Article(url47)
article47.download()
article47.parse()

title47= article47.title
year47= '2020'
source47= 'Business Insider'
text47 = article47.text


# In[117]:


url48 = 'https://www.insider.com/heres-the-latest-wework-news-2019-6'

article48 = Article(url48)
article48.download()
article48.parse()

title48= article48.title
year48= '2020'
source48= 'Business Insider'
text48 = article48.text


# In[118]:


url49 = 'https://www.businessinsider.com/sc/how-masienda-founder-kept-masa-business-alive-after-pandemic-layoffs-2021-11?utm_source=studios_onsite&utm_medium=NPU&utm_campaign=Capital+One'

article49 = Article(url49)
article49.download()
article49.parse()

title49= article49.title
year49= '2020'
source49= 'Business Insider'
text49 = article49.text


# In[119]:


url50 = 'https://www.insider.com/success-insider-coffee-creamer-tech-sneakerheads-goldman-sachs-2020-2'

article50 = Article(url50)
article50.download()
article50.parse()

title50= article50.title
year50= '2020'
source50= 'Business Insider'
text50 = article50.text


# In[120]:


url51 = 'https://finance.yahoo.com/news/meaningful-progress-in-supply-chain-woes-but-ships-cargo-still-linger-as-holidays-loom-133411889.html'

article51 = Article(url51)
article51.download()
article51.parse()

title51= article51.title
year51= '2021'
source51= 'Yahoo'
text51 = article51.text


# In[121]:


url52 = 'https://finance.yahoo.com/news/u-appeals-court-reinstates-covid-001742431.html'

article52 = Article(url52)
article52.download()
article52.parse()

title52= article52.title
year52= '2021'
source52= 'Reuters'
text52 = article52.text


# In[122]:


url53 = 'https://finance.yahoo.com/news/why-bruce-springsteens-500-m-signals-a-perfect-storm-brewing-in-music-141822437.html'

article53 = Article(url53)
article53.download()
article53.parse()

title53= article53.title
year53= '2021'
source53= 'Yahoo'
text53 = article53.text


# In[123]:


url54 = 'https://finance.yahoo.com/news/1-manchin-says-no-bidens-142306001.html'

article54 = Article(url54)
article54.download()
article54.parse()

title54= article54.title
year54= '2021'
source54= 'Reuters'
text54 = article54.text


# In[124]:


url55 = 'https://www.businessinsider.com/jpmorgan-sec-fine-employees-whatsapp-use-2021-12'

article55 = Article(url55)
article55.download()
article55.parse()

title55= article55.title
year55= '2021'
source55= 'Business Insider'
text55 = article55.text


# In[125]:


url56 = 'https://www.businessinsider.com/jpmorgan-fines-over-employees-use-whatsapp-texting-messaging-apps-2021-12'

article56 = Article(url56)
article56.download()
article56.parse()

title56= article56.title
year56= '2021'
source56= 'Business Insider'
text56 = article56.text


# In[126]:


url57 = 'https://www.businessinsider.com/most-us-consumers-use-tools-that-depend-on-open-banking-2021-12'

article57 = Article(url57)
article57.download()
article57.parse()

title57= article57.title
year57= '2021'
source57= 'Business Insider'
text57 = article57.text


# In[127]:


url58 = 'https://www.businessinsider.com/three-payments-startups-raise-funds-to-take-on-legacy-issuers-2021-12'

article58 = Article(url58)
article58.download()
article58.parse()

title58= article58.title
year58= '2021'
source58= 'Business Insider'
text58 = article58.text


# In[128]:


url59 = 'https://www.businessinsider.com/klarna-increases-its-threat-to-issuers-by-enabling-a2a-payments-2021-12'

article59 = Article(url59)
article59.download()
article59.parse()

title59= article59.title
year59= '2021'
source59= 'Business Insider'
text59 = article59.text


# In[129]:


url60 = 'https://www.businessinsider.com/what-does-a-financial-advisor-do'

article60 = Article(url60)
article60.download()
article60.parse()

title60= article60.title
year60= '2021'
source60= 'Business Insider'
text60 = article60.text


# In[130]:


url61 = 'https://www.businessinsider.com/amc-adam-aron-twitter-reddit-investors-meme-stock-2021-12'

article61 = Article(url61)
article61.download()
article61.parse()

title61= article61.title
year61= '2021'
source61= 'Business Insider'
text61 = article61.text


# In[131]:


url62 = 'https://www.businessinsider.com/square-cfo-amrita-ahuja-discusses-long-term-growth-strategy-2021-12'

article62 = Article(url62)
article62.download()
article62.parse()

title62= article62.title
year62= '2021'
source62= 'Business Insider'
text62 = article62.text


# In[132]:


url63 = 'https://www.businessinsider.com/why-maxwells-mortgage-solution-faces-stiff-competition-2021-12'

article63 = Article(url63)
article63.download()
article63.parse()

title63= article63.title
year63= '2021'
source63= 'Business Insider'
text63 = article63.text


# In[133]:


url64 = 'https://www.businessinsider.com/why-maxwells-mortgage-solution-faces-stiff-competition-2021-12'

article64 = Article(url64)
article64.download()
article64.parse()

title64= article64.title
year64= '2021'
source64= 'Business Insider'
text64 = article64.text


# In[134]:


url65 = 'https://www.businessinsider.com/equifax-b2b-payments-onboarding-tool-saves-time-and-effort-2021-12'

article65 = Article(url65)
article65.download()
article65.parse()

title65= article65.title
year65= '2021'
source65= 'Business Insider'
text65 = article65.text


# In[135]:


url66 = 'https://www.businessinsider.com/innovation-strategies-at-small-and-midsize-financial-institutions'

article66 = Article(url66)
article66.download()
article66.parse()

title66= article66.title
year66= '2021'
source66= 'Business Insider'
text66 = article66.text


# In[136]:


url67 = 'https://www.businessinsider.com/canada-mobile-banking-emerging-features-benchmark'

article67 = Article(url67)
article67.download()
article67.parse()

title67= article67.title
year67= '2021'
source67= 'Business Insider'
text67 = article67.text


# In[137]:


url68 = 'https://www.businessinsider.com/congress-most-popular-stocks-members-investing-2021-12'

article68 = Article(url68)
article68.download()
article68.parse()

title68= article68.title
year68= '2021'
source68= 'Business Insider'
text68 = article68.text


# In[138]:


url69 = 'https://www.businessinsider.com/lawmakers-investing-in-crypto-as-congress-weighs-regulations-2021-12'

article69 = Article(url69)
article69.download()
article69.parse()

title69= article69.title
year69= '2021'
source69= 'Business Insider'
text69 = article69.text


# In[139]:


url70 = 'https://www.businessinsider.com/new-york-state-covid-19-record-breaking-daily-cases-2021-12'

article70 = Article(url70)
article70.download()
article70.parse()

title70= article70.title
year70= '2021'
source70= 'Business Insider'
text70 = article70.text


# In[140]:


url71 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/netherlands-starts-painful-christmas-coronavirus-lockdown-2021-12-19/'

article71 = Article(url71)
article71.download()
article71.parse()

title71= article71.title
year71= '2021'
source71= 'Reuters'
text71 = article71.text


# In[142]:


url72 = 'https://www.reuters.com/lifestyle/sports/new-protocols-introduced-curb-spread-covid-19-2021-12-18/'

article72 = Article(url72)
article72.download()
article72.parse()

title72= article72.title
year72= '2021'
source72= 'Reuters'
text72 = article72.text


# In[143]:


url73 = 'https://www.reuters.com/markets/europe/russian-gas-exports-europe-via-yamal-up-after-saturday-drop-2021-12-19/'

article73 = Article(url73)
article73.download()
article73.parse()

title73= article73.title
year73= '2021'
source73= 'Reuters'
text73 = article73.text


# In[144]:


url74 = 'https://www.reuters.com/markets/commodities/more-than-21000-people-displaced-by-floods-malaysia-state-media-2021-12-19/'

article74 = Article(url74)
article74.download()
article74.parse()

title74= article74.title
year74= '2021'
source74= 'Reuters'
text74 = article74.text


# In[145]:


url75 = 'https://www.reuters.com/markets/rates-bonds/eu-commissioner-warns-uk-against-picking-brexit-hardliner-replace-frost-2021-12-19/'

article75 = Article(url75)
article75.download()
article75.parse()

title75= article75.title
year75= '2021'
source75= 'Reuters'
text75 = article75.text


# In[146]:


url76 = 'https://www.reuters.com/business/finance/russia-does-not-expect-be-cut-off-swift-system-vtb-ceo-says-2021-12-19/'

article76 = Article(url76)
article76.download()
article70.parse()

title76= article76.title
year76= '2021'
source76= 'Reuters'
text76 = article76.text


# In[147]:


url77 = 'https://www.reuters.com/world/threat-omicron-looms-over-christmas-holidays-europe-us-2021-12-19/'

article77 = Article(url77)
article77.download()
article77.parse()

title77= article77.title
year77= '2021'
source77= 'Reuters'
text77 = article77.text


# In[148]:


url78 = 'https://www.reuters.com/world/us/covid-omicron-variant-raging-through-world-traveling-increases-risk-fauci-2021-12-19/'

article78 = Article(url78)
article78.download()
article78.parse()

title78= article78.title
year78= '2021'
source78= 'Reuters'
text78 = article78.text


# In[149]:


url79 = 'https://www.reuters.com/world/us/sanders-says-there-should-be-vote-build-back-better-despite-manchin-rejection-2021-12-19/'

article79= Article(url79)
article79.download()
article79.parse()

title79= article79.title
year79= '2021'
source79= 'Reuters'
text79 = article79.text


# In[150]:


url80 = 'https://www.reuters.com/world/uk/uk-health-minister-doesnt-rule-out-new-covid-restrictions-before-christmas-2021-12-19/'

article80 = Article(url80)
article80.download()
article80.parse()

title80= article80.title
year80= '2021'
source80= 'Reuters'
text80 = article80.text


# In[151]:


url81 = 'https://www.reuters.com/world/europe/thousands-santas-stage-madrid-charity-run-volcano-hit-la-palma-2021-12-19/'

article81 = Article(url81)
article81.download()
article81.parse()

title81= article81.title
year81= '2021'
source81= 'Reuters'
text81 = article81.text


# In[152]:


url82 = 'https://www.reuters.com/world/china/four-people-killed-expressway-bridge-collapse-chinas-hubei-province-2021-12-19/'

article82 = Article(url82)
article82.download()
article82.parse()

title82= article82.title
year82= '2021'
source82= 'Reuters'
text82 = article82.text


# In[153]:


url83 = 'https://www.reuters.com/world/middle-east/erdogan-says-he-lowered-inflation-4-before-will-do-it-again-soon-2021-12-19/'

article83 = Article(url83)
article83.download()
article83.parse()

title83= article83.title
year83= '2021'
source83= 'Reuters'
text83 = article83.text


# In[154]:


url84 = 'https://www.reuters.com/world/europe/france-support-ski-resorts-hit-by-british-tourists-ban-2021-12-18/'

article84 = Article(url84)
article84.download()
article84.parse()

title84= article84.title
year84= '2021'
source84= 'Reuters'
text84 = article84.text


# In[155]:


url85 = 'https://www.reuters.com/world/europe/nato-will-not-let-russia-dictate-its-military-posture-germany-says-2021-12-19/'

article85 = Article(url85)
article85.download()
article85.parse()

title85= article85.title
year85= '2021'
source85= 'Reuters'
text85 = article85.text


# In[156]:


url86 = 'https://www.reuters.com/world/china/hong-kong-votes-overhauled-patriots-only-election-2021-12-19/'

article86 = Article(url86)
article86.download()
article86.parse()

title86= article86.title
year86= '2021'
source86= 'Reuters'
text86 = article86.text


# In[157]:


url87 = 'https://www.reuters.com/world/uk/uk-reports-further-12133-confirmed-omicron-cases-24-hours-2021-12-19/'

article87 = Article(url80)
article87.download()
article87.parse()

title87= article87.title
year87= '2021'
source87= 'Reuters'
text87 = article87.text


# In[158]:


url88 = 'https://www.reuters.com/world/americas/final-chile-presidential-polls-show-leftist-boric-edging-ahead-2021-12-18/'

article88 = Article(url88)
article88.download()
article88.parse()

title88= article88.title
year88= '2021'
source88= 'Reuters'
text88 = article88.text


# In[159]:


url89 = 'https://www.reuters.com/world/uk/uk-health-minister-javid-i-understand-frosts-reasons-quitting-2021-12-19/'

article89 = Article(url89)
article89.download()
article89.parse()

title89= article89.title
year89= '2021'
source89= 'Reuters'
text89 = article89.text


# In[160]:


url90 = 'https://www.reuters.com/world/islamic-states-meeting-agrees-set-up-trust-fund-afghanistan-2021-12-19/'

article90 = Article(url90)
article90.download()
article90.parse()

title90= article90.title
year90= '2021'
source90= 'Reuters'
text90 = article90.text


# In[161]:


url91 = 'https://www.reuters.com/world/uk/uk-brexit-supremo-frost-resigns-blow-johnson-mail-sunday-2021-12-18/'

article91 = Article(url91)
article91.download()
article91.parse()

title91= article91.title
year91= '2021'
source91= 'Reuters'
text91 = article91.text


# In[162]:


url92 = 'https://www.reuters.com/technology/facebook-pays-fines-russia-over-banned-content-2021-12-19/'

article92 = Article(url92)
article92.download()
article92.parse()

title92= article92.title
year92= '2021'
source92= 'Reuters'
text92 = article92.text


# In[163]:


url93 = 'https://www.reuters.com/technology/apple-shuts-stores-miami-ottawa-annapolis-after-rise-covid-19-cases-bloomberg-2021-12-15/'

article93 = Article(url93)
article93.download()
article93.parse()

title93= article93.title
year93= '2021'
source93= 'Reuters'
text93 = article93.text


# In[164]:


url94 = 'https://www.reuters.com/technology/russia-proposes-holding-collective-cybersecurity-talks-with-eu-tass-2021-12-16/'

article94 = Article(url94)
article94.download()
article94.parse()

title94= article94.title
year94= '2021'
source94= 'Reuters'
text94 = article94.text


# In[165]:


url95 = 'https://www.reuters.com/technology/boeing-wants-build-its-next-airplane-metaverse-2021-12-17/'

article95 = Article(url95)
article95.download()
article95.parse()

title95= article95.title
year95= '2021'
source95= 'Reuters'
text95 = article95.text


# In[166]:


url96 = 'https://www.reuters.com/technology/sensetime-plans-hong-kong-ipo-re-launch-monday-keeps-fundraising-target-sources-2021-12-16/'

article96 = Article(url96)
article96.download()
article96.parse()

title96= article96.title
year96= '2021'
source96= 'Reuters'
text96 = article96.text


# In[167]:


url97 = 'https://www.reuters.com/business/healthcare-pharmaceuticals/regenerons-antibody-therapy-shows-long-term-protection-against-covid-19-2021-11-08/'

article97 = Article(url97)
article97.download()
article97.parse()

title97= article97.title
year97= '2021'
source97= 'Reuters'
text97 = article97.text


# In[168]:


url98 = 'https://www.reuters.com/world/americas/canadas-td-bank-delays-office-return-over-omicron-fears-2021-12-17/'

article98 = Article(url98)
article98.download()
article98.parse()

title98= article98.title
year98= '2021'
source98= 'Reuters'
text98 = article98.text


# In[169]:


url99 = 'https://www.reuters.com/technology/intel-invest-7-bln-malaysia-build-new-plant-2021-12-16/'

article99 = Article(url99)
article99.download()
article99.parse()

title99= article99.title
year99= '20201'
source99= 'Reuters'
text99 = article99.text


# In[170]:


url100 = 'https://www.reuters.com/technology/motional-partners-with-uber-provide-autonomous-food-deliveries-california-2021-12-16/'

article100 = Article(url100)
article100.download()
article100.parse()

title100= article100.title
year100= '2021'
source100= 'Reuters'
text100 = article100.text


# In[171]:


import pandas as pd


# In[172]:


title = [titleOne,titleTwo,titleThree,titleFour,titleFive,titleSix,titleSeven,titleEight,titleNine,titleTen,title11,title12,title13,title14,title15,title16,title17,title18,title19,title20,title21,title22,title23,title24,title25,title26,title27,title28,title29,title30,title31,title32,title33,title34,title35,title36,title37,title38,title39,title40,title41,title42,title43,title44,title45,title46,title47,title48,title49,title50,title51,title52,title53,title54,title55,title56,title57,title58,title59,title60,title61,title62,title63,title64,title65,title66,title67,title68,title69,title70,title71,title72,title73,title74,title75,title76,title77,title78,title79,title80,title81,title82,title83,title84,title85,title86,title87,title88,title89,title90,title91,title92,title93,title94,title95,title96,title97,title98,title99,title100]
year = [yearOne,yearTwo,yearThree,yearFour,yearFive,yearSix,yearSeven,yearEight,yearNine,yearTen,year11,year12,year13,year14,year15,year16,year17,year18,year19,year20,year21,year22,year23,year24,year25,year26,year27,year28,year29,year30,year31,year32,year33,year34,year35,year36,year37,year38,year39,year40,year41,year42,year43,year44,year45,year46,year47,year48,year49,year50,year51,year52,year53,year54,year55,year56,year57,year58,year59,year60,year61,year62,year63,year64,year65,year66,year67,year68,year69,year70,year71,year72,year73,year74,year75,year76,year77,year78,year79,year80,year81,year82,year83,year84,year85,year86,year87,year88,year89,year90,year91,year92,year93,year94,year95,year96,year97,year98,year99,year100]
source = [sourceOne,sourceTwo,sourceThree,sourceFour,sourceFive,sourceSix,sourceSeven,sourceEight,sourceNine,sourceTen,source11,source12,source13,source14,source15,source16,source17,source18,source19,source20,source21,source22,source23,source24,source25,source26,source27,source28,source29,source30,source31,source32,source33,source34,source35,source36,source37,source38,source39,source40,source41,source42,source43,source44,source45,source46,source47,source48,source49,source50,source51,source52,source53,source54,source55,source56,source57,source58,source59,source60,source61,source62,source63,source64,source65,source66,source67,source68,source69,source70,source71,source72,source73,source74,source75,source76,source77,source78,source79,source80,source81,source82,source83,source84,source85,source86,source87,source88,source89,source90,source91,source92,source93,source94,source95,source96,source97,source98,source99,source100]
url = [urlOne,urlTwo,urlThree,urlFour,urlFive,urlSix,urlSeven,urlEight,urlNine,urlTen,url11,url12,url13,url14,url15,url16,url17,url18,url19,url20,url21,url22,url23,url24,url25,url26,url27,url28,url29,url30,url31,url32,url33,url34,url35,url36,url37,url38,url39,url40,url41,url42,url43,url44,url45,url46,url47,url48,url49,url50,url51,url52,url53,url54,url55,url56,url57,url58,url59,url60,url61,url62,url63,url64,url65,url66,url67,url68,url69,url70,url71,url72,url73,url74,url75,url76,url77,url78,url79,url80,url81,url82,url83,url84,url85,url86,url87,url88,url89,url90,url91,url92,url93,url94,url95,url96,url97,url98,url99,url100]
text = [textOne,textTwo,textThree,textFour,textFive,textSix,textSeven,textEight,textNine,textTen,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,text24,text25,text26,text27,text28,text29,text30,text31,text32,text33,text34,text35,text36,text37,text38,text39,text40,text41,text42,text43,text44,text45,text46,text47,text48,text49,text50,text51,text52,text53,text54,text55,text56,text57,text58,text59,text60,text61,text62,text63,text64,text65,text66,text67,text68,text69,text70,text71,text72,text73,text74,text75,text76,text77,text78,text79,text80,text81,text82,text83,text84,text85,text86,text87,text88,text89,text90,text91,text92,text93,text94,text95,text96,text97,text98,text99,text100]


# In[173]:


for i in title:
    print(title)


# In[174]:


for y in year:
    print(year)


# In[175]:


for s in source:
    print(source)


# In[176]:


for u in url:
    print(url)


# In[177]:


for t in text:
    print(text)


# In[178]:


d = pd.DataFrame({'Title':title, 'Year':year, 'Source':source, 'URL':url, 'Text':text})


# In[179]:


file_name = 'Articles.xlsx'
d.to_excel(file_name)


# In[ ]:




