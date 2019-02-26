from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.encoding import python_2_unicode_compatible

from django.conf import settings
from django.urls import reverse
from django.db import models
import misaka
import datetime
import dateutil.parser
from django.utils import timezone
from django.contrib.auth import get_user_model

from accounts.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    score = models.PositiveIntegerField(default=0)
    published_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.text = misaka.html(self.text)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
        "posts:all",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-published_time"]
        # unique_together = ["url","title"]

class Vote(models.Model):
    user  = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=0)

class Comment(models.Model):
    comment = models.TextField()
    post_id = models.ForeignKey(Post,related_name="posts",on_delete=models.CASCADE)
    published_time = models.DateTimeField(auto_now=True)
    parenta_id = models.PositiveIntegerField(default=0)
    user  = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    # comment_title = models.CharField(max_length=100,default=Post.title)

    class Meta:
        ordering = ["-published_time"]

class Ask(models.Model):
    Q_title = models.CharField(max_length=100)
    Q_text = models.TextField(max_length=100)
    Q_published_time = models.DateTimeField(auto_now=True)

class Job(models.Model):
    J_title = models.CharField(max_length=100)
    J_url = models.CharField(max_length=100)
    published_time =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_time"]
