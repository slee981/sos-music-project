from django.urls import path

from . import views

urlpatterns = [
    path('login_1', views.login_1, name='login_1'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('my_profile', views.my_profile, name='my_profile'),
]  