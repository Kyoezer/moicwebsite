
from django.db import models


class doat(models.Model):
    directorName = models.CharField(max_length=200, null=True)
    directorPost = models.CharField(max_length=200, null=True)
    directorMail = models.CharField(max_length=200, null=True)
    directorPhoneNumber = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=20, blank=True)
    executives = models.CharField(max_length=20, blank=True)
    pro_and_mgmt = models.CharField(max_length=20, blank=True)
    support = models.CharField(max_length=20, blank=True)
    operational = models.CharField(max_length=20, blank=True)


class ditt(models.Model):
    directorName = models.CharField(max_length=200, null=True)
    directorPost = models.CharField(max_length=200, null=True)
    directorMail = models.CharField(max_length=200, null=True)
    directorPhoneNumber = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=20, blank=True)
    executives = models.CharField(max_length=20, blank=True)
    pro_and_mgmt = models.CharField(max_length=20, blank=True)
    support = models.CharField(max_length=20, blank=True)
    operational = models.CharField(max_length=20, blank=True)


class doim(models.Model):
    directorName = models.CharField(max_length=200, null=True)
    directorPost = models.CharField(max_length=200, null=True)
    directorMail = models.CharField(max_length=200, null=True)
    directorPhoneNumber = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=20, blank=True)
    executives = models.CharField(max_length=20, blank=True)
    pro_and_mgmt = models.CharField(max_length=20, blank=True)
    support = models.CharField(max_length=20, blank=True)
    operational = models.CharField(max_length=20, blank=True)


class rsta(models.Model):
    directorName = models.CharField(max_length=200, null=True)
    directorPost = models.CharField(max_length=200, null=True)
    directorMail = models.CharField(max_length=200, null=True)
    directorPhoneNumber = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=20, blank=True)
    total = models.CharField(max_length=20, blank=True)
    executives = models.CharField(max_length=20, blank=True)
    pro_and_mgmt = models.CharField(max_length=20, blank=True)
    support = models.CharField(max_length=20, blank=True)
    operational = models.CharField(max_length=20, blank=True)