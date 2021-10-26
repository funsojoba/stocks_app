from django.shortcuts import render


def home(request):
    return render(request, 'stocks_app/index.html')

def stock_tracker(request):
    return render(request, 'stocks_app/stocktracker.html')