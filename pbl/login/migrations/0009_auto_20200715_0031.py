# Generated by Django 2.2.5 on 2020-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20200714_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_title', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateClassName',
        ),
    ]
