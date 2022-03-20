import email
from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=20)
    email =models.EmailField()
    desc =models.TextField()

