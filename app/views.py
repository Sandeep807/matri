from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
from .serialiser import *
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken 

from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Register(APIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    # queryset=Registration.objects.all()
    # serializer_class=RegistrationSerialiser
    def post(self,request):
        try:
            data=request.data
            serializer=RegistrationSerialiser(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response({
                    'status':'Failure',
                    'Details':serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Error':'Something went wrong'
            })


class Login(APIView):
    def post(self,request):
        try:
            data=request.data
            serialiser=LoginSerialiser(data=data)
            if serialiser.is_valid():
                mobile_number=serialiser.data['mobile_number']
                password=serialiser.data['password']
                register=Registration.objects.filter(mobile_number = mobile_number).first()
                if not register:
                    return Response(
                        {
                            'status':False,
                            'message':'user not found',
                            'data':{}
                        }
                    )
                user_obj = authenticate(mobile_number=mobile_number,password=password)
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
            # import sys, os
            # exc_type, exc_obj, exc_tb = sys.exc_info()
            # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # print(exc_type, fname, exc_tb.tb_lineno)
            print(e)
            return Response({
                'status':False,
                'message':'Something went wrong'
            })

# class LogOut(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.Registration.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class LogOut(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({
            'message':'Logout successfully'
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            })


class ChangePassword(APIView):
    def post(self,request):
        try:
            mobile_number=request.data.get('mobile_number')
            data=request.data
            serialise=PasswordSerialiser(data=data)
            if serialise.is_valid():
                register=Registration.objects.filter(mobile_number=mobile_number).first()
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

class FindPersonAccordinToGender(APIView):
    def get(self,request):
        try:
            mobile_number=request.GET.get("mobile_number")
            data=Registration.objects.filter(mobile_number=mobile_number).first()
            if data is not None:
                gender=data.gender
                if gender=='Male':
                    female=Registration.objects.filter(gender='Female')[:5]
                    serializer=RegistrationSerialiser(female,many=True)
                    return Response({
                        'status':'Success',
                        'details':serializer.data
                    })
                else:
                    male=Registration.objects.filter(gender='Male')[:5]
                    serializer=RegistrationSerialiser(male,many=True)
                    return Response({
                        'status':'Success',
                        'details':serializer.data
                    })
            else:
                return Response({
                    'status':'Failure',
                    'Error':'Mobile number not found'
                })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'Error':'Something went wrong'
            })

class GetFullInfo(APIView):
    def get(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            data=Registration.objects.filter(mobile_number=mobile_number).first()
            if data is not None:
                serializer=RegistrationSerialiser(data)
                return Response({
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response({
                'status':'Failure',
                'Error':'Mobile number not found'
                })

        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Error':'Something went wrong'
            })

class VerifyOtp(APIView):
    def post(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            data=request.data
            serializer=ValidatorSerializer(data=data)
            if serializer.is_valid():
                obj=Registration.objects.filter(mobile_number=mobile_number).first()
                if obj is not None:
                    if serializer.data['otp']==obj.otp:
                        return Response({
                            'status':'Success',
                            'Details':'Otp verify successfully'
                        })
                    else:
                        return Response({
                            'status':'Failure',
                            'Details':'Otp not match'
                        })
                else:
                    return Response({
                        'status':'Failure',
                        'Details':'Mobile number not found'
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

class PackageView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=PackageSerialiser(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response({
                    'status':'Failure',
                    'Details':'Invalid data'
                })
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Error':'Something went wrong'
            })



# class BasicDetail(viewsets.ModelViewSet):
#     queryset=BasicDetails.objects.all()
#     serializer_class=BasicDetailsSerialiser

# class CasteDetail(viewsets.ModelViewSet):
#     queryset=CasteDetails.objects.all()
#     serializer_class=CasteDetailsSerialiser

# class PersonalDetail(viewsets.ModelViewSet):
#     queryset=PersonalDetails.objects.all()
#     serializer_class=PersonalDetailsSerialiser

# class ProfessionalDetail(viewsets.ModelViewSet):
#     queryset=ProfessionalDetails.objects.all()
#     serializer_class=ProfessionalDetailsSerialiser

# class PackageDetail(viewsets.ModelViewSet):
#     queryset=Package.objects.all()
#     serializer_class=PackageSerialiser

# class PaymentDetail(viewsets.ModelViewSet):
#     queryset=PaymentDetails.objects.all()
#     serializer_class=PaymentSerialiser

# class ImageUpload(viewsets.ModelViewSet):
#     queryset=Image.objects.all()
#     serializer_class=ImageSerialiser