from django.db import models

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название ОП")
    description = models.TextField(blank=True,verbose_name='Описание')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Образовательаня программа"
        verbose_name_plural = "Образовательные программы"

class Speciality(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    programapp = models.ForeignKey(Program,on_delete=models.PROTECT,verbose_name="ОП")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Специальность"
        verbose_name_plural="Специальности"
