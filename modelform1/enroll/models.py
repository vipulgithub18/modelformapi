from django.db import models
# Create your models here.

class Useradmin(models.Model):
    name = models.CharField(max_length=100)
    email =  models.EmailField(max_length=100,blank=True)
    pas = models.CharField(max_length=100)