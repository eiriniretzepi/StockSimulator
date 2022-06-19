from django.shortcuts import render
from .models import Portfolio, Stock, Transaction, Watchlist, Alert


def list(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolio': portfolio})
