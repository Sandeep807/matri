from django.db.models import fields
from .models import *
from rest_framework import serializers


class DriverRegistrationSerialiser(serializers.ModelSerializer):
    class Meta:
        model=DriverRegistration
        fields=['first_name','last_name','email',
        'mobile_number','password','gender','licence','aadhar_card','pan_card','profile_image']

class BookingSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Booking
        exclude=('created_at','updated_date')

class PaymentSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

class DriverLoginSerialiser(serializers.Serializer):
    mobile_number=serializers.CharField()
    password=serializers.CharField()

class PasswordSerialiser(serializers.Serializer):
    old_password=serializers.CharField()
    new_password=serializers.CharField()
    confirm_password=serializers.CharField()