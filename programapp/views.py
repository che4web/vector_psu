from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from programapp.models import Program,Speciality
# Create your views here.

def program_list(request):
    context = {
        "program_list":Program.objects.all()
    }
    return render(request,'programapp/program_list.html',context)

def program_detail(request,pk):
    context = {
        "program":Program.objects.get(id=pk)
    }
    return render(request,'programapp/program_detail.html',context)

class SpecialityListView(ListView):
    model = Speciality
