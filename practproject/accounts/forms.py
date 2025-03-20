from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    given_name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=6)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(label='Password1',
                               widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password2',
        widget=forms.PasswordInput)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists(): 
            raise forms.ValidationError('This username is not available')
        return username
    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match')
        return password
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('This email is already registered')
        return email

class LoginForm(forms.Form):
  
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'user-assword'
        }
    ))
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError('This is an invalid username')







 