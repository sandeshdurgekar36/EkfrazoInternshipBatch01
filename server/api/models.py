from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
class UserRole(models.Model):
    User_Role_Name= models.CharField(max_length=100)


class vehicle(models.Model):
    vehicleTypeName = models.CharField(max_length=100)
    capacity = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    details= models.CharField(max_length=100)
    price_per_km =models.FloatField(max_length=10)

class subscription(models.Model):
    sub_plan_name =models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    validity_period = models.DateTimeField(DateTime)

class State(models.Model):
    name = models.CharField(max_length=100)

class Coupon(models.Model):
    Coupon_name = models.CharField(max_length=100)    
    Coupon_discount = models.IntegerField()

class Status(models.Model):
    Status_name = models.CharField(max_length=100)

