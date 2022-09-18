# Generated by Django 3.0 on 2022-04-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_department_of_information_and_media_road_safety_and_transport_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_of_air_transport',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department_of_information_and_media',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department_of_it_telecom',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='road_safety_and_transport_authority',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
