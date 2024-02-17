from django.shortcuts import render
from courseapp.models import Course
from django.views.generic import ListView,DetailView

# Create your views here.
from rest_framework import viewsets
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()



class CourseListView(ListView):
    model = Course
    def get_queryset(self):
        name = self.request.GET.get('couse_name')
        return self.model.objects.filter(name__icontains=name)


class CourseDetailView(DetailView):
    model = Course

