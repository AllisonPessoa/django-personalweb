from django.shortcuts import render
from .models import Article, Banner, Oraltalks
from .models import Data_analysis, Software, Instrument

# Create your views here.
def home(request):
    return render(request, 'home.html')

### PUBLICATIONS
def full_papers(request):
    articles = Article.objects.all().order_by('-year')
    context = {'articles': articles}
    return render(request, 'pub-full.html', context)

def banners(request):
    banners = Banner.objects.all().order_by('-year')
    context = {'banners': banners}
    return render(request, 'pub-banners.html', context)

def oral_talks(request):
    orals = Oraltalks.objects.all().order_by('-year')
    context = {'orals': orals}
    return render(request, 'pub-oral.html', context)

### PORTFOLIO
def portfolio(request):
    data = Data_analysis.objects.all().order_by('-year')
    software = Software.objects.all().order_by('-year')
    instruments = Instrument.objects.all().order_by('-year')

    context = {'data_analysis': data,
               'softwares': software,
               'instruments': instruments}
    
    return render(request, 'portfolio.html', context)

### CV
def cv(request):
    return render(request, 'cv.html')
