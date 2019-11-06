from django.db import models

# Create your models here.
class Song(models.Model):
  artist = models.ForeignKey('artists.Artist',on_delete=models.CASCADE,)
  title = models.CharField(max_length=200)
  lyric = models.TextField(max_length=100)

  class Meta:
    db_table = "songs"