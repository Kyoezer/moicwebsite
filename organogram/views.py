from multiprocessing import context
from django.shortcuts import redirect, render
from .models import ministry_strength


# Create your views here.


def strength(request):
    strengths = ministry_strength.objects.all()
    context = {'strengths': strengths}
    return render(request, 'organogram.html', context)
