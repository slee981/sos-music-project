from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='songs_index'),
    path('<int:id>', views.song, name='song'),
    path('search', views.songs_search, name='songs_search'),
    path('songs_create_comment', views.songs_create_comment, name='songs_create_comment'),
    path('get_topics', views.get_topics, name='get_topics'),
    path('save_song_topics', views.save_song_topics, name='save_song_topics')
]   