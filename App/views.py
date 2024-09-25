from django.shortcuts import render

def index(request):
    return render(request, 'App/index.html')

def gallery(request):
    return render(request, 'App/gallery.html')

def trade_hubs_view(request):
    return render(request, 'App/trade_hubs.html')

def game_stories(request):
    return render(request, 'App/game_stories.html')

def frequent_systems(request):
    return render(request, 'App/frequent_systems.html')