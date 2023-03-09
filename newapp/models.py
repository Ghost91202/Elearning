from django.db import models


# Create your models here.

# model created
# class user(models.Model):
# firstname = models.CharField(max_length=50)
# lastname = models.CharField(max_length=50)
# Email = models.EmailField(max_length=254)
# Contact = models.BigIntegerField()
# password = models.CharField(max_length=250)
# this function is used to converted object to  string
class users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=60)
    contact = models.BigIntegerField()
    password = models.CharField(max_length=50)


def __str__(self):
    return self.firstname
