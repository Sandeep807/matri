
from django.shortcuts import render
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
#from app.models import Registration
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from app.serialiser import ValidatorSerializer
import sys, os
# Create your views here.

class DriverRegister(APIView):
    # queryset=DriverRegistration.objects.all()
    # serializer_class=DriverRegistrationSerialiser
    def post(self,request):
        try:
            data=request.data
            serializer=DriverRegistrationSerialiser(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Details':serializer.data
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    'Error':serializer.errors
                },status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({
                'Error':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request):
    #     try:
    #         data=request.GET.get('mobile_number')
    #         obj=DriverRegistration.objects.filter(mobile_number=data).first()
    #         serializer=DriverLoginSerialiser(obj)
    #         return Response({
    #             'status':'Success',
    #             'Data':serializer.data
    #         })
    #     except Exception as e:
    #         print(e)
    def get(self,request):
        try:
            driver=request.GET.get('mobile_number')
            print('this is ',driver)
            if driver is not None:
                book_all=DriverRegistration.objects.filter(mobile_number=driver)
                print(book_all)
                serializer=DriverRegistrationSerialiser1(book_all,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'Mobile number not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                "message":"Something went wrong"
            },status=status.HTTP_400_BAD_REQUEST)
    

    

# class BookVehicle(viewsets.ModelViewSet):
#     queryset=Booking.objects.all()
#     serializer_class=BookingSerialiser

class PaymentDetail(APIView):
    # queryset=Payment.objects.all()
    # serializer_class=PaymentSerialiser
    def post(self,request):
        try:
            data=request.data
            serializer=PaymentSerialiser(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Payment details':serializer.data
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    'Error':serializer.errors
                },status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):

        try:
            id=request.GET.get('id')
            check=Payment.objects.filter(id=id).first()
            if check:
                check.is_paid=True
                check.save()
                return Response({
                    'Message':'Payment successful'
                },status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'Id not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
    
class BookingVehicle(APIView):
   
    def post(self,request):
        try:
            data=request.data
            serialiser=BookingSerialiser(data=data)
            if serialiser.is_valid():
                serialiser.save()
                return Response(data=serialiser.data,status=status.HTTP_200_OK)
            else:
                return Response({'error':serialiser.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'Message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request):
        try:
            data=request.data
            check=Booking.objects.get(id=data.get('id'))
            check.is_cancel=True
            check.save()
            return Response({'Message':'Booking cancel'},status=status.HTTP_200_OK)  
        except Exception as e:
            print(e)
            return Response({'Message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            serialiser=DriverLoginSerialiser(data=data)
            if serialiser.is_valid():
                mobile_number=serialiser.data['mobile_number']
                password=serialiser.data['password']
                print(password)
                obj=DriverRegistration.objects.filter(mobile_number = mobile_number).first()
                print(obj)
                if not obj:
                    print('sandeep')
                    return Response(
                        {
                            'message':'user not found'
                        }
                    ,status=status.HTTP_404_NOT_FOUND)
                user_obj= authenticate(mobile_number=mobile_number,password=password)
                print(user_obj)

                if user_obj is None:
                    return Response({
                        'message':'Invalid username and password'
                    },status=status.HTTP_401_UNAUTHORIZED)
                token,_=Token.objects.get_or_create(user = user_obj)
                return Response({
                    'Message':'Login success',
                    'data':{
                        'token':str(token)
                    }
                },status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({
                'message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)
class ChangePassword(APIView):
    def post(self,request):
        try:
            mobile_number=request.data.get('mobile_number')
            data=request.data
            serialise=PasswordSerialiser(data=data)
            if serialise.is_valid():
                register=DriverRegistration.objects.filter(mobile_number=mobile_number).first()
                if register is not None:
                    new_password=serialise.data['new_password']
                    confirm_password=serialise.data['confirm_password']
                    old_password=serialise.data['old_password']
                    if confirm_password==new_password:
                        if new_password != old_password:
                            user=authenticate(mobile_number=mobile_number,password=old_password)
                            if user is None:
                                return Response({
                                    'details':" Old password missmatch"
                                    },status=status.HTTP_406_NOT_ACCEPTABLE)
                            register.set_password(new_password)
                            register.save()
                            return Response({
                                        'details':"Password change successfully"
                                    },status=status.HTTP_200_OK)
                        return Response({
                            'details':"new password and old password are same,please new fill password"
                            },status=status.HTTP_406_NOT_ACCEPTABLE)
                    return Response({
                                'details':'new password and confirm passwrod missmatch'  
                                },status=status.HTTP_406_NOT_ACCEPTABLE)
                return Response({
                    'details':'mobile number is not found'
                    },status=status.HTTP_404_NOT_FOUND)
            return Response({
                "Error":serialise.errors
            },status=status.HTTP_406_NOT_ACCEPTABLE)
                            
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

