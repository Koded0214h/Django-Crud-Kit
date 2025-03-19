from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm, LoginForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}')
            return redirect('home')
        else:
            messages.error(request, f'{form.errors}')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'registerform':form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Wlecome back, {user.username}')
                return redirect('home')
            else:
                messages.error(request, 'Empty user!')
        else:
            messages.error(request, f'{form.errors}')
    else:
        form = LoginForm()
        
    return render(request, 'users/login.html', {'loginform':form})

def user_logout(request):
    logout(request)
    return redirect('index')    


@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})