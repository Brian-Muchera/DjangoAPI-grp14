from django.conf import settings
import datetime
from django.contrib.auth.models import User
from group14.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User, UserManager,Permission)
from django.db import models
import sys
sys.setrecursionlimit(1500)
# Create your models here.
class DoctorManager(BaseUserManager):
    def create_doctor(self, first_name, last_name, email, qualification, speciality, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        doctor = Doctor(first_name=first_name, last_name=last_name,
                          email=self.normalize_email(email),
                          qualification=qualification, speciality=speciality)
        doctor.set_password(password)
        doctor.save()
        return doctor
class PatientManager(BaseUserManager):
    def create_patient(self, first_name, last_name, email, date_of_birth,age,phone,address, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        patient = Patient(first_name=first_name, last_name=last_name,
                            email=self.normalize_email(email),
                            date_of_birth=date_of_birth,age=age,address=address,phone=phone)
        patient.set_password(password)
        patient.save()
        return patient
class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
    def create_superuser(self, email, first_name, last_name, password=None,**extra_fields):
           if not email:
               raise ValueError("User must have an email")
           if not password:
               raise ValueError("User must have a password")
           if not first_name:
               raise ValueError("User must have a full name")
           user = self.model(
               email=self.normalize_email(email)
           )
           user.first_name = first_name
           user.set_password(password)
           user.last_name = last_name
           user.is_staff = True
           user.is_superuser = True
           user.save(using=self._db)
class User(AbstractBaseUser, PermissionsMixin, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
    objects = CustomUserManager()

    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
    def get_short_name(self):
        return self.first_name
    def natural_key(self):
        return (self.first_name, self.last_name)
    def __str__(self):
        return self.email
class Doctor(User, PermissionsMixin, models.Model):
    name = models.CharField(unique=True,max_length=50, default='SOME STRING')
    qualification = models.CharField(db_index=True, max_length=255)
    speciality=models.CharField(db_index=True, max_length=255)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    address=models.TextField(db_index=True, max_length=100)
    contact = models.EmailField(max_length=100, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]
    objects = DoctorManager()
    def __str__(self):
        return self.first_name


class Patient(User, PermissionsMixin, models.Model):
    date_of_birth=models.DateField(db_index=True)
    age=models.CharField(db_index=True, max_length=10)
    phone=models.CharField(db_index=True, max_length=10)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    address=models.TextField(db_index=True, max_length=100)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]
    objects = PatientManager()
    def __str__(self):
        return self.first_name
class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)