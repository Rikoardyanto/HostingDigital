from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'DigitalEnt/index.html')

def about(request):
    return render(request, 'DigitalEnt/about.html')

def contact(request):
    return render(request, 'DigitalEnt/contact.html')

def news(request):
    return render(request, 'DigitalEnt/news.html')

def portfolio(request):
    return render(request, 'DigitalEnt/portfolio.html')

def service(request):
    return render(request, 'DigitalEnt/service.html')
