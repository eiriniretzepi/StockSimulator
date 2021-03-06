from django.urls import path, include
from . import views

urlpatterns = [
    path('portfolio', views.list, name="portfolio"),
    path('stockInfo', views.stock_info, name="stockInfo"),
    path('buySell', views.buy_sell, name="buySell"),
]
