from django.db import models
from app.models import Registration
import uuid
# from app.models import BaseModel
# Create your models here.

class BaseModel(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class DriverRegistration(Registration):

    """To store details of driver"""
    licence=models.CharField(max_length=20)
    aadhar_card=models.IntegerField()
    pan_card=models.CharField(max_length=20)
    profile_image=models.ImageField(upload_to="driver",null=True,blank=True)
    type=models.CharField(max_length=100,default='Driver')


class Booking(BaseModel):

    """To store booking details"""

    vehicle=(('Select Options','Select Options'),('TOYOTA ETIOS','TOYOTA ETIOS'),('SWIFT DZIRE','SWIFT DZIRE')
    ,('MAHINDRA VERITO','MAHINDRA VERITO'),('INNOVA 6+1','INNOVA 6+1'),
    ('INNOVA 7+1','INNOVA 7+1'),('TEMPO TRAVELLER','TEMPO TRAVELLER'),
    ('MINI BUS','MINI BUS'),('SEDAN','SEDAN'),('HATCHBACK','HATCHBACK'))

    name=models.CharField(max_length=100)
    no_of_adults=models.IntegerField(null=True,blank=True)
    child_name=models.CharField(max_length=100,null=True,blank=True)
    no_of_child=models.IntegerField(null=True,blank=True)
    mobile_number=models.CharField(max_length=15)
    source_address=models.TextField()
    destination_address=models.TextField()
    booking_date=models.DateField(null=True,blank=True)
    booking_time=models.TimeField()
    type_vehicle=models.CharField(max_length=100,choices=vehicle,null=True,blank=True)
    amount=models.FloatField(default=500)
    is_cancel=models.BooleanField(default=False)
    driver=models.ForeignKey(DriverRegistration,related_name='bookings',on_delete=models.CASCADE,null=True,blank=True)

class Payment(BaseModel):
    book=models.ForeignKey(Booking,on_delete=models.CASCADE)
    #registration=models.ForeignKey(Registration,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    oder_id=models.CharField(max_length=100)