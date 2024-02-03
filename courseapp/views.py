from django.shortcuts import render
from courseapp.models import Course
from django.views.generic import ListView,DetailView

# Create your views here.

class CourseListView(ListView):
    model = Course
    def get_queryset(self):
        name = self.request.GET.get('couse_name')
        return self.model.objects.filter(name__icontains=name)


class CourseDetailView(DetailView):
    model = Course

