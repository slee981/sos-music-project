from django.db import models

# Create your models here.
def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'artists/{0}/{1}'.format(instance.id, 'profile')

class Artist(models.Model):
  name = models.CharField(max_length=200)
  about = models.TextField(blank=False, null=True)
  photo_profile = models.ImageField(upload_to=user_directory_path, blank=False, null=True)

  class Meta:
        db_table = "artists"