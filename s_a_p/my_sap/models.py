from django.db import models
from django.conf import settings
from django.contrib import admin

# from blog.models import Profile, Post, Tag

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)

class Client(models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField()
    technology = models.CharField (max_length = 20)
    image = models.CharField (max_length = 100)

class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resouce_link = models.URLField()




class Blog(models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField()
    technology = models.CharField (max_length = 20)
    image = models.CharField (max_length = 100)