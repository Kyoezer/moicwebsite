from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def Doat(request):
    doats = doat.objects.all()
    context = {'doats': doats}
    return render(request, 'doat.html', context)


def Ditt(request):
    ditts = ditt.objects.all()
    context = {'ditts': ditts}
    return render(request, 'ditt.html', context)


def Doim(request):
    doims = doim.objects.all()
    context = {'doims': doims}
    return render(request, 'doim.html', context)


def Rsta(request):
    rstas = rsta.objects.all()
    context = {'rstas': rstas}
    return render(request, 'rsta.html', context)
