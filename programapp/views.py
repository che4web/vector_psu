from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from programapp.models import Program,Speciality
# Create your views here.

def program_list(request):
    name = request.GET.get('program_name','')
    context = {
        "program_list":Program.objects.filter(name__icontains=name)
    }
    return render(request,'programapp/program_list.html',context)

def program_detail(request,pk):
    obj = Program.objects.get(id=pk)
    base_cousr = obj.course_set.filter(prof_typ="B")

    known_area =[
        {"name":'Физика',
         "code":"FZ",
         'course':base_cousr.filter(known_area="FZ")
         },
        {"name":'математика',
         "code":"MT",
         'course':base_cousr.filter(known_area="MT")
         },
        {"name":'ИТ',
         "code":"IT",
         'course':base_cousr.filter(known_area="IT")
         },
    ]
    context = {
        "program":obj,
        "known_area":known_area,
    }
    return render(request,'programapp/program_detail.html',context)

class SpecialityListView(ListView):
    model = Speciality
