# Create your views here.
from django.shortcuts import render
from .serialiser import *
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
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
            serializer=RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'Error':'Something went wrong'
            })

    def patch(self,request):
        try:
            data=request.data
            mobile_number=request.GET.get('mobile_number')
            obj=Registration.objects.filter(mobile_number=mobile_number).first()
            if obj is not None:
                serializer=RegistrationSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status':'Success',
                        'message':'Data has been save successfully',
                        'data':serializer.data
                    })
                else:
                        return Response({
                        'status':'Failure',
                        'message':'Invalid data',
                        'data':serializer.errors
                    })
            else:
                return Response({
                    'message':'Mobile number not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'message':'Something went wrong'
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
                            'message':'user not found'
                        },status=status.HTTP_404_NOT_FOUND)
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
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
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
                    'details':'mobile number is not found'
                    },status=status.HTTP_404_NOT_FOUND)
            return Response({
                'status':False,
                "Error":serialise.errors
            })
                            
        except Exception as e:
            print(e)
            return Response({'status':404,'message':'Something went wrong'})

class FindFiveView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            print("mobile_number",mobile_number)
            obj=PaymentDetails.objects.filter(register__mobile_number=mobile_number).first()
            if obj is None:  
                print("package")
                data=Registration.objects.filter(mobile_number=mobile_number).first()
                print(type(data))
                if data is not None:
                    print(data)
                    gender=data.gender
                    if gender=='Male':
                        obj=Registration.objects.filter(gender='Female')[:5]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            'status':"Success",
                            'details':serializer.data
                        })
                    else:
                        obj=Registration.objects.filter(gender='Male')[:5]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            'status':"Success",
                            'details':serializer.data
                        })
            r=obj.register
            gender=r.gender
            print(gender)
            packobj=obj.pack
            membership=packobj.membership
            expiredate=packobj.expire_pack
            print(expiredate)
            if expiredate<=date.today():
                
                    gender=data.gender
                    if gender=='Male':
                        obj=Registration.objects.filter(gender='Female')[:5]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            'status':"Success",
                            'details':serializer.data
                        })
                    else:
                        obj=Registration.objects.filter(gender='Male')[:5]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            'status':"Success",
                            'details':serializer.data})
            else:
                if membership=='Gold':
                    if gender=='Male':
                        obj=Registration.objects.filter(gender='Female')[:30]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                                    
                                    'details':serializer.data,

                                        },status=status.HTTP_200_OK)
                    else:
                        obj=Registration.objects.filter(gender='Male')[:30]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            
                            'details':serializer.data
                            },status=status.HTTP_200_OK)
                elif membership=='Silver':
                    if gender=='Male':
                        obj=Registration.objects.filter(gender='Female')[:60]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                                    
                                    'details':serializer.data,

                                        },status=status.HTTP_200_OK)
                    else:
                        obj=Registration.objects.filter(gender='Male')[:60]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            
                            'details':serializer.data
                            },status=status.HTTP_200_OK)
                else:
                    if gender=='Male':
                        obj=Registration.objects.filter(gender='Female')[:100]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                                    
                                    'details':serializer.data,

                                        },status=status.HTTP_200_OK)
                    else:
                        obj=Registration.objects.filter(gender='Male')[:100]
                        serializer=RegistrationSerializer(obj,many=True)
                        return Response({
                            
                            'details':serializer.data
                            },status=status.HTTP_200_OK)
        except Exception as e:
            print('error',e)
            return Response({
                'details':'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class GetFullInfo(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            data=Registration.objects.filter(mobile_number=mobile_number).first()
            if data is not None:
                serializer=RegistrationSerializer(data)
                return Response({
                    'status':'Success',
                    'Details':serializer.data
                })
            else:
                return Response({
                'Error':'Mobile number not found'
                },status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response({
                'Error':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class VerifyOtp(APIView):
    def post(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            print(mobile_number)
            data=request.data
            serializer=ValidatorSerializer(data=data)
            if serializer.is_valid():
                obj=Registration.objects.filter(mobile_number=mobile_number).first()
                print(obj.otp)
                if obj is not None:
                    if serializer.data['otp']==obj.otp:
                        obj.is_active=True
                        obj.save()
                        return Response({
                            'status':'Success',
                            'Details':'Otp verify successfully'
                        })
                    else:
                        return Response({
                            'Details':'Otp not match'
                        },status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({
                        'Details':'Mobile number not found'
                    },status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({
                    'Error':serializer.errors
                },status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({
                'Error':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class PackageView(APIView):
    def post(self,request):
        try:
            data=request.data
            #mobilenumber=request.GET.get('mobilenumber')
            print(data)
            serializer=PackageSerializer(data=data)
            print("ser",serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'details':serializer.data
                })
            return Response({
                'details':serializer.errors
            },status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print("eeror",e)
            return Response({
                'details':'somthing went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


class PaymentView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            data=request.data
            print(data)
            serializer=PaymentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':"Success",
                    'details':serializer.data
                })
            return Response({
                    'details':serializer.errors
                },status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            import sys, os
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("shiv",e)
            return Response({
                    'details':"somthing went wrong"
                },status=status.HTTP_400_BAD_REQUEST)




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