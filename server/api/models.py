from email.headerregistry import Address
from pickle import TRUE
import profile,re
from unittest.util import _MAX_LENGTH
from xmlrpc.client import DateTime
from django.db import models
from django.core.validators import MinLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken
from sqlalchemy import true
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import ValidationError,RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
alphabetic = RegexValidator(r'^[a-zA-Z]{4}(\ )[a-zA-Z]*$', 'Only Letters are allowed.')
numeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only Digits are allowed.')


# Create your models here.
class UserRole(models.Model):
    User_TYPES = (
            ('User', 'User'),
            ('Owner', 'Owner'),
            ('Driver', 'Driver'),

        ) 
    User_Role_Name= models.CharField(max_length=100,choices= User_TYPES)

   

class vehicleType(models.Model):
    vehicleTypeName = models.CharField(max_length=100)
    capacity = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    details= models.CharField(max_length=1000)
    Vehicle_number = models.CharField(max_length = 100,null=true)
    price_per_km =models.FloatField(max_length=100)
    min_charge = models.FloatField(max_length=100,null=True)
    max_time_min = models.TimeField(max_length=100,null=True)
    badge = models.CharField(max_length=100,default='')

class FilterVehicleType(models.Model):
    vehicleTypeName= models.ForeignKey(vehicleType,on_delete=models.CASCADE,null=True)



class subscription(models.Model):
    
    sub_plan_name =models.CharField(max_length=100)
    price = models.FloatField(max_length=10, null=True)
    validity_period = models.TimeField(null=True)


class State(models.Model):
    # State_id = models.IntegerField(null=True)
    State_name = models.CharField(max_length=100)

class Coupon(models.Model):
    # Coupon_id = models.IntegerField(null=True)
    Coupon_name = models.CharField(max_length=100)    
    Coupon_discount = models.IntegerField(null=True)

class Status(models.Model):
    # Status_id = models.IntegerField(null=True)
    Status_name = models.CharField(max_length=100)

class Custom_user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(null=True)
    alternate_number = models.IntegerField(null=True)
    role_id = models.CharField(max_length=50)
    city_id = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100)
    zip_code = models.IntegerField(null=True)
    adhaar_card = models.IntegerField(null=True)
    password = models.IntegerField(null=True)
    reset_otp = models.IntegerField(null=True)
    profile_image = models.ImageField(upload_to='images/Profile_image',null=True)
    pancard_image = models.ImageField(upload_to='images/Pancard_image',null=True)

class Driver(models.Model):
    driving_license_id = models.IntegerField(null=True)
    badge = models.CharField(max_length=50)
    vehicle_id = models.ForeignKey(vehicleType,on_delete=models.CASCADE,null=True)
    owner_user_id = models.IntegerField(null=True)
    user_id = models.CharField(max_length=100)
    driving_license_image = models.ImageField()
    subscription_id = models.ForeignKey(subscription,on_delete=models.CASCADE,null=True)
    driver_status = models.CharField(max_length=50)
    vehicle_status = models.CharField(max_length=50)
    license_expire_date = models.DateField(null=True)
    license_image = models.FileField(upload_to='images/License_image',null=True)
    fitness_certificate_image = models.FileField(upload_to='images/Fitness_certificate_image',null=True)
    permit_expire_date = models.DateField(null=True)
    emission_test_image = models.FileField(upload_to='images/Emission_image',null=True)
    insurence_image = models.FileField(upload_to='images/Insurence_image',null=True)
    rc_image = models.FileField(upload_to='images/Rc_image',null=True)
    permit_expire_image = models.FileField(upload_to='images/Permit_image',null=True)
    account_id = models.IntegerField(null=True)


class Review(models.Model):
   # name = models.CharField(max_length=100)
    review_stars = models.IntegerField(null=True)
    review_type = models.CharField(max_length=50)
    comments = models.CharField(max_length=100)
    linked_id = models.IntegerField(null=True)


# class Vehicles(models.Model):
#     name = models.CharField(max_length=100)
#     vehicles_number = models.IntegerField(null=True)
#     vehicles_type_id = models.ForeignKey(vehicleType,on_delete=models.CASCADE,null=True)

class Customer_address(models.Model):
    #customer_address_id= models.IntegerField(null=True)
    label = models.CharField(max_length=100)
    House_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city_id = models.CharField(max_length=100)
    zip_code = models.IntegerField(null=True)
    refund = models.IntegerField(null=True)
    account_table_details = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    account_no = models.IntegerField(null=True)
    ifsc_code = models.IntegerField(null=True)

class Pickup_details(models.Model):
    Customer_address_id = models.ForeignKey(Customer_address,on_delete=models.CASCADE,null=True)
    pickup_data_time = models.CharField(max_length=100)
    pickup_date = models.DateField(null=True)
    pickup_time = models.TimeField(max_length=10)

class Drop_details(models.Model):
    Customer_address_id = models.ForeignKey(Customer_address,on_delete=models.CASCADE,null=True)
    drop_data_time = models.CharField(max_length=100,null=True,blank=True)
    drop_date = models.DateField(null=True)
    drop_time = models.TimeField(null=True)
    priority = models.IntegerField(null=True)
    drop_id_list = models.IntegerField(null=True)

class Place_order(models.Model):
    user_id = models.CharField(max_length=100)
    pickup_id = models.ForeignKey(Pickup_details,on_delete=models.CASCADE,null=True)
    drop_id_list = models.ForeignKey(Drop_details,on_delete=models.CASCADE,null=True)
    vehicles_type_id = models.ForeignKey(vehicleType,on_delete=models.CASCADE,max_length=100)
    total_estimated_KM = models.IntegerField(null=True)
    total_estimated_AMT = models.IntegerField(null=True)
    ristrict_no_of_drop = models.IntegerField(null=True)

class In_order(models.Model):
    place_order_id = models.ForeignKey(Place_order,on_delete=models.CASCADE,null=True)
    Coupon_id = models.ForeignKey(Coupon,on_delete=models.CASCADE,null=True)
    final_amount = models.IntegerField(null=True)
    comment = models.CharField(max_length=100)
    driver_user_id = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    Status_id = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)

class Payment_details(models.Model):
    In_order_id = models.ForeignKey(In_order,on_delete=models.CASCADE,null=True)
    amount = models.IntegerField(null=True)
    provider = models.CharField(max_length=100)
    status_id = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    user_id = models.CharField(max_length=100,null=True)

class Account_details(models.Model):
    acc_holder_name=models.CharField(max_length=100)
    bank=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account_no=models.IntegerField(null=True)
    ifsc_code=models.IntegerField(null=True)



class register1(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100,validators=[alphabetic])
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(6)])
    confirm_password = models.CharField(max_length=128, validators=[MinLengthValidator(6)],null=True)



# class login1(models.Model):
#     email = models.ForeignKey(register1,on_delete=models.CASCADE,null=True)
#     password = models.CharField(max_length=10)


# class forgotpassword(models.Model):
#     email = models.ForeignKey(register1, on_delete=models.CASCADE,null=True)

    
# class resetpassword(models.Model):
#     email = models.ForeignKey(register1,on_delete=models.CASCADE,null=True)
#     password= models.CharField(max_length=128,null=true)

class registerowner(models.Model):
    fullname = models.CharField(max_length=500)
    email= models.EmailField(max_length=500)
    mobile_number = models.IntegerField(null=True)


class map(models.Model):
    source = models.CharField(max_length=100)
    destination= models.CharField(max_length=100)

# class book(models.Model):
#     first_name = models.ForeignKey(register1, on_delete=models.CASCADE,null=TRUE)
#     vehicleTypeName = models.ForeignKey(vehicleType,on_delete=models.CASCADE,null=true)

