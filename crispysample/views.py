from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import BasicInfo, Person
from .forms import BasicInfoForm

# Create your views here.
def home(request):
    #return HttpResponse('hoot!')
    return render(request, 'crispysample/home.html')

class BasicInfoCreateView(CreateView):
  model = BasicInfo
  fields = ('name', 'occupation', 'email')
  template_name = 'crispysample/basicinfo_form.html'

class PersonCreateView(CreateView):
  model = Person
  fields = ('name', 'email', 'job_title', 'bio')