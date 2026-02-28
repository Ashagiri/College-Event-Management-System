import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class College(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_international = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    DEPARTMENT_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('IT', 'Information Technology'),
        ('CS', 'Computer Science'),
        ('BE', 'Business Engineering'),
        ('EDUC', 'Education'), # Matching department for Education events
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, blank=True)

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('AI', 'AI & Machine Learning'),
        ('TECH', 'Technical'),
        ('CULT', 'Cultural'),
        ('SPRT', 'Sports'),
        ('EDUC', 'Education'), # New category added here!
    ]
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='TECH')
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    seats = models.IntegerField(default=100)
    participants = models.IntegerField(default=0) 
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='events')
    is_global = models.BooleanField(default=False) 

    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.full_name} - {self.event.name}"