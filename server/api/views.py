import email
from urllib import request, response
from django.shortcuts import render
import pkg_resources
from rest_framework.response import Response
from .models import *
from .serializers import UserRoleSerializer, vehicleSerializer,subscriptionSerializer
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse
import random
import base64



from .serializers import UserRoleSerializer, vehicleSerializer,subscriptionSerializer,register1Serializer,login1Serializer,UserSerializer,forgotpasswordSerializer,verifyotpSerializer,UserSerializer,registerownerSerializer
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
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
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
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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




class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

# Create your views here.
class UserRoleApi(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = UserRoleSerializer

    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = UserRole.objects.get(id=id)
            serializer = UserRoleSerializer(role)
            return Response(serializer.data)

        role = UserRole.objects.all()
        serializer = UserRoleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = UserRoleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = UserRole.objects.get(pk=id)
        serializer = UserRoleSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = UserRole.objects.get(pk=id)
        serializer = UserRoleSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = UserRole.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})


class vehicleApi(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = vehicleSerializer

    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = vehicle.objects.get(id=id)
            serializer = vehicleSerializer(role)
            return Response(serializer.data)

        role = vehicle.objects.all()
        serializer = vehicleSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request):
        if request.method == 'POST':
            serializer = vehicleSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = vehicle.objects.get(pk=id)
        serializer = vehicleSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = vehicle.objects.get(pk=id)
        serializer = vehicleSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = vehicletype.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})

class subscriptionApi(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = subscriptionSerializer
    
    def get(self,request,  pk = None, format=None):
        id = pk
        if id is not None:
            role = subscription.objects.get(id=id)
            serializer = subscriptionSerializer(role)
            return Response(serializer.data)

        role = subscription.objects.all()
        serializer = subscriptionSerializer(role, many=True)
        return Response(serializer.data)

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = subscriptionSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created Succesfully'})
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

        
    def put(self,request,pk,  format=None):
        id = pk
        role = subscription.objects.get(pk=id)
        serializer = subscriptionSerializer(role,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

    def patch(self,request,pk,  format=None):
        id = pk
        role = subscription.objects.get(pk=id)
        serializer = subscriptionSerializer(role,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,pk,  format=None):
        id=pk
        role = subscription.objects.get(pk=id)
        role.delete()
        return Response({'msg':'Data Deleted'})

class StateAPI(APIView):
    def get(self, request, pk=id):
        state = State.objects.all().values()
        return Response({'result': state})
 
    def post(self,request):
        data = request.data
        if State.objects.filter(State_id=data['State_id']).exists():
            return Response({'error': 'State_id is already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            state = State.objects.create(State_id=data['State_id'],State_name=data['State_name'])
            return Response({'results':{'msg':'state_id is created successfully'}})
            
    def put(self,request,pk):
        data = request.data
        if State.objects.filter(State_id=data['State_id']).exists():
            State.objects.filter(State_id=data['State_id']).update(State_id=data['State_id'],State_name=data['State_name'])
            return Response({'msg':'State updated successfully'})
        else:
            return Response({'error':'State_id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if State.objects.filter(State_id=pk).exists():
            State.objects.filter(State_id=pk).delete()
            return Response({'Results':{'Coupon':'State deleted successfully'}})
        else:
            return Response({'Result':{'Coupon':'State is not found to delete'}})



class CouponAPI(APIView):
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
    def get(self, request):
        status = Status.objects.all().values()
        return Response({'result': status})

    def post(self,request):
        data = request.data
        if Status.objects.filter(Status_id=data['Status_id']).exists():
            return Response({'error': 'Status_id already exist'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            statuss = Status.objects.create(Status_id=data['Status_id'],Status_name=data['Status_name'])
            return Response({'results':{'msg':'Status Created Successfully!!!'}})

    def put(self,request,pk):
        data = request.data
        if Status.objects.filter(id=pk).exists():
            Status.objects.filter(id=pk).update(Status_id=data['Status_id'],Status_name=data['Status_name'])
            return Response({'msg':'Status updated successfully'})
        else:
            return Response({'error':'Status_id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Status.objects.filter(Status_id=pk).exists():
            Status.objects.filter(Status_id=pk).delete()
            return Response({'Results':{'Status':'Status deleted successfully'}})
        return Response({'Result':{'Status_id':'Status_id not found to delete'}})

class Custom_user_API(APIView):
    def get(self, request, pk=id):
        customer = Custom_user.objects.all().values()
        return Response({'result': customer})

    def post(self,request):
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
                
            return Response({'results':{'msg':'Customer registered successfully'}})
                # return Response({'msg':'plss enter all the details'})



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

class DriverAPI(GenericAPIView):
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

            if data['fitness_certificate_image']:
                count=str(random.randint(100,9999999999))
                split_base_url_data = fitness_certificate_image.split(';base64,')[1]
                imgdata4 = base64.b64decode(split_base_url_data)
                filename4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
                fname4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
                ss=  open(filename4, 'wb')
                ss.write(imgdata4)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(fitness_certificate_image=fname4)

            if data['emission_test_image']:
                count=str(random.randint(100,99999999))
                split_base_url_data = emission_test_image.split(';base64,')[1]
                imgdata5 = base64.b64decode(split_base_url_data)
                filename5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
                fname5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
                ss=  open(filename5, 'wb')
                ss.write(imgdata5)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(emission_test_image=fname5)

            if data['insurence_image']:
                count=str(random.randint(100,999999999))
                split_base_url_data = insurence_image.split(';base64,')[1]
                imgdata6 = base64.b64decode(split_base_url_data)
                filename6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
                fname6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
                ss=  open(filename6, 'wb')
                ss.write(imgdata6)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(insurence_image=fname6)
            
            if data['rc_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = rc_image.split(';base64,')[1]
                imgdata7 = base64.b64decode(split_base_url_data)
                filename7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
                fname7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
                ss=  open(filename7, 'wb')
                ss.write(imgdata7)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(rc_image=fname7)

            if data['permit_expire_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = permit_expire_image.split(';base64,')[1]
                imgdata8 = base64.b64decode(split_base_url_data)
                filename8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
                fname8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
                ss=  open(filename8, 'wb')
                ss.write(imgdata8)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(permit_expire_image=fname8)

            return Response({'results':{'msg':'Driver registered successfully'}})

    def put(self,request,pk):
        data = request.data
        if Driver.objects.filter(driving_license_id=pk).exists():
            Driver.objects.filter(driving_license_id=pk).update(driving_license_id=data['driving_license_id'],vehicle_status=data['vehicle_status'],badge=data['badge'])
            return Response({'msg':'updated successfully'})
        else:
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

            if data['fitness_certificate_image']:
                count=str(random.randint(100,9999999999))
                split_base_url_data = fitness_certificate_image.split(';base64,')[1]
                imgdata4 = base64.b64decode(split_base_url_data)
                filename4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
                fname4 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Fitness_certificate_image/"+count+'.png'
                ss=  open(filename4, 'wb')
                ss.write(imgdata4)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(fitness_certificate_image=fname4)

            if data['emission_test_image']:
                count=str(random.randint(100,99999999))
                split_base_url_data = emission_test_image.split(';base64,')[1]
                imgdata5 = base64.b64decode(split_base_url_data)
                filename5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
                fname5 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Emission_image/"+count+'.png'
                ss=  open(filename5, 'wb')
                ss.write(imgdata5)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(emission_test_image=fname5)

            if data['insurence_image']:
                count=str(random.randint(100,999999999))
                split_base_url_data = insurence_image.split(';base64,')[1]
                imgdata6 = base64.b64decode(split_base_url_data)
                filename6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
                fname6 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Insurence_image/"+count+'.png'
                ss=  open(filename6, 'wb')
                ss.write(imgdata6)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(insurence_image=fname6)
            
            if data['rc_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = rc_image.split(';base64,')[1]
                imgdata7 = base64.b64decode(split_base_url_data)
                filename7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
                fname7 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Rc_image/"+count+'.png'
                ss=  open(filename7, 'wb')
                ss.write(imgdata7)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(rc_image=fname7)

            if data['permit_expire_image']:
                count=str(random.randint(100,9999999))
                split_base_url_data = permit_expire_image.split(';base64,')[1]
                imgdata8 = base64.b64decode(split_base_url_data)
                filename8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
                fname8 = "C:/Users/Sheetal/Desktop/EkfrazoInternshipBatch01/server/images/Permit_image/"+count+'.png'
                ss=  open(filename8, 'wb')
                ss.write(imgdata8)
                ss.close()
                add_profile_img=Driver.objects.filter(id=driver.id).update(permit_expire_image=fname8)

            return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        if Driver.objects.filter(id=pk).exists():
            Driver.objects.filter(id=pk).delete()
            return Response({'Results':{'driver':'driver deleted successfully'}})
        return Response({'Result':{'driver':'driver_id not found to delete'}})
    
class ReviewAPI(APIView):
    def get(self, request):
        review = Review.objects.all().values()
        return Response({'result': review})

    def post(self,request):
        data =  request.data
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
        
class VehiclesAPI(APIView):
    def get(self, request):
        vehicles = Vehicles.objects.all().values()
        return Response({'result':vehicles})
   
    def post(self,request):
        data =  request.data
        if Vehicles.objects.filter(name=data['name']).exists():
            return Response({'error': "name is already exist"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        vehicles = Vehicles.objects.create(name=data['name'],vehicles_type_id_id=data['vehicles_type_id'],vehicles_number=data['vehicles_number'])
        return Response({'message': "vehicle cteated successfully"})

    def put(self,request,pk):
        data = request.data
   
        # if Vehicles.objects.filter(name=data['name'],id=pk).exists():
        #     Vehicles.objects.filter(name=data['name']).update(name=data['name'],vehicles_type_id_id=data['vehicles_type_id'],vehicles_number=data['vehicles_number'])
        #     return Response({'msg':'updated successfully'})
        # return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)
        if Vehicles.objects.filter(id=pk).exists():
            Vehicles.objects.filter(id=pk).update(name=data['name'],vehicles_type_id_id=data['vehicles_type_id'],vehicles_number=data['vehicles_number'])
            return Response({'msg':'updated successfully'})
        else:
            return Response({'error':'id not Found'},status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,pk):
        if Vehicles.objects.filter(id=pk).exists():
            Vehicles.objects.filter(id=pk).delete()
            return Response({'Results':{'Vehicles':'Vehicle deleted successfully'}})
        return Response({'Result':{'Vehicles':'Vehicle not found to delete'}})

class Customer_address_API(APIView):
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
    def get(self, request):
        pickup_details = Pickup_details.objects.all().values()
        return Response({'result': pickup_details})

    # def post(self,request,pk):
    #     data =  request.data
        
    #     if Pickup_details.objects.filter(Customer_address_id=data['Customer_address_id']).exists():
    #         return Response({'error': "Customer_address_id is already exist"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    #         pickup_details = Pickup_details.objects.create(Customer_address_id=data['Customer_address_id'],pickup_data_time=data['pickup_data_time'],pickup_date=data['pickup_date'],pickup_time=data['pickup_time'])
    #     return Response({'message': 'Pickup_details is cteated successfully'})

    def post(self,request):
        data =  request.data
        # pickup_details = Pickup_details.objects.create(Customer_address_id_id=data['Customer_address_id'],pickup_data_time=data['pickup_data_time'],pickup_date=data['pickup_date'],pickup_time=data['pickup_time'])
        # return Response({'message': "Pickup_details cteated successfully"})
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
        else:
            return Response({'error':'priority is not found!!'})


    def delete(self,request,pk):
        if Drop_details.objects.filter(id=pk).exists():
            Drop_details.objects.filter(id=pk).delete()
            return Response({'Results':'Drop_details deleted successfully'})
        return Response({'Result':'Drop_details_id'})
        
class Place_order_API(APIView):
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
            return Response({'msg':'pls pass all the deatils!!'})

    def delete(self,request,pk):
        if Place_order.objects.filter(id=pk).exists():
            Place_order.objects.filter(id=pk).delete()
            return Response({'Results':'Place_order_id deleted successfully'})
        return Response({'Result':'Place_order_id not found to delete'})

class In_order_API(APIView):
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


def coupon_detail(request, pk):
    coupon = Coupon.objects.get(id = pk)
    serializer = CouponSerializer(coupon)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def status_detail(request,pk):
    status = Status.objects.get(id = pk)
    serializer = StatusSerializer(status)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def state_list(request):
    state = State.objects.all()
    serializer = StateSerializer(state, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def coupon_list(request):
    coupon = Coupon.objects.all()
    serializer = CouponSerializer(coupon, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def status_list(request):
    status = Status.objects.all()
    serializer = StatusSerializer(status,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    

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

class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = register1Serializer

    def post(self,request,  format=None):
        if request.method == 'POST':
            serializer = register1Serializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response( "Registration Succesfully")
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)


    
class login1Api(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = login1Serializer

    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        
        user_check =auth.authenticate(username= username,password=password)

        if user_check:
            if user_check.is_authenticated:
                response="login Sucessfully"
                return Response(response, status=status.HTTP_200_OK)
            else:
                response="account is not active"
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
        else:
                response="invalid credentials"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)




def grn_otp():
    otp=random.randint(111111,999999)
    return otp
verify_otp=0

class forgot_password_send_otp(APIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = forgotpasswordSerializer
    def post(self,request):
        response={}
        data = request.data
        username=data.get('username')
        check_user=User.objects.filter(username=username)
        if check_user:
            otp=grn_otp()
            global verify_otp
            verify_otp=otp
            if '@' in username:
                message = inspect.cleandoc('''Hi,\n%s is your OTP to Forgot Password to your logistic account.\nThis OTP is valid for next 10 minutes,
                                      \nWith Warm Regards,\nTeam logistic,
                                       ''' % (otp))
                send_mail(
                    'One Time Password (OTP)', message
                    ,
                    'gunjan.kr518@gmail.com',
                    [username],

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


class check_otp(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    serializer_class = verifyotpSerializer
    
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
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        user_check = User.objects.filter(username= username)
        
        if password == confirm_password:
            if user_check:
                user_data = User.objects.get(username= username)
                user_data.set_password(password)
                user_data.save()

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
        email = data.get('username')
        password = data.get('password')
        
    
        if email:
            
            if str(ranom_pass) == str(password):
                return Response("login succesfull")
            else:
                return Response("credentials doesnot match")
        else:
            return Response('please enter email')
        


       

    







