from django.urls import path, include
from . import views

urlpatterns = [
    path('portfolio', views.list, name="portfolio"),
    path('', views.stock_info)
]
