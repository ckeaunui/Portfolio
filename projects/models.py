from django.db import models
from .models import *
from PIL import Image

# Create your models here.
class Project(models.Model):
    categories = (
        ('Data Cleaning', 'Data Cleaning'),
        ('Data Visualization', 'Data Visualization'),
        ('Machine Learning', 'Machine Learning'),
    )
    title = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=500, null=True, choices=categories)
    thumbnail = models.ImageField(null=True)

