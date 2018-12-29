from django.db import models

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    token    = models.CharField(max_length=255, unique=True, null=False)

class Course(models.Model):
    course_id  = models.AutoField(primary_key=True)
    username   = models.ForeignKey(User, db_column='username', on_delete=models.CASCADE)
    platform   = models.CharField(max_length=30, null=False)
    coursename = models.CharField(max_length=200, null=False)
    status     = models.BooleanField(choices=((True, 'online'), (False, 'offline')))
    