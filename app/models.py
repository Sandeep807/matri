from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import *
from .Options import *

def generate_id():
    try:
        obj=Registration.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class Registration(AbstractUser):

    """To store user details"""
    gender_choices=(('Male','Male'),('Female','Female'))
    username=None
    id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    mobile_number=models.CharField(max_length=15,unique=True)
    otp=models.IntegerField(null=True,blank=True)
    profile_created_by=models.CharField(max_length=100,choices=profile_choices,null=True,blank=True)
    gender=models.CharField(max_length=15,choices=gender_choices,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    religion=models.CharField(max_length=200,choices=religion_choices,null=True,blank=True)
    mother_tongue=models.CharField(max_length=100,choices=tongue,null=True,blank=True)
    caste=models.CharField(max_length=1000,null=True,blank=True)
    gotra=models.CharField(max_length=100,null=True,blank=True)
    peta=models.CharField(max_length=100,null=True,blank=True)
    dosh=models.CharField(max_length=100,null=True,blank=True)
    height=models.CharField(max_length=100,null=True,blank=True)
    marital_status=models.CharField(max_length=100,choices=status_choices,null=True,blank=True)
    any_disability=models.CharField(max_length=100,choices=disability_choices,null=True,blank=True)
    family_status=models.CharField(max_length=100,choices=family_choices,null=True,blank=True)
    family_type=models.CharField(max_length=100,choices=family_type_choices,null=True,blank=True)
    family_value=models.CharField(max_length=100,choices=family_value_choices,null=True,blank=True)
    education=models.CharField(max_length=1000,choices=education_choices,null=True,blank=True)
    employed_in=models.CharField(max_length=100,choices=employee_choices,null=True,blank=True)
    occupation=models.CharField(max_length=100,choices=occupation_choices,null=True,blank=True)
    annual_income=models.CharField(max_length=1000,choices=annual_income_choices,null=True,blank=True)
    work_location=models.CharField(max_length=100,choices=work_choices,null=True,blank=True)
    residing_state=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    dp_pic=models.ImageField(upload_to='matri/image',null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    USERNAME_FIELD='mobile_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()

def generate_id():
    try:
        obj=Package.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class Package(models.Model):

    """To store package details"""
    id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    mem_choices=(('Silver','Silver'),('Gold','Gold'),('Diamond','Diamond'))
    subscription_amount=models.IntegerField()
    membership=models.CharField(max_length=100,choices=mem_choices)
    expire_pack=models.DateField(null=True,blank=True)
    registeruser=models.ForeignKey(Registration,related_name='packs',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def generate_id():
    try:
        obj=PaymentDetails.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class PaymentDetails(models.Model):

    """To store payment details"""
    id=models.IntegerField(default=generate_id,primary_key=True,editable=True)
    tranc_id=models.CharField(max_length=100,null=True,blank=True)
    payment_mode=models.CharField(max_length=100,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    register=models.ForeignKey(Registration,related_name='payment',on_delete=models.CASCADE)
    pack=models.ForeignKey(Package,related_name='payment',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
