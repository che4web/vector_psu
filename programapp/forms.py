from django import forms
from django.forms import ModelForm
from programapp.models import Program

class SearchForm(forms.Form):
    program_name = forms.CharField(label="Название программы", max_length=100,required=False)
    date  = forms.DateField(label="Дата нача программы",required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class BootstrapModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
class ProgramForm(BootstrapModelForm):

    class Meta:
        model = Program
        fields= '__all__'
