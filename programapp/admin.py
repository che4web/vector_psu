from django.contrib import admin
from programapp.models import Program,Speciality,ProgramEge,Ege
from courseapp.models import Course

class SpecialityInline(admin.TabularInline):
    model = Speciality

class ProgramEgeInline(admin.TabularInline):
    model = ProgramEge
# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')
    list_editable = ('name','description')
    list_filter = ('speciality',)
    readonly_fields =('name',)
    inlines= [
        SpecialityInline,
        ProgramEgeInline
    ]
    pass

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass

@admin.register(Ege)
class EgeAdmin(admin.ModelAdmin):
    pass
