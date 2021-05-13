from django.urls import path
from app import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',views.NewsListView.as_view(),name='news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='NewsDetailView'),
]
