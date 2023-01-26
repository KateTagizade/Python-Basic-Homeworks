"""
models
"""
from django.db import models

# Create your models here.

class Category (models.Model):
    """
    class Category
    """
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Service (models.Model):
    """
    class Service
    """
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    desc = models.TextField(verbose_name='description', blank=True)

