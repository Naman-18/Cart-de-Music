from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.forms import Form
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,label='Email', widget = forms.EmailInput(attrs={'class':'form-control'}))

class Meta:
    model = User
    fields= ['username','email','password1','password2']
    
    