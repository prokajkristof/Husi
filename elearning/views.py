from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
            messages.succes(request, 'Felhasználó sikeresen létrehozva (' + user + ')')
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
