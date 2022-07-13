from django.contrib import admin
from .models import *
from .models import Custom_user
from .models import Driver
from .models import Review


# Register your models here.
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display =['id','User_Role_Name']

@admin.register(vehicleType)
class vehicleAdmin(admin.ModelAdmin):
    list_display = ['id','vehicleTypeName','capacity','size','details','Vehicle_number','price_per_km','min_charge','max_time_min','badge']

@admin.register(subscription)
class subscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','sub_plan_name','price','validity_period']

# @admin.register(register1)
# class register1Admin(admin.ModelAdmin):
#     list_display = ['id','username','first_name','last_name','email','password']

# @admin.register(login1)
# class login1Admin(admin.ModelAdmin):
#     list_display = ['id','email', 'password']

# @admin.register(forgotpassword)
# class forgotpasswordAdmin(admin.ModelAdmin):
#     list_display =['id','email']

# @admin.register(resetpassword)
# class resetpasswordAdmin(admin.ModelAdmin):
#     list_display =['id','email','password']

@admin.register(registerowner)
class registerownerAdmin(admin.ModelAdmin):
    list_display= ['fullname','email','mobile_number']

# @admin.register(booking)
# class register1Admin(admin.ModelAdmin):
#     list_display = ['id','first_name','vehicleTypeName']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['State_name']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id','Coupon_name','Coupon_discount']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['Status_name']

@admin.register(Custom_user)
class Custom_user_Admin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','company_name','mobile_number','adhaar_card','profile_image','pancard_image']

@admin.register(Driver)
class Driver_Admin(admin.ModelAdmin):
    list_display = ['id','driving_license_id','vehicle_status','badge']

@admin.register(Review)
class Review_Admin(admin.ModelAdmin):
    list_display = ['review_stars','review_type','comments','linked_id']

# @admin.register(Vehicles)
# class Vehicles_Admin(admin.ModelAdmin):
#     list_display = ['name','vehicles_number','vehicles_type_id']

@admin.register(Customer_address)
class Customer_address(admin.ModelAdmin):
    list_display = ['id','House_number','address','city_id','account_table_details','account_no']

@admin.register(Pickup_details)
class Pickup_details(admin.ModelAdmin):
    list_display = ['Customer_address_id','pickup_data_time','pickup_date','pickup_time']

@admin.register(Drop_details)

class Drop_details(admin.ModelAdmin):
    list_display = ['Customer_address_id','drop_data_time','drop_date','drop_time','priority','drop_id_list']

@admin.register(Place_order)
class Place_order(admin.ModelAdmin):
    list_dispaly = ['user_id','pickup_id','drop_id_list','vehicles_type_id','total_estimated_KM','total_estimated_AMT','ristrict_no_of_drop']

@admin.register(In_order)
class In_order(admin.ModelAdmin):
    list_dispaly = ['place_order_id','Coupon_id','final_amount','comment','driver_user_id','Status_id']

@admin.register(Payment_details)
class Payment_details(admin.ModelAdmin):
    list_dispaly = ['In_order_id','amount','provider','status_id','user_id']

@admin.register(Account_details)
class Account_details(admin.ModelAdmin):
    list_dispaly = ['acc_holder_name','bank','branch','account_no','ifsc_code']
