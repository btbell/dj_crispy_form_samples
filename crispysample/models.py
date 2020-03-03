from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
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


class BasicInfo(models.Model):
  name = models.CharField(max_length=100, null=True)
  occupation = models.CharField(max_length=100, null=True)
  email = models.EmailField(max_length=100)


class Invite(models.Model):
  f_name = models.CharField(max_length=40,)
  l_name = models.CharField(max_length=70, null=False)
  email= models.EmailField(null=False, unique=True)
  phone = PhoneNumberField()

  def __str__(self):
    return "%s %s" % (self.l_name, self.f_name)


class InviteGuest(models.Model):
  f_name = models.CharField(max_length=40)
  l_name = models.CharField(max_length=70)
  guest = models.ForeignKey(Invite, on_delete=models.CASCADE)

  def __str__(self):
    return "%s %s" % (self.l_name, self.f_name)