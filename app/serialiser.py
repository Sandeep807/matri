
from .models import *
from rest_framework import serializers
from .mail import *

class RegistrationSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['id','profile_created_by','password','first_name',
        'last_name','email','mobile_number','is_verified','gender',
        'dob','religion','mother_tongue','caste','dosh','height','family_value',
        'marital_status','any_disability','family_status','family_type',
        'education','employed_in','occupation','annual_income',
        'work_location','residing_state','city','pic']

class PackageSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields='__all__'

class PaymentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=PaymentDetails
        fields='__all__'

class LoginSerialiser(serializers.Serializer):
    mobile_number=serializers.CharField()
    password=serializers.CharField()

class PasswordSerialiser(serializers.Serializer):
    new_password=serializers.CharField()
    confirm_password=serializers.CharField()
    old_password=serializers.CharField()

# class ValidatorSerializer(serializers.Serializer):
#     otp=serializers.CharField(required=True)

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






