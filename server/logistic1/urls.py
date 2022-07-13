from django.contrib import admin
from django.conf import settings
from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('luser/',views.UserRoleApi.as_view()),
    path('luser/<int:pk>/',views.UserRoleApi.as_view()),
    
    path('vehicle/',views.vehicleApi.as_view()),
    path('vehicle/<int:pk>/',views.vehicleApi.as_view()),
    # path('vehiclefilter/',views.filterList.as_view()),

    path('subscription/',views.subscriptionApi.as_view()),
    path('subscription/<int:pk>/',views.subscriptionApi.as_view()),
    path('subscriptionfilter/',views.SubscriptionfilterList.as_view()),

    path('StateAPI/', views.StateAPI.as_view()),
    path('StateAPI/<int:pk>/', views.StateAPI.as_view()),

    path('Statefilter/',views.StatefilterList.as_view()),
    
    path('CouponAPI/', views.CouponAPI.as_view()),
    path('CouponAPI/<int:pk>/', views.CouponAPI.as_view()),
    
    path('StatusAPI/',views.StatusAPI.as_view()),
    path('StatusAPI/<int:pk>/',views.StatusAPI.as_view()),

    path('Custom_user_API/', views.Custom_user_API.as_view()),
    path('Custom_user_API/<int:pk>/',views.Custom_user_API.as_view()),

    # path('Custom_userfilterList/',views.Custom_userfilterList.as_view()),
    
    path('DriverAPI/', views.DriverAPI.as_view()),
    path('DriverAPI/<int:pk>/', views.DriverAPI.as_view()),
    
    path('ReviewAPI/', views.ReviewAPI.as_view()),
    path('ReviewAPI/<int:pk>/', views.ReviewAPI.as_view()),
    
    # path('VehiclesAPI/', views.VehiclesAPI.as_view()),
    # path('VehiclesAPI/<int:pk>/', views.VehiclesAPI.as_view()), 

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

    # path('Order_tracker_API/',views.Order_tracker_API.as_view()),
    # path('Order_tracker_API/<int:pk>/',views.Order_tracker_API.as_view()),
]
# if settings.DEBUG:  
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)