
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  about = models.TextField(blank=True)
  photo_profile = models.ImageField(upload_to='photos/%Y/%m/%d/')
  is_active = models.BooleanField(default=True)

  class Meta:
    db_table = "accounts"
