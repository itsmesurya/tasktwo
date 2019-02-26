from bs4 import BeautifulSoup
import requests
import csv

page_link = 'https://news.ycombinator.com/jobs'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
for i in range(0,5):
    data=page_content.find_all('span',class_='age')
    data1=page_content.find_all('a',class_='storylink')
    # comment=data[i].text.strip()
    comment=data1[i].text.strip()
    print(comment)
    link=data[i].text.strip()
    print(link)
