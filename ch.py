from bs4 import BeautifulSoup
import requests
import csv

page_link = 'https://news.ycombinator.com/newcomments'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
# f=csv.writer(open('req.csv','w'))
# f.writerow(['title','link','comment'])
for i in range(0,1):
    data=page_content.find_all('span',attrs={'class':'commtext'})
    # title=data[i].text.strip()
    # print(title)
    comment=data[i].text.strip()
    # link=data[i].get('href')
    # print(link)
    print(comment)
    # f.writerow([title , link, comment])
