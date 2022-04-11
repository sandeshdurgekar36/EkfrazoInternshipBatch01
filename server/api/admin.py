from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display =['id','User_Role_Name']

@admin.register(vehicle)
class vehicleAdmin(admin.ModelAdmin):
    list_display = ['id','vehicleTypeName','capacity','size','details','price_per_km']

@admin.register(subscription)
class subscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','sub_plan_name','price','validity_period']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['id','Coupon_name','Coupon_discount']
@admin.register(Status)
class Status(admin.ModelAdmin):
    list_display = ['id','Status_name']