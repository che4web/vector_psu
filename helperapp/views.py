from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers

from django_filters import rest_framework as filters

from helperapp.models import Interest



# Create your views here.
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class InterestFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="name", lookup_expr='icontains')
    speciality =  filters.NumberFilter(method="get_speciality")

    def get_speciality(self,queryset,field_name,value):
        if value:
            queryset = queryset.filter(speciality__id=value)
        return queryset

    class Meta:
        model = Interest
        fields = "__all__"

class InterestViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InterestFilter


