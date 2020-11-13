
import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User, UserManager)
from django.db import models


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
    def create_patient(self, first_name, last_name, email, date_of_birth,age,phone,address,city, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        patient = Patient(first_name=first_name, last_name=last_name, 
                            email=self.normalize_email(email),
                            date_of_birth=date_of_birth,age=age,address=address,phone=phone,city=city)
        patient.set_password(password)
        patient.save()
        return patient



class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
    
    objects = UserManager()
 
 
    def get_full_name(self):
        return (self.first_name+' '+self.last_name)
 
    def get_short_name(self):
        return self.first_name
 
    def natural_key(self):
        return (self.first_name, self.last_name)
 
    def __str__(self):
        return self.email

class Doctor(User, PermissionsMixin):
    qualification = models.CharField(db_index=True, max_length=255)
    speciality=models.CharField(db_index=True, max_length=255)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]
 
    objects = DoctorManager()
 
    def __str__(self):
        return self.first_name

class Patient(User, PermissionsMixin):
    date_of_birth=models.DateField(db_index=True)
    age=models.CharField(db_index=True, max_length=10)
    phone=models.CharField(db_index=True, max_length=10)
    address=models.TextField(db_index=True, max_length=100)
    city=models.CharField(db_index=True, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]
 
    objects = PatientManager()
 
    def __str__(self):
        return self.first_name

class UserManager(BaseUserManager):
 
    def get_by_natural_key(self, email):
        return self.get(email=email)

