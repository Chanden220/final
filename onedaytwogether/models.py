from typing import Any
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import *
from datetime import date
import os
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField


import uuid
# Create your models here.
Sex = (
    ('Male', 'Male'),
    ('Femail', 'Female')
) 

def validate_file_extension(value): 
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def User_Profile_directory_path(request, filename):
 # return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', request.tel, filename])

def Destination_directory_path(request, filename):
 # return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', request.destination, filename])
def Product_directory_path(request, filename):
 # return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', request.Product_name, filename])

class User_Profile(models.Model):
    Users = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.FileField(blank=True, upload_to=User_Profile_directory_path,  validators=[validate_file_extension])
    sex = models.CharField(max_length=7, choices=Sex)
    dob = models.DateField(default='2023-09-03')
    email = models.EmailField(max_length=150)
    tel = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    detail = RichTextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.id)+ '  ' + str(self.Users)
    class Meta():
        ordering = ['id']

class Tour_Team(models.Model):
    Team_name = models.CharField(max_length=30)
    Image = models.FileField(blank=True, upload_to=User_Profile_directory_path,  validators=[validate_file_extension])
    tel = models.CharField(max_length=30)
    detail = RichTextField(blank=True, null=True)
    status = models.BooleanField()
    def __str__(self):
        return str(self.Team_name)
    class Meta():
        ordering = ['id']

class Destination(models.Model):
    destination = models.CharField(max_length=50)
    address=RichTextField(blank=True, null=True)
    Image = models.FileField(blank=True, upload_to=Destination_directory_path,  validators=[validate_file_extension])
    description=RichTextField(blank=True, null=True)
    def __str__(self):
        return self.destination
    class Meta():
        ordering = ['id']

class Schedule(models.Model):
    Destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    Schedule = models.DateField()
    def __str__(self):
        return str(self.Destination)
    class Meta():
        ordering = ['id']    


class Tour(models.Model):
    User_Profile_ID = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    Tour_Team_ID = models.ForeignKey(Tour_Team, on_delete=models.CASCADE)
    Destination_ID = models.ForeignKey(Destination, on_delete=models.CASCADE)
    Schedule_ID = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    def str(self):
        return str(self.id) + '  ' + str(self.User_Profile_ID) + '  '+str(self.Tour_Team_ID) + '  ' + str(self.Destination_ID) + '  '+str(self.Schedule_ID) 
    class Meta():
        ordering = ['id']
class Shop(models.Model):
    Product_name = models.CharField(max_length=30)
    Image = models.FileField(blank=True, upload_to=Product_directory_path,  validators=[validate_file_extension])
    Quantity = models.IntegerField()
    Original_Price = models.DecimalField(max_digits=10, decimal_places=2)
    New_Price = models.DecimalField(max_digits=10, decimal_places=2)
    Product_Type = models.CharField(max_length=30)
    detail = RichTextField(blank=True, null=True)
    def str(self):
        return str(self.Product_name)
    class Meta():
        ordering = ['id']
class Purchase_History(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Product_name = models.ForeignKey(Shop, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Date = models.DateField()
    detail = RichTextField(blank=True, null=True)
    def str(self):
        return str(self.User)+ ' ' +str(self.Product_name)
    class Meta():
        ordering = ['id']
