from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Course
# Create your views here.


class CourseList(ListView):
   model = Course


def index(request):
    return render(request, 'elearning/index.html')
