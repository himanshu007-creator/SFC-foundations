"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app import views
urlpatterns = [
    #general
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('blog/', views.blog, name="blog"),
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('contact/', views.contact, name="contact"),
    path('events/', views.events, name='event'),
    path('joinus/', views.join, name='join'),
    path('news/', views.news, name='news'),

    #projects
    path('sampuran/', views.sampuran, name="sampuran"),
    path('gyan/', views.gyan, name="gyan"),
    path('vatavaran/', views.vatavaran, name='vatavaran'),

    #about
    path('founder/', views.founder, name='founder'),
    path('know/', views.know, name='know'),
    path('objectives/', views.objectives, name='objectives'),
    path('workingmodel/', views.workingmodel, name='workingmodel'),
]
