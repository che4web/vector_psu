from django.contrib import admin
from courseapp.models import Course
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
@admin.register(Course)
class CourseAdmin(SimpleHistoryAdmin):
    list_display=('id','name','prof_typ','known_area')
    list_editable=('prof_typ','known_area')
    pass
