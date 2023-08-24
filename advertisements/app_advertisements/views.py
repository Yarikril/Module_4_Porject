from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementFrom

def index(request):
    adverisements = Advertisement.objects.all()
    context = {'adverisements' : adverisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementFrom(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
            
    else:
        form = AdvertisementFrom()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)