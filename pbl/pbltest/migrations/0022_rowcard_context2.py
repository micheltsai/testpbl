# Generated by Django 2.2.5 on 2020-07-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbltest', '0021_card_context1'),
    ]

    operations = [
        migrations.AddField(
            model_name='rowcard',
            name='context2',
            field=models.TextField(blank=True),
        ),
    ]
