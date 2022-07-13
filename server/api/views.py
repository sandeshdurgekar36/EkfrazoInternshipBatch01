
# from curses.ascii import isalpha
import email
from re import search
from urllib import request, response
# # from aiohttp import Payload
# from argon2 import verify_password
from django.shortcuts import render
# from pandas import value_counts
# import pkg_resources
# from pytest import Instance
# from regex import Regex
from rest_framework.response import Response
# from sympy import per, source
# from yaml import emit
from logistic1.settings import EMAIL_HOST_USER
from .backend import CheckAuth
from .models import *
from .serializers import UserRoleSerializer, vehicleSerializer,subscriptionSerializer
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView, ListAPIView
from django.http import HttpResponse
import random
import base64
import smtplib
from .serializers import *
# UserRoleSerializer, vehicleSerializer,subscriptionSerializer,register1Serializer,login1Serializer,UserSerializer,forgotpasswordSerializer,verifyotpSerializer,UserSerializer,registerownerSerializer
from rest_framework import status,authentication,views
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.authtoken.serializers import AuthTokenSerializer
from api import serializers
from django.contrib.auth.models import User
import urllib.request
from rest_framework.authtoken.models import Token
from django.contrib import messages

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.http import HttpResponsePermanentRedirect
import os,email
import jwt
from django.conf import settings
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from logistic1 import settings
from lib2to3.pgen2.tokenize import generate_tokens
from django.utils.encoding import force_bytes
from . tokens import generate_token
import random
from django.core.mail import message, send_mail, EmailMessage
from django.core.mail import send_mail
import inspect
from django.contrib import auth
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime,timedelta
from rest_framework.filters import SearchFilter,OrderingFilter
# from jose import jwt
# from jose.constants import ALGORITHMS
from django.views.decorators.csrf import csrf_exempt
import string




class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

# Create your views here.
class UserRoleApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = UserRole.objects.get(id=id)
            serializer = UserRoleSerializer(role)
            return Response(serializer.data)

        role = UserRole.objects.all()
        serializer = UserRoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request):
        data= request.data
        if data:
            user= subscription.objects.create( User_Role_Name= data['User_Role_Name'])
            return Response('Subscription added Succesfully')

        
    def put(self,request,pk):
        data = request.data
        if vehicleType.objects.filter(id=pk).exists():
            vehicleType.objects.filter(id=pk).update(User_Role_Name=data['User_Role_Name'])
            return Response('Vehicle data updated ')
        else:
            return Response('vehicle_id not Found',status=status.HTTP_404_NOT_FOUND)

    # def patch(self,request,pk,  format=None):
    #     id = pk
    #     role = UserRole.objects.get(pk=id)
    #     serializer = UserRoleSerializer(role,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'})
    #     return Response(serializer.errors)

    def delete(self,request,pk):
        if UserRole.objects.filter(id=pk).exists():
            UserRole.objects.filter(id=pk).delete()
            return Response('Deleted successfully')
        else:
            return Response('Data not found to delete')


class vehicleApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = vehicleType.objects.get(id=id)
            serializer = vehicleSerializer(role)
            return Response(serializer.data)

        role = vehicleType.objects.all()
        serializer = vehicleSerializer(role, many=True)
        return Response(serializer.data)


    def post(self,request):
        data= request.data
        vehicleTypeName = data.get('vehicleTypeName')
        capacity =data.get('capacity')
        details= data.get('details')
        Vehicle_number = data.get('Vehicle_number')
        price_per_km = data.get('price_per_km')
        min_charge =data.get('min_charge')
        max_time_min= data.get('max_time_min')
        val = re.search("[a-zA-Z]",vehicleTypeName)
        val1 = re.search("[a-zA-Z]",details)
        val2= re.search("[0-9]",price_per_km)
        val3 = re.search("[0-9]",min_charge)
        val4 = re.search("[0-9]",max_time_min)
        val5= re.search("[0-9]",Vehicle_number)
        if data:
            if vehicleType.objects.filter(Vehicle_number=data['Vehicle_number']).exists():
                return Response("vehicle is already exists")
            elif  not  val:
                return Response("vehicleTypeName: only letters allowed")
            elif  not  val1:
                return Response("details: only letters allowed")
            elif not val2:
                return Response("price_per_km: only integers allowed")
            elif not  val3:
                return Response("min_charge: only integers allowed ")
            elif not  val4:
                return Response("max_time_min: only integers allowed")
            elif not val5:
                return Response("Vehicle_number: only integers allowed")

            else:
                user = vehicleType.objects.create(vehicleTypeName= data['vehicleTypeName'],capacity=data['capacity'],details=data['details'],Vehicle_number=data['Vehicle_number'],price_per_km=data['price_per_km'],min_charge= data['min_charge'],max_time_min=data['max_time_min'],badge=data['badge'])
                return Response('vehicle added succesfully')




    def put(self,request,pk):
        data = request.data
        if vehicleType.objects.filter(id=pk).exists():
            vehicleType.objects.filter(id=pk).update(vehicleTypeName= data['vehicleTypeName'],capacity=data['capacity'],details=data['details'],Vehicle_number=data['Vehicle_number'],price_per_km=data['price_per_km'],min_charge= data['min_charge'],max_time_min=data['max_time_min'],badge=data['badge'])
            return Response('Vehicle data updated ')
        else:
            return Response('vehicle_id not Found',status=status.HTTP_404_NOT_FOUND)

    # def patch(self,request,pk,  format=None):
    #     id = pk
    #     role = vehicleType.objects.get(pk=id)
    #     serializer = vehicleSerializer(role,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Partial Data Updated'})
    #     return Response(serializer.errors)

    
    def delete(self,request,pk):
        if vehicleType.objects.filter(id=pk).exists():
            vehicleType.objects.filter(id=pk).delete()
            return Response('Deleted successfully')
        else:
            return Response('Data not found to delete')


class filterApi(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = filtervehicleSerializer

    def post(self, request):
        data= request.data
        if vehicleType.objects.filter(vehicleTypeName=data['vehicleTypeName']).exists():
            role=vehicleType.objects.filter(vehicleTypeName=data['vehicleTypeName']).count()
            
            return Response(role)
        else:
            return Response('please enter correct name')

class filterList(ListAPIView):
    queryset = vehicleType.objects.all()
    serializer_class = vehicleSerializer
    filter_backends = [SearchFilter]
    search_fields =['vehicleTypeName']



class subscriptionApi(APIView):
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = subscription.objects.get(id=id)
            serializer = subscriptionSerializer(role)
            return Response(serializer.data)

        role = subscription.objects.all()
        serializer = subscriptionSerializer(role, many=True)
        return Response(serializer.data)

   

    # def post(self,request):
    #     data= request.data 
    #     sub_plan_name = request.data['sub_plan_name']
    #     if data:
    #             if sub_plan_name == 'Basic':
    #                 # price=199
    #                 # validity_period = '1 Month'
    #                 # user= subscription.objects.create(sub_plan_name= data['sub_plan_name'],price=data['price'],validity_period=['validity_period'].days)
    #                 return Response("you have choosed Basic Subscription,Price = 199 and Validity period is 1 Month")
    #             elif sub_plan_name == 'Gold':
    #                 # price=599
    #                 # validity_period = '6 Monnths'
    #                 return Response("you have choosed Gold Subscription Price = 599 and Validity period is 6 Month")
    #             elif sub_plan_name == 'Premium':
    #                 # price=999
    #                 # validity_period = '1 year'
    #                 return Response("you have choosed Premium Subscription Price=999 and Validity period is 1 Year")
    #             # user= subscription.objects.create(sub_plan_name= data['sub_plan_name'],price=data['price'],validity_period=['validity_period'].days)
    #             return Response('''please choose plan.Basic Gold Premium''')
    #     else:
            
    #          return Response('Please choose the valid plan')


    def post(self,request):
        data= request.data
        if subscription.objects.filter(sub_plan_name=data['sub_plan_name']).exists():
             return Response('subscription plan already exists')
        else:
            user= subscription.objects.create(sub_plan_name=data['sub_plan_name'],price=data['price'],validity_period=data['validity_period'])
            return Response('Subscription added Succesfully')
        
    
    def put(self,request,pk):
        data = request.data
        if subscription.objects.filter(id=pk).exists():
            subscription.objects.filter(id=pk).update(sub_plan_name=data['sub_plan_name'],price=data['price'],validity_period=data['validity_period'])
            return Response('Subscription updated successfully')
        else:
            return Response('Subscription_id not Found',status=status.HTTP_404_NOT_FOUND)

    
    
    def put(self,request,pk,  format=None):
        id = pk
        role = subscription.objects.get(pk=id)
        serializer = subscriptionSerializer(role,data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response( 'Subscription Data Updated')
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


class SubscriptionfilterList(ListAPIView):
    queryset = subscription.objects.all()
    serializer_class = subscriptionSerializer
    filter_backends = [SearchFilter]
    search_fields =['sub_plan_name']

class StateAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        state = State.objects.all().values()
        filter_backends = [SearchFilter]
        Search_fields = ['^name',]
        return Response({'result': state})
    
    def post(self,request):
        data = request.data
        State_name=data.get('State_name')
        nm = re.search("^[a-zA-z]+",State_name)
        if not nm:
            return Response({'name should be alphabet'},status=status.HTTP_406_NOT_ACCEPTABLE)
        elif State.objects.filter(State_name=data['State_name']).exists():
            return Response({'msg': 'State_name is created successfully!!'})
        else:
            state = State.objects.create(State_name=data['State_name'])
        return Response({'msg':'state_name is created successfully'})
        

            
    def put(self,request,pk):
        data = request.data
        if State.objects.filter(id=pk).exists():
            State.objects.filter(id=pk).update(State_name=data['State_name'])
            return Response({'msg':'State updated successfully'})
        else:
            return Response({'error':'State_id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if State.objects.filter(id=pk).exists():
            State.objects.filter(id=pk).delete()
            return Response({'Results':{'Coupon':'State deleted successfully'}})
        else:
            return Response({'Result':{'Coupon':'State is not found to delete'}})

class StatefilterList(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [SearchFilter]
    search_fields =['^State_name']



class CouponAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        coupon = Coupon.objects.all().values()
        return Response({'result': coupon})


    def post(self,request):
        data = request.data
        if Coupon.objects.filter(Coupon_name=data['Coupon_name']).exists():
            return Response({'error': 'Coupon is already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:    
            coupon = Coupon.objects.create(Coupon_name=data['Coupon_name'],Coupon_discount=data['Coupon_discount'])
            return Response({'results':{'msg':'Coupon is created successfully'}})

    def put(self,request,pk):
        data = request.data
        if Coupon.objects.filter(id=pk).exists():
            Coupon.objects.filter(id=pk).update(Coupon_name=data['Coupon_name'],Coupon_discount=data['Coupon_discount'])
            return Response({'msg':'Coupon updated successfully'})
        else:
            return Response({'error':'Coupon_id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Coupon.objects.filter(id=pk).exists():
            Coupon.objects.filter(id=pk).delete()
            return Response({'Results':{'Coupon':'Coupon deleted successfully'}})
        else:
            return Response({'Result':{'Coupon':'Coupon is not found to delete'}})

class StatusAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        status = Status.objects.all().values()
        return Response({'result': status})

    def post(self,request):
        data = request.data
        Status_name = data.get('Status_name')
        nm = re.search("^[a-zA-z]+",Status_name)
        if not nm:
            return Response('Status_name should be alphabet')
            return Response({'msg': 'Status_name is created successfully!!'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if Status.objects.filter(Status_name=data['Status_name']).exists():
            return Response({'error': 'Status_name already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            statuss = Status.objects.create(Status_name=data['Status_name'])
            return Response({'results':{'msg':'Status Created Successfully!!!'}})

    def put(self,request,pk):
        data = request.data
        if Status.objects.filter(id=pk).exists():
            Status.objects.filter(id=pk).update(Status_name=data['Status_name'])
            return Response({'msg':'Status updated successfully'})
        else:
            return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Status.objects.filter(id=pk).exists():
            Status.objects.filter(id=pk).delete()
            return Response({'Results':'Status deleted successfully'})
        return Response({'Status_id not found to delete'})

class Custom_user_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, pk=id):
        customer = Custom_user.objects.all().values()
        return Response({'result': customer})

    def post(self,request):
        # data = request.data
        # first_name = data['first_name']
        # last_name = data['last_name']
        # company_name = data['company_name']
        # mobile_number= data['mobile_number']
        # email = data['email']
        # password = data['password']
        # mobile_number = data['mobile_number']
        # alternate_number = data['alternate_number']
        # role_id = data['role_id']
        # city_id = data['city_id']
        # user_id = data['user_id']
        # zip_code = data['zip_code']
        # adhaar_card = data['adhaar_card']
        # reset_otp = data['reset_otp']
        # profile_image = data['profile_image']
        # pancard_image =data ['pancard_image']
        # if Custom_user.objects.filter(email=request.data['email']).exists():
        #     return Response("")
        # custom_user = Custom_user.objects.create(
        #     first_name = request.data['first_name'],
        #     last_name = request.data['last_name']
        # )

        # if data['profile_image']:
        #     Custom_user.objects.filter(id=custom_user.id).update(
        #         profile_image = request.FILE('profile_image')
        #     )
        # return Response("image updated successfully")





        data = request.data
        profile_image = data.get('profile_image')
        pancard_image = data.get('pancard_image')
        if Custom_user.objects.filter(adhaar_card=data['adhaar_card']).exists():
            return Response({'error': 'adhaar_card already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            custom_user = Custom_user.objects.create(first_name=data['first_name'],last_name=data['last_name'],company_name=data['company_name'],mobile_number=data['mobile_number'],adhaar_card=data['adhaar_card'])
            if data['profile_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = profile_image.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                # "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/"
                filename1 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Profile_image/"+count+'.png'
                fname1 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Profile_image/"+count+'.png'
                ss=  open(filename1, 'wb')
                ss.write(imgdata1)
                ss.close()

            add_profile_img=Custom_user.objects.filter(id=custom_user.id).update(profile_image=fname1)

            if data['pancard_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = pancard_image.split(';base64,')[1]
                imgdata2 = base64.b64decode(split_base_url_data)
                # "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/"
                filename2 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Pancard_image/"+count+'.png'
                fname2 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Pancard_image/"+count+'.png'
                ss=  open(filename2, 'wb')
                ss.write(imgdata2)

                ss.close()

                add_profile_img=Custom_user.objects.filter(id=custom_user.id).update(pancard_image=fname2)
                
                return Response('Customer registered successfully')
            return Response({'msg':'plss enter all the details'})



    def put(self,request,pk):
        data = request.data
        if Custom_user.objects.filter(id=pk).exists():
            Custom_user.objects.filter(id=pk).update(first_name=data['first_name'],last_name=data['last_name'],company_name=data['company_name'],mobile_number=data['mobile_number'],adhaar_card=data['adhaar_card'])
            return Response({'msg':'updated successfully'})
        else:
            if data['profile_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = profile_image.split(';base64,')[1]
                imgdata1 = base64.b64decode(split_base_url_data)
                # "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/"
                filename1 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Profile_image/"+count+'.png'
                fname1 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Profile_image/"+count+'.png'
                ss=  open(filename1, 'wb')
                ss.write(imgdata1)
                ss.close()

                add_profile_img=Custom_user.objects.filter(id=custom_user.id).update(profile_image=fname1)

            if data['pancard_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = pancard_image.split(';base64,')[1]
                imgdata2 = base64.b64decode(split_base_url_data)
                # "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/"
                filename2 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Pancard_image/"+count+'.png'
                fname2 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Pancard_image/"+count+'.png'
                ss=  open(filename2, 'wb')
                ss.write(imgdata2)
                ss.close()

                add_profile_img=Custom_user.objects.filter(id=custom_user.id).update(pancard_image=fname2)
            return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Custom_user.objects.filter(id=pk).exists():
            Custom_user.objects.filter(id=pk).delete()
            return Response({'Results':{'Custom_user':'Customer_user deleted successfully'}})
        else:
            return Response({'Result':{'Custom_user':'Customer_user not found to delete'}})

# class Custom_userfilterList(ListAPIView):
#     queryset = State.objects.all()
#     serializer_class = Custom_user_Serializer
#     filter_backends = [SearchFilter]


#     search_fields =['^first_name']

class DriverAPI(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        drver = Driver.objects.all().values()
        return Response({'result': drver})


    def post(self,request):
        data = request.data
        license_image = data.get('license_image')
        fitness_certificate_image = data.get('fitness_certificate_image')
        emission_test_image = data.get('emission_test_image')
        insurence_image = data.get('insurence_image')
        rc_image = data.get('rc_image')
        permit_expire_image = data.get('permit_expire_image')

        if Driver.objects.filter(driving_license_id=data['driving_license_id']).exists():
            return Response({'error': 'driving_license_id already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            driver = Driver.objects.create(driving_license_id=data['driving_license_id'],vehicle_status=data['vehicle_status'],badge=data['badge'])
            if data['license_image']:
                count=str(random.randint(100,999999999))
                split_base_url_data = license_image.split(';base64,')[1]
                imgdata3 = base64.b64decode(split_base_url_data)
                filename3 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/License_image/"+count+'.png'
                fname3 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/License_image/"+count+'.png'
                ss=  open(filename3, 'wb')
                ss.write(imgdata3)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(license_image=fname3)
                return Response({'results':{'msg':'Driver registered successfully'}})
        # return Response({'msg':'pls fill all the'})
            # if data['fitness_certificate_image']:
            #     count=str(random.randint(100,9999999999))
            #     split_base_url_data = fitness_certificate_image.split(';base64,')[1]
            #     imgdata4 = base64.b64decode(split_base_url_data)
            #     filename4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
            #     fname4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
            #     ss=  open(filename4, 'wb')
            #     ss.write(imgdata4)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(fitness_certificate_image=fname4)

            # if data['emission_test_image']:
            #     count=str(random.randint(100,99999999))
            #     split_base_url_data = emission_test_image.split(';base64,')[1]
            #     imgdata5 = base64.b64decode(split_base_url_data)
            #     filename5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
            #     fname5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
            #     ss=  open(filename5, 'wb')
            #     ss.write(imgdata5)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(emission_test_image=fname5)

            # if data['insurence_image']:
            #     count=str(random.randint(100,999999999))
            #     split_base_url_data = insurence_image.split(';base64,')[1]
            #     imgdata6 = base64.b64decode(split_base_url_data)
            #     filename6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
            #     fname6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
            #     ss=  open(filename6, 'wb')
            #     ss.write(imgdata6)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(insurence_image=fname6)
            
            # if data['rc_image']:
            #     count=str(random.randint(100,9999999))
            #     split_base_url_data = rc_image.split(';base64,')[1]
            #     imgdata7 = base64.b64decode(split_base_url_data)
            #     filename7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
            #     fname7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
            #     ss=  open(filename7, 'wb')
            #     ss.write(imgdata7)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(rc_image=fname7)

            # if data['permit_expire_image']:
            #     count=str(random.randint(100,9999999))
            #     split_base_url_data = permit_expire_image.split(';base64,')[1]
            #     imgdata8 = base64.b64decode(split_base_url_data)
            #     filename8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
            #     fname8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
            #     ss=  open(filename8, 'wb')
            #     ss.write(imgdata8)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(permit_expire_image=fname8)

            # return Response({'results':{'msg':'Driver registered successfully'}})

    def put(self,request,pk):
        data = request.data
        if Driver.objects.filter(driving_license_id=pk).exists():
            Driver.objects.filter(driving_license_id=pk).update(driving_license_id=data['driving_license_id'],vehicle_status=data['vehicle_status'],badge=data['badge'])
            return Response({'msg':'updated successfully'})
        return Response('driving_license_id is not found')
        # else:
        #     if data['license_image']:
        #         count=str(random.randint(100,999999999))
        #         split_base_url_data = license_image.split(';base64,')[1]
        #         imgdata3 = base64.b64decode(split_base_url_data)
        #         filename3 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/License_image/"+count+'.png'
        #         fname3 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/License_image/"+count+'.png'
        #         ss=  open(filename3, 'wb')
        #         ss.write(imgdata3)
        #         ss.close()
        #         add_profile_img=Driver.objects.filter(id=driver.id).update(license_image=fname3)

            # if data['fitness_certificate_image']:
            #     count=str(random.randint(100,9999999999))
            #     split_base_url_data = fitness_certificate_image.split(';base64,')[1]
            #     imgdata4 = base64.b64decode(split_base_url_data)
            #     filename4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
            #     fname4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
            #     ss=  open(filename4, 'wb')
            #     ss.write(imgdata4)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(fitness_certificate_image=fname4)

            # if data['emission_test_image']:
            #     count=str(random.randint(100,99999999))
            #     split_base_url_data = emission_test_image.split(';base64,')[1]
            #     imgdata5 = base64.b64decode(split_base_url_data)
            #     filename5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
            #     fname5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
            #     ss=  open(filename5, 'wb')
            #     ss.write(imgdata5)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(emission_test_image=fname5)

            # if data['insurence_image']:
            #     count=str(random.randint(100,999999999))
            #     split_base_url_data = insurence_image.split(';base64,')[1]
            #     imgdata6 = base64.b64decode(split_base_url_data)
            #     filename6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
            #     fname6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
            #     ss=  open(filename6, 'wb')
            #     ss.write(imgdata6)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(insurence_image=fname6)
            
            # if data['rc_image']:
            #     count=str(random.randint(100,9999999))
            #     split_base_url_data = rc_image.split(';base64,')[1]
            #     imgdata7 = base64.b64decode(split_base_url_data)
            #     filename7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
            #     fname7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
            #     ss=  open(filename7, 'wb')
            #     ss.write(imgdata7)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(rc_image=fname7)

            # if data['permit_expire_image']:
            #     count=str(random.randint(100,9999999))
            #     split_base_url_data = permit_expire_image.split(';base64,')[1]
            #     imgdata8 = base64.b64decode(split_base_url_data)
            #     filename8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
            #     fname8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
            #     ss=  open(filename8, 'wb')
            #     ss.write(imgdata8)
            #     ss.close()
            #     add_profile_img=Driver.objects.filter(id=driver.id).update(permit_expire_image=fname8)

            # return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Driver.objects.filter(id=pk).exists():
            Driver.objects.filter(id=pk).delete()
            return Response({'Results':{'driver':'driver deleted successfully'}})
        return Response({'Result':{'driver':'driver_id not found to delete'}})
    
class ReviewAPI(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        review = Review.objects.all().values()
        return Response({'result': review})

    def post(self,request):
        data =  request.data
        review_stars = data.get('review_stars')
        if review_stars  > str(1) or review_stars < str(5):
            return Response('pls give rating between 1 to 5')
        else:

            vehicle = Review.objects.create(review_stars=data['review_stars'],review_type=data['review_type'],comments=data['comments'],linked_id=data['linked_id'])
        return Response({'message': "Review cteated successfully"})
    
    def put(self,request,pk):
        data = request.data
        if Review.objects.filter(linked_id=pk).exists():
            Review.objects.filter(linked_id=pk).update(review_stars=data['review_stars'],review_type=data['review_type'],comments=data['comments'],linked_id=data['linked_id'])
            return Response({'msg':'updated successfully'})
        return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Review.objects.filter(id=pk).exists():
            Review.objects.filter(id=pk).delete()
            return Response({'Results':{'Review':'Review deleted successfully'}})
        return Response({'Result':{'Review':'Review not found to delete'}})
        
# class VehiclesAPI(APIView):
#     permission_classes = (permissions.AllowAny,)
#     def get(self, request):
#         vehicles = Vehicles.objects.all().values()
#         return Response({'result':vehicles})
   
#     def post(self,request):
#         data =  request.data
#         if Vehicles.objects.filter(name=data['name']).exists():
#             return Response({'error': "name is already exist"}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         vehicles = Vehicles.objects.create(name=data['name'],vehicles_type_id_id=data['vehicles_type_id'],vehicles_number=data['vehicles_number'])
#         return Response({'message': "vehicle cteated successfully"})

#     def put(self,request,pk):
#         data = request.data
#         if Vehicles.objects.filter(id=pk).exists():
#             Vehicles.objects.filter(id=pk).update(name=data['name'],vehicles_type_id_id=data['vehicles_type_id'],vehicles_number=data['vehicles_number'])
#             return Response({'msg':'updated successfully'})
#         else:
#             return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)


#     def delete(self,request,pk):
#         if Vehicles.objects.filter(id=pk).exists():
#             Vehicles.objects.filter(id=pk).delete()
#             return Response({'Results':{'Vehicles':'Vehicle deleted successfully'}})
#         return Response({'Result':{'Vehicles':'Vehicle not found to delete'}})

class Customer_address_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):
        customer_address = Customer_address.objects.all().values()
        return Response({'result':customer_address})

    def post(self,request):
        data =  request.data
        serializer = Customer_address_Serializer(data=request.data)
        if serializer.is_valid():
            cust_obj = serializer.save()
            return Response({'message': 'customer_address is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate=Customer_address_Serializer(data=request.data)
        if validate.is_valid():
            if Customer_address.objects.filter(id=pk).exists():
                Customer_address.objects.filter(account_no=data['account_no']).update(House_number=data['House_number'],address=data['address'],city_id=data['city_id'],account_table_details=data['account_table_details'],account_no=data['account_no'])
                return Response({'success':'data updated successfully'})
            return Response({'error':'account_no is not found'})
        else:
            return Response({'error':'please pass all the data'}) 

    def delete(self,request,pk):
        if Customer_address.objects.filter(id=pk).exists():
            Customer_address.objects.filter(id=pk).delete()
            return Response({'Results':'Customer_address deleted successfully'})
        return Response({'Result':'Customer_address not found to delete'})

class Pickup_details_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        pickup_details = Pickup_details.objects.all().values()
        return Response({'result': pickup_details})

    def post(self,request):
        data =  request.data
        serializer = Pickup_details_serializer(data=request.data)
        if serializer.is_valid():
            pickup = serializer.save()
            
            return Response({'message': 'Pickup_details is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate = Pickup_details_serializer(data=request.data)
        if validate.is_valid():
            if Pickup_details.objects.filter(Customer_address_id=data['Customer_address_id'],id=pk).exists():
                Pickup_details.objects.filter(Customer_address_id=data['Customer_address_id']).update(Customer_address_id=data['Customer_address_id'],pickup_data_time=data['pickup_data_time'],pickup_date=data['pickup_date'],pickup_time=data['pickup_time'])
                return Response({'msg':'Pikup_details updated successfully!!'})
            return Response({'error':'Customer_address_id is not found'})
        else:
            return Response({'msg' : 'pls pass all the details' })

    def delete(self,request,pk):
        if Pickup_details.objects.filter(id=pk).exists():
            Pickup_details.objects.filter(id=pk).delete()
            return Response({'Results':'Customer_address_id deleted successfully'})
        return Response({'Result':'Customer_address_id not found to delete'})

class Drop_details_API(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [CsrfExemptSessionAuthentication]
    serializer_class =  Drop_details_serializer

    def get(self, request):
        drop_details = Drop_details.objects.all().values()
        return Response({'result':drop_details})

    def post(self,request):
        data =  request.data
        serializer = Drop_details_serializer(data=request.data)
        if serializer.is_valid():
            drop = serializer.save()
            return Response({'message': 'Drop_details is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,pk):
        data = request.data
        validate = Drop_details_serializer(data=request.data)
        if validate.is_valid():
            if Drop_details.objects.filter(id=pk).exists():
                Drop_details.objects.filter(id=pk).update(Customer_address_id_id=data['Customer_address_id'],drop_data_time=data['drop_data_time'],drop_date=data['drop_date'],drop_time=data['drop_time'],priority=data['priority'],drop_id_list=data['drop_id_list'])
                return Response({'msg': 'Drop_detail updated successfully!!'})
            return Response({'msg':'Drop_id is not found'})
        # else:
        #    return Response({'ms'})
             
    def delete(self,request,pk):
        if Drop_details.objects.filter(id=pk).exists():
            Drop_details.objects.filter(id=pk).delete()
            return Response({'Results':'Drop_details deleted successfully'})
        return Response({'Result':'Drop_details_id'})
        
class Place_order_API(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [CsrfExemptSessionAuthentication]
    serializer_class = Place_order_serializer
    queryset = Place_order.objects.all()

    def get(self, request):
        place_order = Place_order.objects.all().values()
        return Response({'result':place_order})

    def post(self,request):
        data =  request.data
        serializer = Place_order_serializer(data=request.data)
        if serializer.is_valid():
            place = serializer.save()
            
            return Response({'message': 'Place_order is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate = Place_order_serializer(data=request.data)
        if validate.is_valid():
            if Place_order.objects.filter(id=pk).exists():
                Place_order.objects.filter(id=pk).update(pickup_id_id=data['pickup_id'],drop_id_list=data['drop_id_list'],vehicles_type_id_id=data['vehicles_type_id'],total_estimated_KM=data['total_estimated_KM'],total_estimated_AMT=data['total_estimated_AMT'],ristrict_no_of_drop=data['ristrict_no_of_drop'])
                return Response({'msg':'Place_order details updated successfully'})
            return Response({'error':'Place_order is not found'})
        else:
            return Response({'msg':'place_order details updated successfully'})

    def delete(self,request,pk):
        if Place_order.objects.filter(id=pk).exists():
            Place_order.objects.filter(id=pk).delete()
            return Response({'Results':'Place_order_id deleted successfully'})
        return Response({'Result':'Place_order_id not found to delete'})

class In_order_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        in_order = In_order.objects.all().values()
        return Response({'result':in_order})

    def post(self,request):
        data = request.data
        serializer = In_order_serializer(data=request.data)
        if serializer.is_valid():
            in_odr = serializer.save()
            return Response({'message': 'In_order is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate = In_order_serializer(data=request.data)
        if validate.is_valid():
            if In_order.objects.filter(id=pk).exists():
                In_order.objects.filter(id=pk).update(place_order_id_id=data['place_order_id'],final_amount=data['final_amount'],comment=data['comment'],driver_user_id_id=data['driver_user_id'],Status_id_id=data['Status_id'])
                return Response({'msg':'In_order_details upadated successfully!!'})
            return Response({'msg':'In_order id is not found'})
        else:
         return Response({'error':'plss pass all the details'})

    def delete(self,request,pk):
        if In_order.objects.filter(id=pk).exists():

            In_order.objects.filter(id=pk).delete()
            return Response({'Results':'In_order_id deleted successfully'})
        return Response({'Result':'In_order_id not found to delete'})

class Payment_details_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        payment_details = Payment_details.objects.all().values()
        return Response({'result':payment_details})

    def post(self,request):
        data = request.data
        serializer = Payment_details_serializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            return Response({'message': 'Payment_details is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate = Payment_details_serializer(data=request.data)
        if validate.is_valid():
            if Payment_details.objects.filter(id=pk).exists():
                Payment_details.objects.filter(id=pk).update(In_order_id_id=data['In_order_id'],amount=data['amount'],provider=data['provider'],user_id_id=data['user_id'],Status_id_id=data['Status_id'])
                return Response({'msg':'Payment_details updated successfully!!'})
            return Response({'error':'Payment_id is not found'})
        else:
            return Response({'msg':'Plss pass all the details'})

    def delete(self,request,pk):
        if Payment_details.objects.filter(id=pk).exists():
            Payment_details.objects.filter(id=pk).delete()
            return Response({'Results':'In_order_id deleted successfully'})
        return Response({'Result':'In_order_id not found to delete'})

class Account_details_API(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        account = Account_details.objects.all().values()
        return Response({'result':account})

    def post(self,request):
        data = request.data
        serializer = Account_details_serializer(data=request.data)
        if serializer.is_valid():
            acc = serializer.save()
            return Response({'message': 'Account is cteated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        data = request.data
        validate = Account_details_serializer(data=request.data)
        if validate.is_valid():
            if Account_details.objects.filter(id=pk).exists():
                Account_details.objects.filter(id=pk).update(acc_holder_name=data['acc_holder_name'],bank=data['bank'],branch=data['branch'],account_no=data['account_no'],ifsc_code=data['ifsc_code'])
                return Response({'msg':'Account updated successfully!!'})
            return Response({'error':'Account_details_id is not found'})
        else:
            return Response({'msg':'Plss pass all the details'})

    def delete(self,request,pk):
        if Account_details.objects.filter(id=pk).exists():
            Account_details.objects.filter(id=pk).delete()
            return Response({'Results':'Account deleted successfully'})
        return Response({'Result':'Account_id not found to delete'})

def state_detail(request, pk):
    state = State.objects.get(id = pk)
    serializer = StateSerializer(state)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# class Order_tracker_API(APIView):
    # permission_classes = (permissions.AllowAny,)
    # def order_tracker(request):
    #     if request.method=="POST":
    #         orderId = request.POST.get('orderId', '')
    #     try:
    #         order=Order.objects.filter(pk=orderId)

    #         if len(order)>0:
    #             update = Order.objects.filter(pk=orderId)
    #             updates = []
    #             for order in update:
    #                 # change order status to scheduled
    #                 if order.status == 'processing':
    #                     order.status = 'scheduled'
    #                     order.save()
    #                 updates.append({'status' : order.status})
    #                 response = json.dumps(updates)
    #                 return HttpResponse(response)
    #         else:
    #             return HttpResponse('{}')
    #     except Exception as e:
    #         return HttpResponse('{}')
    # return render(request,"tracker.html")
    

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  queryset = get_user_model().objects.all()
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer

import re
from django.core.validators import ValidationError,RegexValidator
from django.contrib.auth.hashers import make_password, check_password

class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = register1Serializer
    queryset = register1.objects.all()
   
    @csrf_exempt
    def get(self, request):
        CheckAuth(request)
        
        roldata= register1.objects.all().values()
        return Response(roldata)

        

    def post(self,request):
        data= request.data
        username = data.get('username')
        first_name = data.get('first_name')
        last_name =data.get('last_name')
        email =data.get('email')
        password= data.get('password')
        confirm_password= data.get('confirm_password')
        val = re.search("^[a-zA-Z]+",first_name)
        val1 = re.search("^[a-zA-Z]+",last_name)
        if data:
            
            if register1.objects.filter(email=data['email']).exists():
                return Response( "email  already exist", status=status.HTTP_406_NOT_ACCEPTABLE)
            elif password != confirm_password:
                return Response("Password fields didn't match.")
            elif len(password)< 6:
                return Response('password length should be min 6')
            
            elif not val :
                 return Response('name should be alphabet')
            elif not val1 :
                 return Response('Last name should be alphabet')
            elif '@gmail.com' not in email:
                return Response('please enter valid email')


            else:
                user = register1.objects.create(username=username, first_name=first_name, last_name=last_name,
                                             email=email, password=make_password(password))
                # return Response({'message': "Registration successfull"})

                # auth_token = jwt.encode(
                #             {'user_id': user.id, 'username': user.username,'first_name':user.first_name,'last_name':user.last_name,'email':user.email,
                #             }, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                # authorization = 'Bearer'+' '+auth_token

                # response_result = {}
                # response_result['Result'] = 'Registration Succesfull'
                # header = {}
                # header['Authorization'] =authorization
                
                
                # return Response(response_result['Result'], headers=header,status=status.HTTP_200_OK)
                auth_token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=12)}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer'+' '+auth_token
                print(authorization)

                response = {}
                response['Authorization']=authorization
                return Response({'result': {'registration': 'user registered successfully'}}, headers=response, status=status.HTTP_200_OK)
        

        else:
            return Response({'result': 'Please fill all the OPTIONS'})


    # def post(self, request):
    #     data = request.data
    #     username = data.get('username')
    #     first_name = data.get('first_name')
    #     last_name = data.get('last_name')
    #     email = data.get('email')
    #     password = data.get('password')
    #     confirm_password = data.get('confirm_password')

        

    #     if register1.objects.filter(email=email).exists():
    #         return Response({'error':{"email already Taken"}}, status=status.HTTP_406_NOT_ACCEPTABLE)
    #     if register1.objects.filter(username=username).exists():
    #         return Response({'error': {"username already Taken"}}, status=status.HTTP_406_NOT_ACCEPTABLE)
    #     else:
            


            # user = register1.objects.create(username=username, first_name=first_name, last_name=last_name,
            #                                  email=email, password=make_password(password))

            # auth_token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=12)}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
            # authorization = 'Bearer'+' '+auth_token
            # print(authorization)

            # response = {}
            # response['Authorization']=authorization
            # return Response({'result': {'registration': 'user registered successfully'}}, headers=response, status=status.HTTP_200_OK)
    

class login1Api(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [CsrfExemptSessionAuthentication]
    # serializer_class = login1Serializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        user = register1.objects.filter(email=email)
        
        for user in user:
            print(user)
            username = user.username
            user_id = user.id
            data = check_password(password, user.password)
        if user and data:
                print("========================",str(settings.JWT_SECRET_KEY))
                auth_token = jwt.encode({'user_id': user.id, 'username': user.username, 'password':user.password, 'exp': datetime.utcnow() + timedelta(days=5)}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
                authorization = auth_token
                print(authorization)

                response = {}
                response['Authorization']=authorization
                
                return Response({'result': { 'user_info': {'username': username, 'user_id': user_id,  'token': response['Authorization']}, 'message': 'login successfull'}}, headers=response, status=status.HTTP_200_OK)
        return Response({'result': {'error': 'invalid credential'}}, status=status.HTTP_401_UNAUTHORIZED)

    # def post(self,request):
    #     data = request.data
    #     email = data.get('email')
    #     password = data.get('password')

    #     check_user=register1.objects.get(email=email)
        
    #     if data: 
    #         if (check_user & password ==check_user.password):
    #             auth_token = jwt.encode(
    #                         {'user_id': check_user.id, 'username': check_user.username, 'password':check_user.password}, str(settings.JWT_SECRET_KEY), algorithm="HS256")
    #             authorization = 'Bearer'+' '+auth_token

    #             response_result = {}
    #             response_result['Result'] =  'Login Succesfull'
    #             header = {}
    #             header['Authorization'] =authorization
    #             return Response(response_result['Result'], headers=header,status=status.HTTP_200_OK)
                
    #         else:
    #             response="please check your credentials"
    #             return Response(response,status=status.HTTP_400_BAD_REQUEST)
                    

            


    



def grn_otp():
    otp=random.randint(111111,999999)
    return otp
verify_otp=0

class forgot_password_send_otp(APIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = register1Serializer
    def post(self,request):
        response={}
        data = request.data
        email=data.get('email')
        check_user=register1.objects.filter(email=email)
        if check_user:
            otp=grn_otp()
            global verify_otp
            verify_otp=otp
            if '@gmail' in email:
                message = inspect.cleandoc('''Hi,\n%s is your OTP to Forgot Password to your logistic account.\nThis OTP is valid for next 10 minutes,
                                      \nWith Warm Regards,\nTeam logistic,
                                       ''' % (otp))
                send_mail(
                    'One Time Password (OTP)', message
                    ,
                    'pallavisn099@gmail.com',
                    [email],

                )
                
                data_dict = {}
                data_dict["Otp"] = otp
                print(data_dict,'data_dict')
                return Response('OTP sent successfully')
            else:
                return Response(otp)
        else:
            response='Invalid username'
            return Response(response,status=status.HTTP_401_UNAUTHORIZED)

# class forgot_password_send_otp(APIView):
    # permission_classes = (permissions.AllowAny,)
    # authentication_classes = (CsrfExemptSessionAuthentication,)
    # # serializer_class = forgotpasswordSerializer

    # def post(self, request):

    #     data = request.data
        # response = {}
        # response_result = {}
        # response_login = {}

        # email = data.get('email')
        # user_check = register1.objects.get(email=email)
        # if user_check:

        #     user_data = register1.objects.get(email=email)
        #     custom_user = register1.objects.get(id=user_data.id)
        #     message = 'Hello!\nIf you\'ve lost your Password or Wish to Reset it, use the below\n\n reset_id=' + \
        #         str(user_data.id)+'\n\n If you did not request a password reset, you can safely ignore this email. Only a person with access to your email can reset your account password.\n\nThanks\nAdmin'
        #     subject = 'Reset Password - Robas '

        #     email = EmailMessage(subject, message, to=[email])
        #     email.send()
        #     auth_token = jwt.encode(
        #         {'user_id': user_check.id, 'username': user_check.username, 'email': user_check.email}, str(settings.JWT_SECRET_KEY), algorithm="HS256")

        #     serializer = register1Serializer(user_check)

        #     authorization = 'Bearer'+' '+auth_token
        #     response_result['result'] = {
        #         'detail': 'link send in your email-id successfully', 'status': status.HTTP_200_OK}
        #     response_login['Authorization'] = authorization
        #     response_login['status'] = status.HTTP_200_OK

        # else:
        #     header_response = {}
        #     response_login['error'] = {'error': {
        #         'detail': 'Invalid credentials', 'status': status.HTTP_401_UNAUTHORIZED}}
        #     header_response['status'] = status.HTTP_401_UNAUTHORIZED
        #     header_response['detail'] = 'Invalid credentials'

        #     return Response(response_login['error'], headers=header_response)

        # return Response(response_result, headers=response_login)

class check_otp(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    # serializer_class = verifyotpSerializer
    
    def post(self,request):
        data=request.data
        otp=data.get('otp')
        if otp:
            if int(verify_otp) == int(otp) :
                return Response("otp matched")
            else:
                return Response("otp doesnot matched")
        else:
            return Response('please enter otp')        


    
        

class ForgotPasswordUpdate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    # serializer_class = login1Serializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        user_check = register1.objects.filter(email= email)
        
        if password == confirm_password:
            if user_check:
                
                
                user = register1.objects.filter(email=data['email']).update(password=data['password'],confirm_password=data['confirm_password'])
                response="Password Updated Sucessfully"
                return Response(response, status=status.HTTP_200_OK)

            else:
                response="Please Enter Valid username"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response="Password did not matched"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

import uuid
ranom_pass=0
class registerowner(APIView):
    permission_classes = (AllowAny,)
    serializer_class = registerownerSerializer

    def post(self,request):
        serializer = registerownerSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            ranom_pass = uuid.uuid1()
            global random_pass
            random_pass =ranom_pass
            print(email,ranom_pass)

            send_mail(
                'login credentials',
                'Hi,\n\nis your login credentials for your logistic account. \nusername = ' +email+' \npassword= ' + str(ranom_pass)+ '\n\nWith Warm Regards \nTeam logistic',
                'demo.django.login@gmail.com',
                [email],
                fail_silently=False
            )
            
            return Response({"message": "mail sent sucessfully"})
            
    
class verify_registration(APIView):
    permission_classes = (AllowAny,)
    serializer_class = registerownerSerializer

    def post(self,request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        print(email,password)
            
        if str(random_pass) == str(password):
                
            return Response("login succesfull")
        else:
            return Response("credentials doesnot match")
        


# from pgeocode import GeoDistance        
# import googlemaps
# import ssl
# ssl.get_default_verify_paths()
# ssl._create_default_https_context = ssl._create_unverified_context

class find_distance(APIView):
    permission_classes = (AllowAny,)
    serializer_class = mapSerializer

    def post(self,request):
        data= request.data
        source = data.get('source')
        destination = data.get('destination')
        val1 = re.search("[0-9]",source)
        val2 = re.search("[0-9]",destination)
        dist = GeoDistance('in')
        if data:
            if not val1:
                return Response("please enter correct pincode and only digits allowed")
            elif not val2:
                return Response("please enter correct pincode and only digits allowed")
            elif len(source)> 6:
                return Response("Please eneter correct pincode")
            elif len(destination)> 6:
                return Response("Destinatio pincode is incorrect")
            else:
                find_dist = dist.query_postal_code(source, destination)
                total_price = find_dist * 30
                statement = "total distance is " +str(find_dist)+ "km  and Total Price is " +str(total_price)
                return Response(statement )
        else:
            return Response("Please enter correct Pincode")

