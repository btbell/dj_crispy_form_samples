from django.urls import path

from . import views
from . import contact

app_name = 'crispysample'

urlpatterns = [
  path('', views.home, name='home'),
  path('add', views.PersonCreateView.as_view(), name='add'),
  path('biadd', views.BasicInfoCreateView.as_view(), name='biadd'),
  path('feedback', views.get_feedback, name='get_feedback'),
  ]