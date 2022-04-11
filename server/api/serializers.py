from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id','User_Role_Name']

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = ['id','vehicleTypeName','capacity','size','details','price_per_km']

class subscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ['id','sub_plan_name','price','validity_period']

class StateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class CouponSerializer(serializers.Serializer):
    Coupon_name = serializers.CharField(max_length=100)    
    Coupon_discount = serializers.IntegerField()

class StatusSerializer(serializers.Serializer):
    Status_name = serializers.CharField(max_length=100)