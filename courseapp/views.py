from django.shortcuts import render
from courseapp.models import Course
from django.views.generic import ListView,DetailView
from django_filters import rest_framework as filters
from helperapp.models import Interest
# Create your views here.
from rest_framework import viewsets
from rest_framework import serializers
class CourseFilter(filters.FilterSet):
    #interest=  filters.NumberFilter(method="get_interest",many=True)

    interest = filters.ModelMultipleChoiceFilter(
        field_name='interest',
        queryset= Interest.objects.all(),
    )
    #def get_interest(self,queryset,field_name,value):
    #    if value:
    #        print(value)
    #        queryset = queryset.filter(interest__id=value)
    #    return queryset



    class Meta:
        model = Course
        #fields = "__all__"
        exclude = ['img']



class CourseSerializer(serializers.ModelSerializer):
    speciality_list = serializers.ListField(
        child=serializers.IntegerField(),
        read_only=True
    )
    img_preview = serializers.CharField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CourseFilter



class CourseListView(ListView):
    model = Course
    def get_queryset(self):
        name = self.request.GET.get('couse_name')
        return self.model.objects.filter(name__icontains=name)


class CourseDetailView(DetailView):
    model = Course

