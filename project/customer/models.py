from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone_num = models.IntegerField()
    company = models.CharField(max_length=100)
    def __str__(self):
        return self.name