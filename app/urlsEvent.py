from django.urls import path
from app import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.EventListView.as_view(), name='event'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='EventDetailView'),
]
