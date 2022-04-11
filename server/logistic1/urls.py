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
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('luser/',views.UserRoleApi.as_view()),
    path('luser/<int:pk>/',views.UserRoleApi.as_view()),
    
    path('vehicles/',views.vehicleApi.as_view()),
    path('vehicles/<int:pk>/',views.vehicleApi.as_view()),

    path('subscription/',views.subscriptionApi.as_view()),
    path('subscription/<int:pk>/',views.subscriptionApi.as_view()),

    path('stateinfo/<int:pk>', views.state_detail),
    path('stateinfo/', views.state_list),
    path('couponinfo/<int:pk>', views.coupon_detail),
    path('couponinfo/', views.coupon_list),
    path('statusinfo/<int:pk>',views.status_detail),
    path('statusinfo/',views.status_list),
]
