from django.contrib import admin
from courseapp.models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
