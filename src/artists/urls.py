from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='artists_index'),
    path('<int:id>', views.artist, name='artist'),
] 