from django.db import models
from django.db.models.fields import CharField, FloatField


class mobile_phone(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    price=models.IntegerField(null=True)
    os=models.CharField(max_length=200, null=True)
    ram=models.CharField(max_length=200, null=True)
    storage=models.CharField(max_length=200, null=True)
    display=models.CharField(max_length=200, null=True)
    battery=models.CharField(max_length=200, null=True)
    color_1=models.CharField(max_length=200, null=True)
    color_2=models.CharField(max_length=200, null=True)
    color_3=models.CharField(max_length=200, null=True)
    h=models.CharField(max_length=200, null=True)
    w=models.CharField(max_length=200, null=True)
    m=models.CharField(max_length=200, null=True)
    spec_1=models.CharField(max_length=200, null=True)
    spec_2=models.CharField(max_length=200, null=True)
    spec_3=models.CharField(max_length=200, null=True)
    spec_4=models.CharField(max_length=200, null=True)
    spec_5=models.CharField(max_length=200, null=True)
    model_embed_1=models.CharField(max_length=200, null=True)
    model_embed_2=models.CharField(max_length=200, null=True)
    model_embed_3=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class lego_model(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    price=models.IntegerField(null=True)
    section=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    model_no=models.CharField(max_length=200, null=True)
    pieces=models.CharField(max_length=200, null=True)
    dimensions=models.CharField(max_length=200, null=True)
    top=models.CharField(max_length=200, null=True)
    bottom=models.CharField(max_length=200, null=True)
    spec_1=models.CharField(max_length=200, null=True)
    spec_2=models.CharField(max_length=200, null=True)
    spec_3=models.CharField(max_length=200, null=True)
    spec_4=models.CharField(max_length=200, null=True)
    model_image=models.ImageField(upload_to='static', null=True)
    def __str__(self):
        return self.name


class bedsheet(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    price=models.IntegerField(null=True)
    size=models.CharField(max_length=200, null=True)
    material=models.CharField(max_length=200, null=True)
    type=models.CharField(max_length=200, null=True)
    pattern=models.CharField(max_length=200, null=True)
    wash_care=models.CharField(max_length=200, null=True)
    color=models.CharField(max_length=200, null=True)
    style=models.CharField(max_length=200, null=True)
    spec_1=models.CharField(max_length=200, null=True)
    spec_2=models.CharField(max_length=200, null=True)
    spec_3=models.CharField(max_length=200, null=True)    
    def __str__(self):
        return self.name


class clock(models.Model):
    name=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='static')
    price=models.IntegerField(null=True)
    size=models.CharField(max_length=200, null=True)
    type=models.CharField(max_length=200, null=True)
    mechanism=models.CharField(max_length=200, null=True)
    company=models.CharField(max_length=200, null=True)
    design=models.CharField(max_length=200, null=True)
    mt=models.CharField(max_length=200, null=True)
    style=models.CharField(max_length=200, null=True)
    spec_1=models.CharField(max_length=200, null=True)
    spec_2=models.CharField(max_length=200, null=True)
    spec_3=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class slider(models.Model):
    image_1=models.ImageField(upload_to='static')
    category_1=models.CharField(max_length=200, null=True)
    description_1=models.CharField(max_length=200, null=True)
    image_2=models.ImageField(upload_to='static')
    category_2=models.CharField(max_length=200, null=True)
    description_2=models.CharField(max_length=200, null=True)
    image_3=models.ImageField(upload_to='static')
    category_3=models.CharField(max_length=200, null=True)
    description_3=models.CharField(max_length=200, null=True)
    image_4=models.ImageField(upload_to='static')
    category_4=models.CharField(max_length=200, null=True)
    description_4=models.CharField(max_length=200, null=True)


class categorie(models.Model):
    image=models.ImageField(upload_to='static')
    category=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    style=models.CharField(max_length=200, null=True)
    mb=models.FloatField(max_length=200, null=True)
    link=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.category


class company(models.Model):
    name=models.CharField(max_length=200, null=True)
    logo=models.ImageField(upload_to='static')
    def __str__(self):
        return self.name


class contact_us_form(models.Model):
    name=models.CharField(max_length=200, null=True)
    e_mail=models.CharField(max_length=200, null=True)
    message=models.TextField(max_length=200, null=True)
    def __str__(self):
        return self.name

class signup_form(models.Model):
    username=models.CharField(max_length=200, null=True)
    password=models.CharField(max_length=200, null=True)
    e_mail=models.CharField(max_length=200, null=True)
    phone_number=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.username
        

class blog_data(models.Model):
    name=models.CharField(max_length=200, null=True)
    message=models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.name


class checkout_detail(models.Model):
    first_name=models.CharField(max_length=200, null=True)
    last_name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    state_select=(
        
        ('Andra Pradesh' , 'Andra Pradesh'),
        ('Arunachal Pradesh' , 'Arunachal Pradesh'),
        ('Assam' , 'Assam'),
        ('Bihar' , 'Bihar'),
        ('Chhattisgarh' , 'Chhattisgarh'),
        ('Goa' , 'Goa'),
        ('Gujarat' , 'Gujarat'),
        ('Haryana' , 'Haryana'),
        ('Himachal Pradesh' , 'Himachal Pradesh'),
        ('Jammu and Kashmir' , 'Jammu and Kashmir'),
        ('Jharkhand' , 'Jharkhand'),
        ('Karnataka' , 'Karnataka'),
        ('Kerala' , 'Kerala'),
        ('Madya Pradesh' , 'Madya Pradesh'),
        ('Maharashtra' , 'Maharashtra'),
        ('Manipur' , 'Manipur'),
        ('Meghalaya' , 'Meghalaya'),
        ('Mizoram' , 'Mizoram'),
        ('Nagaland' , 'Nagaland'),
        ('Orissa' , 'Orissa'),
        ('Punjab' , 'Punjab'),
        ('Rajasthan' , 'Rajasthan'),
        ('Sikkim' , 'Sikkim'),
        ('Tamil Nadu' , 'Tamil Nadu'),
        ('Telangana' , 'Telangana'),
        ('Tripura' , 'Tripura'),
        ('Uttaranchal' , 'Uttaranchal'),
        ('Uttar Pradesh' , 'Uttar Pradesh'),
        ('West Bengal' , 'West Bengal'),
        ('Andaman and Nicobar Islands' , 'Andaman and Nicobar Islands'),
        ('Chandigarh' , 'Chandigarh'),
        ('Dadar and Nagar Haveli' , 'Dadar and Nagar Haveli'),
        ('Daman and Diu' , 'Daman and Diu'),
        ('Delhi' , 'Delhi'),
        ('Lakshadeep' , 'Lakshadeep'),
        ('Pondicherry' , 'Pondicherry'),
    )
    state=models.CharField(max_length=200, null=True, choices=state_select)
    pincode=models.CharField(max_length=200, null=True)
    def __str__ (self):
        return self.first_name

# Create your models here.
