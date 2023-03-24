from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add any additional fields or methods here
    pass

class Movie(models.Model):
    title=models.CharField(max_length=255)
    year=models.IntegerField()
    genre=models.CharField(max_length=511)
    cast=models.CharField(max_length=511)
    description=models.CharField(max_length=10000)
    p1=models.URLField(max_length=255)
    p2=models.URLField(max_length=255)
    p3=models.URLField(max_length=255)
    class Meta:
        db_table="Movie"
