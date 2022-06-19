from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Profit/loss


class Stock(models.Model):
    bought = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    numberOfStocks = models.IntegerField()
    date = models.DateField()
    stockPrice = models.FloatField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Transaction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Watchlist(models.Model):
    stockName = models.CharField(max_length=50)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class Alert(models.Model):
    stockName = models.CharField(max_length=50)
    alertPrice = models.FloatField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)



