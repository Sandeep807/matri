from django.contrib import admin
from .models import *
#Register your models here.
@admin.register(DriverRegistration)
class DriverRegistrationAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','mobile_number','password',
                'gender','licence','aadhar_card','pan_card','profile_image']
                
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','mobile_number','source_address','destination_address','booking_date'
    ,'booking_time','type_vehicle','is_cancel','driver']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=['book','is_paid','oder_id']



