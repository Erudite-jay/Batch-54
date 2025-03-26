from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=60,unique=True)
    mobile=models.CharField(max_length=10)
    message=models.TextField(max_length=200)

class test(models.Model):
    test=models.CharField(max_length=100)