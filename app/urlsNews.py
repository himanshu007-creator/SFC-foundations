from django.urls import path
from app import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.NewsListView.as_view(),name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='NewsDetailView'),
]
