from django.db import models

# Create your models here.
class BasicInfo(models.Model):
  name = models.CharField(max_length=100, null=True)
  occupation = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=100)


class Person(models.Model):
  name = models.CharField(max_length=130)
  email = models.EmailField(blank=True)
  job_title = models.CharField(max_length=30, blank=True)
  bio = models.TextField(blank=True)


class CrispPerson(models.Model):
  name = models.CharField(max_length=130)
  email = models.EmailField(blank=True)
  job_title = models.CharField(max_length=30, blank=True)
  bio = models.TextField(blank=True)