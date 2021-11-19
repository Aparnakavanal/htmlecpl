from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()