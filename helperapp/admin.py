from django.contrib import admin
from helperapp.models import Interest

# Register your models here.
@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    pass
