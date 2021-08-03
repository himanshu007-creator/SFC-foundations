from django.urls import path
from app import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.BlogListView.as_view(),name='blog'),
    path('<int:pk>/',views.BlogDetailView,name='BlogDetailView'),
    path('blog_donate',views.BlogDonate,name='BlogDonate'),
    path('blog_slider',views.BlogSlider,name='BlogSlider'),
]
