from django.db import models
from django.contrib.auth.models import User

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='technology/', blank=True)
    
    
    def __str__(self):
        return self.name
    
class Armor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    model_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/',blank=True)
    description = models.TextField()
    creation_year = models.IntegerField()
    views = models.PositiveIntegerField(default=0)
    creator = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology, blank=True)
    
    def __str__(self):
        return self.name



class Actor(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/', blank=True, null=True)

    def __str__(self):
        return self.name


