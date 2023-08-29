from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class': "form-control form-control-lg"}),
            'email' : forms.EmailInput(attrs={'class': "form-control form-control-lg"}),
            'first_name' : forms.TextInput(attrs={'class': "form-control form-control-lg"}),
            'last_name' : forms.TextInput(attrs={'class': "form-control form-control-lg"}),
            }



form = MyUserCreationForm()