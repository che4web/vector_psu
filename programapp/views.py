from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,CreateView

from programapp.models import Program,Speciality

from django.contrib.auth.decorators import login_required
# Create your views here.
from programapp.forms import SearchForm,ProgramForm

@login_required
def program_list(request):

    form = SearchForm(request.GET)
    program_list =Program.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('program_name')
        date= form.cleaned_data.get('date')
        if name:
            program_list=program_list.filter(name__icontains=name)
        if date:
            program_list =program_list.filter(date__gt=date)
    else:
        pass
    context = {
        "program_list":program_list,
        'form':form,
    }
    return render(request,'programapp/program_list.html',context)

def program_create(request):
    if request.method =='GET':
        form = ProgramForm()
    else:
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form,
    }
    return render(request,'programapp/program_form.html',context)

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    #fields="__all__"

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
