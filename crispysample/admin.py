from django.contrib import admin
from . import models

admin.site.register(models.Invite)
admin.site.register(models.InviteGuest)
