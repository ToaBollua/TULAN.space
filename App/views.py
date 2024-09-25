from django.shortcuts import render

def index(request):
    return render(request, 'App/index.html')

def gallery(request):
    return render(request, 'App/gallery.html')