# Generated by Django 2.2.5 on 2020-07-21 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20200721_0235'),
        ('pbltest', '0019_auto_20200721_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='activate',
        ),
        migrations.RemoveField(
            model_name='card',
            name='group',
        ),
        migrations.AddField(
            model_name='upcard',
            name='activate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.CreateActivate'),
        ),
        migrations.AddField(
            model_name='upcard',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Group'),
        ),
    ]
