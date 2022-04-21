from django.urls import path
from django.conf.urls import include
from elearning import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name ="logout"),


]