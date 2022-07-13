from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate,get_user_model,login
from django.core.exceptions import ValidationError
from django.db.models import Q
from uuid import uuid4
from rest_framework.exceptions import AuthenticationFailed

import django_filters 





User = get_user_model()

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id','User_Role_Name']

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleType
        
        fields = ['id','vehicleTypeName','capacity','size','details','Vehicle_number','price_per_km','min_charge','max_time_min','badge']

class filtervehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterVehicleType
        fields = ['vehicleTypeName']


        
class subscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ['id','sub_plan_name','price','validity_period']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =['State_name']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class StatusSerializer(serializers.Serializer):
    class Meta:
        model = Status
        fileds =['Status_name']

class Custom_user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_user
        fields = '__all__'

class Driver_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '--all--'
        #['id','driving_license_id','vehicle_status','badge','permit_expire_image','rc_image','insurence_image','emission_test_image','fitness_certificate_image','license_image']

class Review_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# class Vehicles_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicles
#         fields = '__all__'

class Customer_address_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_address
        fields = ['id','account_no','House_number','address','city_id','account_table_details']

class Pickup_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup_details
        fields = ['Customer_address_id','pickup_data_time','pickup_date','pickup_time']

class Drop_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Drop_details
        fields = ['Customer_address_id','drop_data_time','drop_date','drop_time','priority','drop_id_list']

class Place_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = Place_order
        fields = ['user_id','pickup_id','drop_id_list','vehicles_type_id','total_estimated_KM','total_estimated_AMT','ristrict_no_of_drop']

class In_order_serializer(serializers.ModelSerializer):
    class Meta:
        model = In_order
        fields = ['place_order_id','Coupon_id','final_amount','comment','driver_user_id','Status_id']

class Payment_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_details
        fields = ['In_order_id','amount','provider','status_id','user_id']

class Account_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Account_details
        fields = ['acc_holder_name','bank','branch','account_no','ifsc_code']
    

# class StateSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = State
#         fields = '__all__'

from django.core.validators import ValidationError,RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
alphabetic = RegexValidator(r'^[a-zA-Z]{4}(\ )[a-zA-Z]*$', 'Only Letters are allowed.')
numeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only Digits are allowed.')

class register1Serializer(serializers.ModelSerializer):
    first_name = models.CharField(max_length=100,validators=[alphabetic])
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = register1
        fields = ('id','username', 'first_name', 'last_name', 'email' ,'password', 'confirm_password' )

       

# class login1Serializer(serializers.ModelSerializer):
#     email= serializers.CharField(max_length=100)
#     password = serializers.CharField(max_length=100)
#     class Meta:
#         model = login1
#         fields = ['id','email', 'password']
        

# class forgotpasswordSerializer(serializers.Serializer):
#     email =serializers.EmailField(min_length=2)
#     redirect_url = serializers.CharField(max_length=500, required=False)

#     class Meta:
#         field = ['email']

# class verifyotpSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=500,required=False)
#     otp = serializers.IntegerField()

#     class Meta:
#         field =['username','otp']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user  
    

class registerownerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = registerowner
        fields='__all__'    

    def create(self, validated_data):
        user = registerowner.objects.create(fullname=validated_data['fullname'],email=validated_data['email'],mobile_number=validated_data['mobile_number'])
        user.save()
        return user

class verify_registrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=500,required=False)
    password = serializers.CharField(max_length=500,required=False)
    class Meta:
        model =registerowner
        fields='__all__'
        
    def validate(self, data):
      
        if registerowner.objects.filter(username=data['username'], password= data['password']).exists():
            return Response({'error': 'user already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        return data



class mapSerializer(serializers.ModelSerializer):
    class Meta:
        model = map
        fields='__all__'

# class bookingSerializer(serializers.Serializer):
#     class Meta:
#         model = booking
#         fields ='__all__'
