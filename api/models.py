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


class Message(models.Model):
    msg_id     = models.AutoField(primary_key=True)
    from_user  = models.ForeignKey(User, db_column='from_user', related_name='from_user', on_delete=models.PROTECT)
    to_user    = models.ForeignKey(User, db_column='to_user', related_name='to_user', on_delete=models.PROTECT)
    message    = models.TextField(max_length=2000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)