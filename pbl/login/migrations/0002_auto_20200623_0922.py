# Generated by Django 2.2.5 on 2020-06-23 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='identify',
            field=models.CharField(default='guest', max_length=123),
        ),
    ]
