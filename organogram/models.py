from turtle import title
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# organogram
class top_title(models.Model):
    top_title = models.CharField(max_length=200)
    organogram_description = RichTextField(blank=True)
# Ministry's Human Resource Strength
class human_resource(models.Model):
    number_of_Human_Resource = models.IntegerField()
    name_of_Human_Resource = models.CharField(max_length=200)
# organogram img
class organogram(models.Model):
    title = models.CharField(max_length=200, blank=True)
    organogram_img = models.ImageField(blank=True,upload_to='pics')
# INFORMATION & DOWNLOADS
class information_download(models.Model):
    title = models.CharField(max_length=200, blank=True)
    download_link = models.CharField(max_length=400)


class ministry_strength(models.Model):
    year = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=20, blank=True)
    executives = models.CharField(max_length=20, blank=True)
    pro_and_mgmt = models.CharField(max_length=20, blank=True)
    support = models.CharField(max_length=20, blank=True)
    operational = models.CharField(max_length=20, blank=True)

