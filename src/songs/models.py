from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
  artist = models.ForeignKey('artists.Artist',on_delete=models.CASCADE,)
  title = models.CharField(max_length=200)
  lyric = models.TextField(max_length=100)

  class Meta:
    db_table = "songs"

class SongComment(models.Model):
    song = models.ForeignKey('songs.Song', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  
    class Meta:
        db_table = "songs_comments"