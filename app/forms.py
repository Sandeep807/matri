from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.db.models import fields

from .models import Registration

class customUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=Registration
        fields=('mobile_number',)

class customeUserChangeForms(UserChangeForm):
    class Meta:
        model=Registration
        fields=('mobile_number',)