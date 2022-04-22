from django.urls import path
from django.conf.urls import include
from elearning import views
from elearning.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name ="logout"),


    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('course_list/', CourseListView.as_view(), name='course-list'),
    path('course_list/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('course_list/create/', CourseCreateView.as_view(), name='course-create'),
    path('course_list/<int:id>/delete/', views.delete, name='delete'),
    path('course_list/<pk>/update/', CourseUpdateView.as_view(), name='update'),

]
