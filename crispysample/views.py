from django.shortcuts import render, render_to_response
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import BasicInfo, Person, CrispPerson
from .forms import BasicInfoForm, FeedbackForm

# Home page with links to example forms
def home(request):
    return render(request, 'crispysample/home.html')


def thanks(request):
  return render(request, 'crispysample/thanks.html')


# get META dictionary
def display_meta(request):
  values = request.META.items()
  html = []
  for k, v in values:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return HttpResponse('<table>%s</table>' % '\n'.join(html))


# modelForm - Person
class PersonCreateView(CreateView):
  model = Person
  fields = ('name', 'email', 'job_title', 'bio')
  success_url = 'http://localhost:8000/crispysample/thanks'


# modelForm - Crispy Person
class CrispPersonCreateView(CreateView):
  model = CrispPerson
  fields = ('name', 'email', 'job_title', 'bio')
  success_url = 'http://localhost:8000/crispysample/thanks'


# modelForm Basic Info
class BasicInfoCreateView(CreateView):
  model = BasicInfo
  fields = ('name', 'occupation', 'email')
  template_name = 'crispysample/basicinfo_form.html'

# modelForm Crispy Basic Info
class CrispBasicInfoCreateView(CreateView):
  model = BasicInfo
  fields = ('name', 'occupation', 'email')
  template_name = 'crispysample/crispbasicinfo_form.html'


# form.Form examples
def get_feedback(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = FeedbackForm(request.POST)
    # check whether it's valid:
    #if form.is_valid():
      # process the data in form.cleaned_data as required
      # ...
      # redirect to a new URL:
    return HttpResponseRedirect('/thanks/')

  # if a GET (or any other method) we'll create a blank form
  else:
    form = FeedbackForm()

  return render(request, 'crispysample/feedback.html', {'form': form})