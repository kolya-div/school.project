from django.db import models


# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    email = models.EmailField
