from django.contrib.auth.base_user import BaseUserManager
import random
from .mail import *
class UserManager(BaseUserManager):
    use_in_migrations=True
    def create(self,mobile_number,password,**extra_fields):
        if mobile_number:
            user=self.model(mobile_number=mobile_number,**extra_fields)
            user.set_password(password)
            user.is_active=False
            user.otp=random.randint(999,9999)
            user.save(using=self._db)
            #user.email=emai
            activate_url = f'{user.otp}'
            print(user.email)
            send_otp(user.email,user.first_name,activate_url)
            return user
        else:
            raise ValueError('Mobile number is required')

    def create_superuser(self,mobile_number,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff is true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user have is_superuser is true')
        return self.create(mobile_number,password,**extra_fields)
