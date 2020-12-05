from django.urls import path ,include
from resume import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('themes/',views.themes,name='themes'),
    path('blankformat/',views.blankformat,name='blankformat'),
    path('tableformat/',views.tableformat,name='tableformat'),
   	path('signup/',views.signup,name='signup'),
   	path('signin/',auth_views.LoginView.as_view(template_name="resume/signin.html"),name='signin'),
   	path('signout/',auth_views.LogoutView.as_view(template_name="resume/signout.html"),name='signout')
]