from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    description = models.CharField(max_length=25)

    class Meta:
        db_table = "topics"

class SongTopic(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    song = models.ForeignKey('songs.Song', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
  
    class Meta:
        db_table = "songs_topics"