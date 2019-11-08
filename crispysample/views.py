from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import BasicInfo, Person
from .forms import BasicInfoForm, FeedbackForm

# Create your views here.
def home(request):
    #return HttpResponse('hoot!')
    return render(request, 'crispysample/home.html')

class BasicInfoCreateView(CreateView):
  model = BasicInfo
  fields = ('name', 'occupation', 'email')
  template_name = 'crispysample/basicinfo_form.html'


def get_feedback(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'crispysample/feedback.html', {'form': form})


class PersonCreateView(CreateView):
  model = Person
  fields = ('name', 'email', 'job_title', 'bio')