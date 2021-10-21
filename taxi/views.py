
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
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response({
                    'status':'Failure',
                    'Error':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Error':'Something went wrong'
            })

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
                    'status':'Success',
                    'Payment details':serializer.data
                })
            else:
                return Response({
                    'status':'Failure',
                    'Error':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Message':'Something went wrong'
            })

class BookingVehicle(APIView):
   
    def post(self,request):
        try:
            data=request.data
            serialiser=BookingSerialiser(data=data)
            if serialiser.is_valid():
                return Response(serialiser.data,status=status.HTTP_200_OK)
            else:
                return Response({'error':serialiser.errors,'Message':'Invalid data'})
        except Exception as e:
            print(e)
            return Response({'Status':'Failure',
            'Message':'Something went wrong'})
    def get(self,request):
        try:
            book_all=Booking.objects.all()
            serializer=BookingSerialiser(book_all,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
    
    def patch(self,request):
        try:
            data=request.data
            check=Booking.objects.get(id=data.get('id'))
            check.is_cancel=True
            check.save()
            return Response({'Message':'Booking cancel'})  
        except Exception as e:
            print(e)
            return Response({'Message':'Something went wrong'})

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
                            'status':False,
                            'message':'user not found',
                            'data':{}
                        }
                    )
                user_obj, = authenticate(mobile_number=mobile_number,password=password)
                print(user_obj)

                if user_obj is None:
                    return Response({
                        'status':False,
                        'message':'Invalid username and password',
                        'data':{}
                    })
                token,_=Token.objects.get_or_create(user = user_obj)
                return Response({
                    'status':True,
                    'Message':'Login success',
                    'data':{
                        'token':str(token)
                    }
                })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })

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
                                    'status':'Success',
                                    'details':" Old password missmatch"
                                    })
                            register.set_password(new_password)
                            register.save()
                            return Response({
                                        'status':'Success',
                                        'details':"Password change successfully"
                                    })
                        return Response({
                            'status':'False',
                            'details':"new password and old password are same,please new fill password"
                            })
                    return Response({
                                'status':'False',
                                'details':'new password and confirm passwrod missmatch'  
                                })
                return Response({
                    'status':'False',
                    'details':'mobile number is not found'
                    })
            return Response({
                'status':False,
                "Error":serialise.errors
            })
                            
        except Exception as e:
            print(e)
            return Response({'status':404,'message':'Something went wrong'})

