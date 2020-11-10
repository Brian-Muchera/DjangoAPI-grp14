from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from uuidfield import UUIDField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='', default='')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Appointments(models.Model):
    appointments_id=models.UUIDField(auto=True)
    patients_id=models.CharField(max_length=100)
    doctor_id=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    # time_allocated=models.CharField(max_length=50)
    time_alloted=models.CharField(max_length=50)
    # number_alloted=models.CharField(max_length=50)
    is_completed=models.BooleanField(default=False)
    is_confirmed=models.BooleanField(default=False)
    is_rejected=models.BooleanField(default=False)
    is_disabled=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        get_latest_by='created_at'

