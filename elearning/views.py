from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Course
# Create your views here.


class CourseListView(ListView):
    template_name = 'course_list.html'
    queryset = Course.objects.all()


class CourseDetailView(DetailView):
    #template_name = 'course_detail.html'
    queryset = Course.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Course, id=id_)


def index(request):
    return render(request, 'elearning/index.html')
