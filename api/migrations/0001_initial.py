# Generated by Django 2.1.3 on 2018-12-29 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=30)),
                ('coursename', models.CharField(max_length=200)),
                ('status', models.BooleanField(choices=[(True, 'online'), (False, 'offline')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
