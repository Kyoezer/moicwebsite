from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('doat/', views.Doat, name='doat'),
    path('ditt/', views.Ditt, name='ditt'),
    path('doim/', views.Doim, name='doim'),
    path('rsta/', views.Rsta, name='rsta'),#url mapping with view
]
