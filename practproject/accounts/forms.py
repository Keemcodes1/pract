from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
  
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    given_name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=6)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)






 