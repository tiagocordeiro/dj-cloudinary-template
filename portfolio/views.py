from django.shortcuts import render
from .models import Trabalho


def portfolio(request):
    trabalhos = Trabalho.objects.all()
    return render(request, 'portfolio.html', {'trabalhos': trabalhos})
