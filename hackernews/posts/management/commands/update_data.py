from django.core.management.base import BaseCommand
from posts.models import Post,Comment,Job
from bs4 import BeautifulSoup
import requests

def update_post():
    page_link = 'https://news.ycombinator.com/news'
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    data1=page_content.find_all('a',attrs={'class':'storylink'})
    for i in data1[0:10]:
        title1=i.text.strip()
        url1=i.get('href')
        post_object = Post.objects.get_or_create(title = title1, url=url1)

def update_comment():
    page_link = 'https://news.ycombinator.com/newcomments'
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    # data2=page_content.find_all('span',class_='storyon')
    data=page_content.find_all('div',class_='comment')
    # for i in data2[0:10]:
    for j in data[0:10]:
        # commenttil=j.text.strip('| on: ')
        comment1=j.text.strip()
        comment_object = Comment.objects.get_or_create(comment=comment1)

def update_job():
    page_link = 'https://news.ycombinator.com/jobs'
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    data=page_content.find_all('a',class_='storylink')
    for k in data[0:30]:
        comment=k.text.strip()
        link=k.get('href')
        job_object = Job.objects.get_or_create(J_title = comment, J_url=link)

class Command(BaseCommand):
    def handle(self,**options):
        # update_post()
        # update_comment()
        update_job()
