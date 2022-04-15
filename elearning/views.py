from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
# Create your views here.


from django.views.generic.edit import CreateView


class CourseUpdateView(UpdateView):
    template_name_suffix = '_update_form'
    model = Course
    fields = [
        'course_title',
        'course_brief',
        'instructor_id',
        'num_of_chapters'
    ]


def delete(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  return HttpResponseRedirect(reverse('course-list'))


class CourseCreateView(CreateView):
    model = Course
    fields = [
        'course_title',
        'course_brief',
        'instructor_id',
        'num_of_chapters'
    ]


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
