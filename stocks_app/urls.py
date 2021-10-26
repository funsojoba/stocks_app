from django.contrib import admin
from django.urls import path

from .views import home, stock_tracker

urlpatterns = [
    path('', home),
    path('stocktracker', stock_tracker),
]
