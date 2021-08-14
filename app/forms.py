from django.db.models import fields
from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http.response import FileResponse
from .models import *

class contact_us_form(ModelForm):
    class Meta:
        model=contact_us_form
        fields='__all__'

class signup_data(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]

    
class add_blog_data(ModelForm):
    class Meta:
        model=blog_data
        fields='__all__'


class checkout_details(ModelForm):
    class Meta:
        model=checkout_detail
        fields='__all__'