# Generated by Django 3.0 on 2022-04-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0002_annual_performance_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual_performance_agreement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='select_annual_report',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='social_link',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
