# Generated by Django 3.0.5 on 2020-04-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20200422_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formation',
            options={'ordering': ['starting_date']},
        ),
        migrations.AlterModelOptions(
            name='professional',
            options={'ordering': ['starting_date']},
        ),
    ]
