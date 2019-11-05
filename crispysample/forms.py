from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
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

class PersonalDataForm(forms.Form):
  first_name = forms.CharField(required=True, max_length=255)
  last_name = forms.CharField(required=True, max_length=255)
  email = forms.EmailField(required=True)
  phone = forms.CharField(required=True, max_length=200)
  address = forms.CharField(max_length=1000, widget=forms.Textarea())