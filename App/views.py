from django.shortcuts import render
from .models import TradeHub

def index(request):
    """Renders the index page."""
    return render(request, 'App/index.html')

def gallery(request):
    """Renders the gallery page."""
    return render(request, 'App/gallery.html')

def trade_hubs_view(request):
    trade_hubs = TradeHub.objects.all()
    return render(request, 'App/trade_hubs.html', {'trade_hubs': trade_hubs})