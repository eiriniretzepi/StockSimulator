from django.shortcuts import render
from .models import Portfolio, Stock, Transaction, Watchlist, Alert


def list(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolio': portfolio})


def stock_info(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']

        # sk_bf8836850ac8416a927deaeab73b3f0b
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=sk_bf8836850ac8416a927deaeab73b3f0b")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'stock_info.html', {'ticker': "Enter a Ticker Symbol Above "})