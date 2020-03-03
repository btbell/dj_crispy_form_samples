from django.urls import path

from . import views
from . import contact

app_name = 'crispysample'

urlpatterns = [
  # landing page
  path('', views.home, name='home'),
  # person info - NOT CRISPY!!!
  path('add', views.PersonCreateView.as_view(), name='add'),
  # person info - CRISPY!!!
  path('cadd', views.CrispPersonCreateView.as_view(), name='cadd'),
  # basic info - NOT CRISPY!!!
  path('biadd', views.BasicInfoCreateView.as_view(), name='biadd'),
  # basic info - CRISPY!!!
  path('cbiadd', views.CrispBasicInfoCreateView.as_view(), name='cbiadd'),
  #desc
  path('feedback', views.get_feedback, name='get_feedback'),
  #path('crispyfeedback', views.get_crispyfeedback, name='get_crispyfeedback'),
  path('show-meta', views.display_meta),
  #desc
  path('thanks', views.thanks),
  ]