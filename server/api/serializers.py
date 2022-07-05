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
        fields = ['id','vehicle_Type_id','capacity','size','details','price_per_km']

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
# class Order_tracker_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = 