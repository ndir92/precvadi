from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username ', 'style': 'width: 300px;', 'class': 'form-control'}))
   
   
    password   = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
   
    

    
    
    
class UserForm(UserCreationForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username ', 'style': 'width: 300px;', 'class': 'form-control'}))
   
    
    
    email= forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'email ', 'style': 'width: 300px;', 'class': 'form-control'}))
   
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
   
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    
   

    class Meta:
            model = User
            fields = ('username', 'email', 'password1', 'password2')