from django.contrib import admin
from . models import TrafficOffence, CrimesReported, WantedList


# Register your models here.
admin.site.register(TrafficOffence)
admin.site.register(CrimesReported)
admin.site.register(WantedList)

