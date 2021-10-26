from django.contrib import admin
admin.site.site_header = "Karthavyabharath"
admin.site.index_title = "Welcome to Karthavyabharath Site"
from .models import *
# Register your models here.
# from taxi.models import *
# Register your models here.
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','mobile_number','email','password',
                    'gender','profile_created_by','dob','religion','mother_tongue','caste',
                    'dosh','height','marital_status','any_disability','family_status',
                    'family_type','family_value','education','employed_in','occupation',
                    'annual_income','work_location','residing_state','city',
                    'pic','create_at','updated_at','otp')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display=('amount','membership')

@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display=('transaction_id','order_id','payment_signature','is_paid','register','pack')

