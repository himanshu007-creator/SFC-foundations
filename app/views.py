from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def knowsfc(request):
    return render(request, 'pages/About-Us/knowsfc.html')

def objectives(request):
    return render(request, 'pages/About-Us/objectives.html')

def workingmodel(request):
    return render(request, 'pages/About-Us/workingmodel.html')

def joinus(request):
    return render(request, 'pages/Join-Us/joinus.html')

def gyan(request):
    return render(request, 'pages/Projects/gyan.html')

def sampuran(request):
    return render(request, 'pages/Projects/Sampuran.html')

def vatavaran(request):
    return render(request, 'pages/Projects/vatavaran.html')