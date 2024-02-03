from django.contrib import admin
from programapp.models import Program,Speciality
from courseapp.models import Course

class SpecialityInline(admin.TabularInline):
    model = Speciality
# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    list_filter = ('speciality',)
    inlines= [
        SpecialityInline
    ]
    pass

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass
