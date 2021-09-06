from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    year = models.IntegerField
    isbn = models.IntegerField
