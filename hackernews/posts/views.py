from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy,reverse
from django.http import Http404
from django.views import generic
from django.views.generic import UpdateView,DetailView
from braces.views import SelectRelatedMixin
from . import models
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
User = get_user_model()
from posts.models import Post, Comment,Ask,Job,Vote
from accounts.models import User
import csv

class PostList(generic.ListView):
    model = models.Post

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        context['post_list'] = posts
        for post in context['post_list']:
            total_comment = Comment.objects.filter(post_id = post).count()
            post.total_comment = total_comment
        comments=Comment.objects.filter()
        context["comments"] = comments
        return context
    # page_link = 'https://news.ycombinator.com/news'
    # page_response = requests.get(page_link, timeout=5)
    # page_content = BeautifulSoup(page_response.content, "html.parser")
    # for i in range(0,5):
    #     data=page_content.find_all('a',attrs={'class':'storylink'})
    #     name=data[i].text.strip()
    #     print(name)

class Voting(generic.DetailView):
    model = models.Vote





class JobList(generic.ListView):
    model =models.Job
    context_object_name = 'Jobs'
    template_name ="posts/job_list.html"

class DetailPost(generic.DetailView):
    fields=['comment']
    model = models.Post
    template_name = "posts/ask_detail.html"



    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        post=Post.objects.get(id = self.kwargs['pk'])
        context["post_title"] = post.title
        comments=Comment.objects.filter(post_id = self.kwargs['pk'])
        context["comments"] = comments
        for comment in comments:
            print(comment.user_id)
        return context

class CommentList(generic.ListView):
    fields=['comment']
    model =models.Comment
    template_name="posts/comment_list.html"


    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        comments=Comment.objects.filter()
        context["comments"] = comments
        return context


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('title','url','text')
    model = models.Post
    success_url = "/posts"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AskPost(LoginRequiredMixin,generic.CreateView,generic.ListView):
    fields = ('Q_title','Q_text')
    model = models.Ask
    template_name = "posts/ask_form.html"
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        questions=Ask.objects.filter()
        context["questions"] = questions
        return context

class AskList(generic.ListView):
    model = models.Post
    template_name = "posts/_ask.html"

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        context['post_list'] = posts
        for post in context['post_list']:
            total_comment = Comment.objects.filter(post_id = post).count()
            post.total_comment = total_comment
        comments=Comment.objects.filter()
        context["comments"] = comments
        return context

class ShowList(generic.ListView):
    model = models.Post
    template_name = 'posts/_ask.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        context['post_list'] = posts
        for post in context['post_list']:
            total_comment = Comment.objects.filter(post_id = post).count()
            post.total_comment = total_comment
        comments=Comment.objects.filter()
        context["comments"] = comments
        return context

class CommentPost(LoginRequiredMixin,generic.CreateView):
    fields=['comment']
    model =models.Comment
    template_name= "posts/post_comment.html"
    success_url = "Comments"


    def __str__(self):
        return self.comment


    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.post_id =Post.objects.get(id= self.kwargs['pk'])
        self.object.user = self.request.user
        if self.request.GET.get('comment_id'):
            self.object.parenta_id = self.request.GET.get('comment_id')
        print(self.request.user)
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        post=Post.objects.get(id = self.kwargs['pk'])
        context["post_title"] = post.title
        comments=Comment.objects.filter(post_id = self.kwargs['pk'],parenta_id=0)
        context["comments"] = comments
        for comment in comments:
            child_comment = Comment.objects.filter(parenta_id=comment.id)
            commentsobj = {}
            commentsobj = comment
            if child_comment:
                print(child_comment[0].comment)

                # commentsobj["child"] = child_comment
        return context

# class ReplyComment(LoginRequiredMixin,generic.CreateView):
#     fields=['comment']
#     model=models.Comment
#     template_name ="posts/comwwment_reply.html"
#
#     def __str__(self):
#         return self.comment
#
#     def get_context_data(self,*args,**kwargs):
#         context = super().get_context_data(**kwargs)
#         post=Post.objects.get(id = self.kwargs['pk'])
#         context["post_title"] = post.title
#         comments=Comment.objects.filter(post_id = self.kwargs['pk'])
#         context["comments"] = comments
#         for comment in comments:
#             print(comment.user_id)
#         return context
#

# class UserPosts(generic.ListView):
#     model = models.Post
#     template_name = "posts/user_post_list.html"
#
#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related("posts").get(
#                 title__iexact=self.kwargs.get("title")
#             )
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.posts.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_user"] = self.post_user
#         return context
