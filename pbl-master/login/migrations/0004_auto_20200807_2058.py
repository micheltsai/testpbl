# Generated by Django 2.2.5 on 2020-08-07 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200806_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='activate_id',
            new_name='activate',
        ),
    ]
