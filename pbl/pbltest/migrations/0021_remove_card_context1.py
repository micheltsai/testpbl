# Generated by Django 2.2.6 on 2020-06-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbltest', '0020_auto_20200617_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='context1',
        ),
    ]
