from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    ids = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    favs = models.IntegerField(blank=True, null=True)

class Users(models.Model):
    ids = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    email = models.EmailField(blank=True, null=True, max_length=254)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profile_pic = models.ImageField(blank=True, null=True)
    cest = models.CharField(max_length=4000)

class Features(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=60)
    image = models.ImageField(blank=True, null=True)
    url = models.CharField(max_length=20, null=True, blank=True)