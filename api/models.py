from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    user_id     = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=255, unique=True)
    email       = models.EmailField(max_length=255, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    status      = models.BooleanField(choices=((True, 'online'), (False, 'offline')))
    auth_token  = models.CharField(max_length=255, unique=True, null=True)

    # implemented from the AbstractBaseUser class
    objects = UserManager()

    USERNAME_FIELD  = 'email'
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Course(models.Model):
    course_id  = models.AutoField(primary_key=True)
    user_id    = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    platform   = models.CharField(max_length=30, null=False)
    coursename = models.CharField(max_length=200, null=False)
    status     = models.BooleanField(choices=((True, 'online'), (False, 'offline')))


class Message(models.Model):
    msg_id       = models.AutoField(primary_key=True)
    from_user_id = models.ForeignKey(User, db_column='from_user_id', related_name='from_user_id', on_delete=models.PROTECT)
    to_user_id   = models.ForeignKey(User, db_column='to_user_id', related_name='to_user_id', on_delete=models.PROTECT)
    message      = models.TextField(max_length=2000, null=False)
    created_at   = models.DateTimeField(auto_now_add=True)