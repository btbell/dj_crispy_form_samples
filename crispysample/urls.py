from django.urls import path

from . import views
from . import contact

app_name = 'crispysample'

urlpatterns = [
    path('add', views.PersonCreateView.as_view(), name='add'),
    path('biadd', views.BasicInfoCreateView.as_view(), name='biadd'),

  ]