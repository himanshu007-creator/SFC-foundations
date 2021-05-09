from django.shortcuts import render
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


