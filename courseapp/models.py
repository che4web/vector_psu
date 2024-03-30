from django.db import models
from programapp.models import Program,Speciality
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Foo(models.Model):
    name = models.CharField(max_length=222)

class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название курса")
    program = models.ManyToManyField(Program,verbose_name="Образовательные программы")
    speciality  = models.ManyToManyField(Speciality,verbose_name="Специальности")
    study_load = models.IntegerField(default=0,blank=True)
   # foo = models.OneToOneField(Foo,on_delete=models.SET_NULL,null=True)
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
    date = models.DateField(blank=True,null=True)
    img  = ThumbnailerImageField(blank=True,null=True)

    def img_preview(self):
        if self.img:
            return self.img['preview'].url
    def speciality_list(self):
        return self.speciality.all().values_list('id',flat=True)

    def get_absolute_url(self):
        return f"/course/{self.id}/"

    def __str__(self):
        return self.name

