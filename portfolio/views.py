from django.shortcuts import render
from .models import Trabalho


def portfolio(request):
    trabalhos = Trabalho.objects.all()
    return render(request, 'portfolio.html', {'trabalhos': trabalhos})

def portfolio_detail(request, pk):
    trabalho = Trabalho.objects.get(pk=pk)
    return render(request, 'portfolio-detail.html', {'trabalho': trabalho})
