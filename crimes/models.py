from django.db import models

# Create your models here.
class TrafficOffence(models.Model):
        offender = models.CharField(max_length=200, default='')
        address = models.CharField(max_length=200, default='')
        plate_no = models.CharField(max_length=100, default='')
        offence = models.CharField(max_length=1000, default='')
        created = models.DateTimeField(auto_now_add=True)
        updated =  models.DateTimeField(auto_now=True) 

        
        def __str__(self):
                return self.offender

class CrimesReported(models.Model):
        offence = models.CharField(max_length=200, default='')
        plate_no = models.CharField(max_length=200, default='')
        location = models.CharField(max_length=200, default='')

        def __str__(self):
                return self.plate_no


class WantedList(models.Model):
        name = models.CharField(max_length=200, default='')
        offence = models.CharField(max_length=200, default='')
        plate_no = models.CharField(max_length=200, default='')

        def __str__(self):
                return self.plate_no

