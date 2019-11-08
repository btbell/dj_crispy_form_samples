from django import forms
#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import BasicInfo

class BasicInfoForm(forms.ModelForm):
  class Meta:
    model = BasicInfo
    fields = [
      'name',
      'occupation',
      'email'
    ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('submit', 'Save person'))

class FeedbackForm(forms.Form):
  f_name = forms.CharField(max_length=30, label='First name')
  l_name = forms.CharField(max_length=50, label='Last name')
  email = forms.EmailField(max_length=100, label='Email')
  phone = forms.CharField(label='Phone number')
  comment = forms.CharField(max_length=255)