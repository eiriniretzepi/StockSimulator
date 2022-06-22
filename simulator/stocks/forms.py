from django import forms
from .models import Portfolio, Stock, Transaction, Watchlist, Alert


class PortolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["cash"]


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["bought", "name", "numberOfStocks", "date", "stockPrice", "portfolio"]



