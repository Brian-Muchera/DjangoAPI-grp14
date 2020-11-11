from django.db import models



# Create your models here.
class Patient(models.Model):
    pt_id=models.CharField(max_length=50)
    patient_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=15)
    age=models.CharField(max_length=10)
    phone=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)   
    
    def __str__(self):
        return self.patient_name        

    class Meta:
        ordering = ['-pt_id']
        db_table='Patient'


