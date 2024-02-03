from django.shortcuts import render
from courseapp.models import Course
from django.views.generic import ListView

# Create your views here.

class CourseListView(ListView):
    model = Course

