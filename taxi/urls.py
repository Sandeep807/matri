from django.urls import path
#from django.db import router
from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register(r'driver_register',DriverRegister,basename='driver_register')
# router.register(r'payment_taxi',PaymentDetail,basename='payment_taxi')
urlpatterns = [
    path('login/',Login.as_view()),
    path('booking/',BookingVehicle.as_view()),
    path('changepassword/',ChangePassword.as_view()),
    path('driver_register/',DriverRegister.as_view()),
    path('payment_taxi/',PaymentDetail.as_view())
]

# urlpatterns += router.urls


