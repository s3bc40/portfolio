# Generated by Django 3.0.5 on 2020-04-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20200422_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='professional',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
