from bs4 import BeautifulSoup
import requests
import csv

page_link = 'https://news.ycombinator.com/newcomments'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
for i in range(0,1):
    # data=page_content.find_all('div',class_='comment')
    data=page_content.find_all('span',class_='storyon')
    comment=data[i].text.strip('| on: ')
    # link=data[i].get('href')
    # print(link)
    print(comment)
