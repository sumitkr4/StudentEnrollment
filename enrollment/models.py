from django.contrib.auth.models import User
from django.db import models


class Classroom(models.Model):
    title = models.CharField(max_length=65)
    descriptions = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    classroom = models.ManyToManyField(Classroom)
