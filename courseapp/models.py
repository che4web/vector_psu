from django.db import models
from programapp.models import Program,Speciality

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название курса")
    program = models.ManyToManyField(Program,verbose_name="Образовательные программы")
    speciality  = models.ManyToManyField(Speciality,verbose_name="Специальности")

    def __str__(self):
        return self.name

