"""logistic1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from posixpath import basename
from django.contrib import admin
from django.db import router
from django.urls import path,include
from api import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('luser/',views.UserRoleApi.as_view()),
    path('luser/<int:pk>/',views.UserRoleApi.as_view()),
    
    path('vehicle/',views.vehicleApi.as_view()),
    path('vehicle/<int:pk>/',views.vehicleApi.as_view()),

    path('subscription/',views.subscriptionApi.as_view()),
    path('subscription/<int:pk>/',views.subscriptionApi.as_view()),

    path('StateAPI/', views.StateAPI.as_view()),
    path('StateAPI/<int:pk>/', views.StateAPI.as_view()),
    
    path('CouponAPI/', views.CouponAPI.as_view()),
    path('CouponAPI/<int:pk>/', views.CouponAPI.as_view()),
    
    path('StatusAPI/',views.StatusAPI.as_view()),
    path('StatusAPI/<int:pk>/',views.StatusAPI.as_view()),

    path('Custom_user_API/', views.Custom_user_API.as_view()),
    path('Custom_user_API/<int:pk>/',views.Custom_user_API.as_view()),
    
    path('DriverAPI/', views.DriverAPI.as_view()),
    path('DriverAPI/<int:pk>/', views.DriverAPI.as_view()),
    
    path('ReviewAPI/', views.ReviewAPI.as_view()),
    path('ReviewAPI/<int:pk>/', views.ReviewAPI.as_view()),
    
    path('VehiclesAPI/', views.VehiclesAPI.as_view()),
    path('VehiclesAPI/<int:pk>/', views.VehiclesAPI.as_view()), 

    path('Customer_address_API/',views.Customer_address_API.as_view()),
    path('Customer_address_API/<int:pk>/',views.Customer_address_API.as_view()),

    path('Pickup_details_API/',views.Pickup_details_API.as_view()),
    path('Pickup_details_API/<int:pk>/',views.Pickup_details_API.as_view()),

    path('Drop_details_API/',views.Drop_details_API.as_view()),
    path('Drop_details_API/<int:pk>/',views.Drop_details_API.as_view()),

    path('Place_order_API/',views.Place_order_API.as_view()),
    path('Place_order_API/<int:pk>/',views.Place_order_API.as_view()),

    path('In_order_API/',views.In_order_API.as_view()),
    path('In_order_API/<int:pk>/',views.In_order_API.as_view()),

    path('Payment_details_API/',views.Payment_details_API.as_view()),
    path('Payment_details_API/<int:pk>/',views.Payment_details_API.as_view()),

    path('Account_details_API/',views.Account_details_API.as_view()),
    path('Account_details_API/<int:pk>/',views.Account_details_API.as_view()),
    path('getuser/',views.UserDetailAPI.as_view()),

    path('registration/',views.RegisterUserAPIView.as_view()),
    path('registration/<int:pk>/',views.login1Api.as_view()),
    

    path('log/',views.login1Api.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('log/<int:pk>/',views.login1Api.as_view()),
    path('forgot-password-send-otp/',views.forgot_password_send_otp.as_view()),
    path('verify-otp/',views.check_otp.as_view()),
    path('set-password/',views.ForgotPasswordUpdate.as_view()),
    path('register-owner/',views.registerowner.as_view()),
    path('verify-credentials/',views.verify_registration.as_view()),


    path('stateinfo/<int:pk>', views.state_detail),
    path('stateinfo/', views.state_list),
    path('couponinfo/<int:pk>', views.coupon_detail),
    path('couponinfo/', views.coupon_list),
    path('statusinfo/<int:pk>',views.status_detail),
    path('statusinfo/',views.status_list),
]


