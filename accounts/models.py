from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class OfficerProfile(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	city 		= models.CharField(max_length=100, default='')
	phone		= models.IntegerField(default=0)
	image       = models.ImageField(upload_to='profile_image', blank=True)




