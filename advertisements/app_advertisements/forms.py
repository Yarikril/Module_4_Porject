from django import forms
from .models import Advertisement
from django.core import validators
from django.db import models
from django.forms import ModelForm

class AdvertisementFrom(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            "title" : forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'description' : forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control  form-control-lg'}), 
            'auction' : forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
            'image' : forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

form = AdvertisementFrom()