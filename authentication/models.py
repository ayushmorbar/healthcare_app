from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Address fields
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator(regex=r'^\d{6}$', message='Pincode must be 6 digits')]
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional patient-specific fields can be added here
    
    def __str__(self):
        return f"Patient: {self.user.first_name} {self.user.last_name}"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional doctor-specific fields can be added here
    
    def __str__(self):
        return f"Doctor: {self.user.first_name} {self.user.last_name}"
