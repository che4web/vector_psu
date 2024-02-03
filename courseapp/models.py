from django.db import models
from programapp.models import Program,Speciality

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название курса")
    program = models.ManyToManyField(Program,verbose_name="Образовательные программы")
    speciality  = models.ManyToManyField(Speciality,verbose_name="Специальности")
    AREA_CHOISES = (
        ("FZ","Физика"),
        ("MT","Математика"),
        ("IT","Информационные технологии"),
    )
    known_area = models.CharField(
        max_length=2,
        blank=True,
        choices=AREA_CHOISES,
        default="FZ"
    )
    PROF_TYP_CHOISES = (
        ('B','Базова'),
        ('P','Профизионнальная'),
        ('V','По выбору'),

    )
    prof_typ= models.CharField(
        max_length=1,
        blank=True,
        choices=PROF_TYP_CHOISES,
        default="B")

    def __str__(self):
        return self.name

