from django.urls import path

from .import views

urlpatterns= [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('news.html', views.contact, name='news'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('service.html', views.service, name='service'),
]