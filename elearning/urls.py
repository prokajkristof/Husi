from django.urls import path
from django.conf.urls import include
from elearning import views
from elearning.views import ModView, CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, ProfileView, \
    InstructorView, StudentView, PasswordChangeView
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name ="logout"),
    path('profile_s/', ProfileView.as_view(), name="ProfileView"),
    path('instructors/', InstructorView.as_view(), name="InstructorView"),
    path('students/', StudentView.as_view(), name="StudentView"),
    path('admin/', admin.site.urls),
    path('course_list/', CourseListView.as_view(), name='course-list'),
    path('course_list/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('course_list/create/', CourseCreateView.as_view(), name='course-create'),
    path('course_list/<int:id>/delete/', views.delete, name='delete'),
    path('course_list/<pk>/update/', CourseUpdateView.as_view(), name='update'),
    path('mod_form/', ModView.as_view(), name="mod_form"),
    #path('password_mod_form/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_mod_form.html')),
    path('password_mod_form/', PasswordChangeView.as_view(template_name='accounts/password_mod_form.html')),
    path('password_success/', views.password_success, name="password_success"),
]
