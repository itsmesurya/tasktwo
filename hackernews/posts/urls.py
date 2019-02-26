from django.conf.urls import url

from . import views

app_name='posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
    url(r"^ask/$", views.AskList.as_view(), name="allask"),
    url(r"^show/$", views.ShowList.as_view(), name="allshow"),
    url(r"^jobs/$", views.JobList.as_view(), name="jobs"),
    url(r"^vote/$",views.Voting.as_view(),name="vote"),
    url(r"new/$", views.CreatePost.as_view(), name="create"),
    url(r"^ask/$", views.AskPost.as_view(), name="ask"),
    url(r"comment/(?P<pk>\d+)/$",views.CommentPost.as_view(),name="comment"),
    # url(r"replycomment/(?P<pk>\d+)/$",views.ReplyComment.as_view(),name="reply"),
    # url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.ReplyComment.as_view,name="reply"),
    # url(r"ask/detail/(?P<pk>\d+)",views.DetailPost.as_view(),name="detail"),
    url(r"show/detail/(?P<pk>\d+)/",views.DetailPost.as_view(),name="detail"),
    url(r"Comments", views.CommentList.as_view(), name="all_comments"),

]
