from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
from .forms import CreateUserForm

def index(request):
    return render(request, 'elearning/index.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Felhasználó sikeresen létrehozva (' + user + ')')
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Hibás felhasználónév vagy jelszó!')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
