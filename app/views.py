from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'index.html')


def founder(request):
    return render(request, 'pages/About-Us/founder.html')


def know(request):
    return render(request, 'pages/About-Us/knowsfc.html')


def objectives(request):
    return render(request, 'pages/About-Us/objectives.html')


def workingmodel(request):
    return render(request, 'pages/About-Us/workingmodel.html')


def blog(request):
    return render(request, 'pages/Blog/blog.html')


def contact(request):
    return render(request, 'pages/Contact-Us/contact.html')


def events(request):
    return render(request, 'pages/Events/events.html')


def join(request):
    return render(request, 'pages/Join-Us/joinus.html')


def news(request):
    return render(request, 'pages/news/news.html')

def gyan(request):
    return render(request,'pages/Projects/gyan.html')

def sampuran(request):
    return render(request, 'pages/Projects/Sampuran.html')


def vatavaran(request):
    return render(request, 'pages/Projects/vatavaran.html')



class BlogListView(ListView):
    model=BlogPost
    template_name='pages/Blog/blog_list.html'
    paginate_by=12

    def get_context_data(self, *args, **kwargs):
        try:
            return super(BlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page']='last'
            return super(BlogListView, self).get_context_data(*args, **kwargs)
    
    

class BlogDetailView(DetailView):
    model=BlogPost
    template_name='pages/Blog/blog_detail.html'
