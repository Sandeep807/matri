from django.contrib import admin
from django.db import models
from .models import *
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','mobile_number','source_address','destination_address','booking_date'
    ,'booking_time','type_vehicle','is_cancel')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('book','registration','is_paid','oder_id')

