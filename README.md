# fe595Final
scraping, querying, data lakes and more fun stuff!

In this project, we have built a financial article search engine. From the frontend, a user can use our website to search for a list of financial articles that fit their search criteria. For example, if a user inputs 'Omicron' in the Subject textbox from the Start Year of 2020 to the End Year of 2021 from the source Retuers, they will receive a list of urls of financial articles whose Titles and Text reference Omicron from the years 2020 and 2021 published on the Reuters site. 

To build this search engine we took the following steps:
1. We created a database to store our information using MySQL and connected it to our RDS which is hosted on an EC2 instance
2. We scraped data from 100 financial articles and outputted it into an Excel file as seen in the 100articles_scrape_intoTable.py and Articles.xlsx files
3. Using python, we connected and created our table and its columns as seen in the PythonToDBConnection.py file
4. Using the Excel file, we created a SQL Script workbook to more efficiently write out queries using an Excel formula (SQLScriptWorkbook.xlsx)
5. Using the SQL Script Workbook, we uploaded the articles' data into our SQL Workbench (InputArticleData.sql)
6. We created and connected the frontend to our cloud-hosted database by using flask and libraries like pymysql.

