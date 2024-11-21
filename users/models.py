from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser):
	username =  None
	first_name = None
	last_name = None
	name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

 
	class Role(models.TextChoices):
		RIDER = 'rider', 'Rider'
		DRIVER = 'driver', 'Driver'
  
	role = models.CharField(
		max_length=10,
		choices=Role.choices,
		default=Role.RIDER,
	)
  	
	objects = CustomUserManager()

	USERNAME_FIELD = 'phone_number'

	REQUIRED_FIELDS = ['email', 'name', 'password']
 
	def __str__(self):
		return self.name