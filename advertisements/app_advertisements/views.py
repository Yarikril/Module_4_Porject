from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(request):
    adverisements = Advertisement.objects.all()
    context = {'adverisements' : adverisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')