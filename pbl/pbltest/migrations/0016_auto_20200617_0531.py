# Generated by Django 2.2.6 on 2020-06-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbltest', '0015_auto_20200617_0530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='card',
            name='published_date',
        ),
        migrations.AddField(
            model_name='card',
            name='context1',
            field=models.TextField(blank=True),
        ),
    ]
