from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, default=None, unique=False)
    token    = models.CharField(primary_key=True, max_length=255, unique=True, null=False)

class Course(models.Model):
    course_id  = models.AutoField(primary_key=True)
    token      = models.ForeignKey(User, db_column='token', on_delete=models.CASCADE)
    platform   = models.CharField(max_length=30, null=False)
    coursename = models.CharField(max_length=200, null=False)
    status     = models.BooleanField(choices=((True, 'online'), (False, 'offline')))
