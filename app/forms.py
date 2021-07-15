from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.forms import Form
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,label='Email', widget = forms.EmailInput(attrs={'class':'form-control'}))

class Meta:
    model = User
    fields= ['username','email','password1','password2']
    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip= False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
   old_password = forms.CharField(label=_("Old Password"),strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
   new_password1 = forms.CharField(label=_("New Password"),strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
   new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})) 

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length = 254, widget = forms.EmailInput(attrs={'autocomplet':'email', 'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
   new_password1 = forms.CharField(label=_("New Password"),strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
   new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False, widget = forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))  