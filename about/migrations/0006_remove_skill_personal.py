# Generated by Django 3.0.5 on 2020-04-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20200421_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='personal',
        ),
    ]
