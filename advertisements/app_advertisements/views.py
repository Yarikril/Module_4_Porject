from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementFrom
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    adverisements = Advertisement.objects.all()
    context = {'adverisements' : adverisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_advertisements/advertisement-post.html', context)