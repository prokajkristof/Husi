
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Course, Instructor, Student
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect


from django.urls import reverse
# Create your views here.
from .forms import CreateUserForm


@login_required(login_url='login')
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
    if request.user.is_authenticated:
        return redirect('index')
    else:
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


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get(self, *args, **kwargs):

        return render(self.request, 'accounts/profile.html')
