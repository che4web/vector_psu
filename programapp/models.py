from django.db import models

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название ОП")
    description = models.TextField(blank=True,verbose_name='Описание')
    date =models.DateField(blank=True,null=True)
    def ege_list(self):
        return self.programege_set.all()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"program/{self.id}/"

    def get_prof_cousr(self):
        return self.course_set.filter(prof_typ="P")

    def get_var_cousr(self):
        return self.course_set.filter(prof_typ="V")

    class Meta:
        verbose_name="Образовательаня программа"
        verbose_name_plural = "Образовательные программы"


class Ege(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProgramEge(models.Model):
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    ege = models.ForeignKey(Ege,on_delete=models.PROTECT)
    value = models.IntegerField()
    def ege_name(self):
        return self.ege.name


class Speciality(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    programapp = models.ForeignKey(Program,on_delete=models.PROTECT,verbose_name="ОП")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Специальность"
        verbose_name_plural="Специальности"
