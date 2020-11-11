from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('pt_id','patient_name', 'gender','age',
        'phone','address','city')
