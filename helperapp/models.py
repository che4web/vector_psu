from django.db import models
from courseapp.models import Course
from programapp.models import Speciality


# Create your models here.

class Interest(models.Model):
    name = models.CharField(max_length=255)
    course = models.ManyToManyField(Course,blank=True)
    speciality = models.ManyToManyField(Speciality,blank=True)
    def __str__(self):
        return self.name

