##### scraping SINGLE article

from newspaper import Article

url = 'https://finance.yahoo.com/news/3-reasons-why-the-stock-market-hates-the-omicron-variant-morning-brief-100956774.html'

#download/parse
article = Article(url)
article.download()
article.parse()

#print article text
print(article.text)

