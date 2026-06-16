from django.db import models


# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    email = models.EmailField()
    Gender = (
        ('erkak','Erkak'),
        ('ayol','Ayol')
    )
    gender = models.CharField(max_length=10, choices=Gender)
    password = models.CharField(max_length=6, help_text="6-ta belgi dan iborat bolsin ")

