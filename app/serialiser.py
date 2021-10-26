
from .models import *
from rest_framework import serializers
from .mail import *
import random
# from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta
class RegistrationSerialiser(serializers.ModelSerializer):
    """This serializer is showing all information for user"""

    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    class Meta:
        model=Registration
        fields=['id','profile_created_by','password','first_name',
        'last_name','email','mobile_number','gender',
        'dob','religion','mother_tongue','caste','dosh','height','family_value',
        'marital_status','any_disability','family_status','family_type',
        'education','employed_in','occupation','annual_income',
        'work_location','residing_state','city','pic']
        

# class PackageSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=Package
#         fields='__all__'
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields='_all_'
    def create(self,validated_data):
        #print(validated_data)
        data=Registration.objects.filter(mobilenumber=validated_data['registeruser']).first()
        print("registeruser",data.uid)
        m=None
        if "silver" in validated_data:
            m = date.today() + datetime(months=+3)
        elif "gold" in validated_data:
            m = date.today() + datetime(months=+6)
        else:
            m = date.today() + datetime(months=+12)
        print("shiv",m)
        
        obj=Package.objects.create(
            subscribtion_amount=validated_data['subscribtion_amount'],
            membership=validated_data['membership'],
            registeruser=data,
            expire_pack=m
            ) 
        
        #print(obj)
        return obj
class PaymentSerializer(serializers.ModelSerializer):
    register=RegistrationSerialiser( read_only=True)
    pack=PackageSerializer(read_only=True)
    
    class Meta:
        model=PaymentDetails
        fields=['payment_mode','tranc_id','register','pack','is_verify']
        read_only_fields=['register','pack']
        dept=1

class LoginSerialiser(serializers.Serializer):
    mobile_number=serializers.CharField()
    password=serializers.CharField()

class PasswordSerialiser(serializers.Serializer):
    new_password=serializers.CharField()
    confirm_password=serializers.CharField()
    old_password=serializers.CharField()

class ValidatorSerializer(serializers.Serializer):
    otp=serializers.IntegerField(required=True)

# class SendOtpSerializer(serializers.ModelSerializer):
#     mobilenumber=serializers.CharField(required=True)
#     class Meta:
#         fileds=['mobile_number']
#         def update(self , instance , validated_data):
#             instance.mobile_number = validated_data['mobile_number']
#             otp=random.randint(999,9999)
#             instance.otp = otp
#             instance.save()
#             activate_url = f'{otp}'
#             send_otp(instance.email,instance.first_name,activate_url)
#             return instance


# class BasicDetailsSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=BasicDetails
#         fields='__all__'

# class CasteDetailsSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=CasteDetails
#         fields='__all__'

# class PersonalDetailsSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=PersonalDetails
#         fields='__all__'

# class ProfessionalDetailsSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=ProfessionalDetails
#         fields='__all__'


# class ImageSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model=Image
#         fields='__all__'






