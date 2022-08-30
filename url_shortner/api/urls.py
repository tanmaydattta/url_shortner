from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.makeshorturl, name="shorten"),
    path('clicked/', views.getclicks, name='clicks'),
    path('summary/', views.summary, name='summary'),
    path('<str:shorturl>', views.redirectUrl, name='redirect')
]