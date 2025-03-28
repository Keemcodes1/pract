from django.contrib.auth import authenticate,login,logout,get_user_model
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm

# Create your views here.

User = get_user_model()
def register_view(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')
        try:
            user = User.objects.create(username,email,password)
       
        except:
            user = None
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            request.session['register_error'] = 1

    context = {form:'form'}

    return render(request, 'forms.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            attempt = request.session.get('attempt') or 0
            request.session['attempt'] = attempt + 1
            return redirect('/invalid-password')
        # return redirect('/login-success')
    context = {form:'form'}

    return render(request, 'forms.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')
    
