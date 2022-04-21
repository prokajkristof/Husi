from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'elearning/index.html')

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)
