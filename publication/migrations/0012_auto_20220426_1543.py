# Generated by Django 3.0 on 2022-04-26 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0011_auto_20220426_1540'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rules',
            new_name='regulation',
        ),
        migrations.RenameModel(
            old_name='regulations',
            new_name='rule',
        ),
    ]
