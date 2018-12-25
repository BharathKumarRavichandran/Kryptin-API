from django.db import models

class User(models.Model):
    user_id  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, default=None, unique=False)
    token    = models.CharField(max_length=250, unique=True, null=False)
    platform = models.CharField(max_length=30, null=False)
    course   = models.CharField(max_length=200, null=False)
    status   = models.BooleanField(choices=((True, 'online'), (False, 'offline')))
