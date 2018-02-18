from django.contrib import admin
from . models import OfficerProfile

# Register your models here.
admin.site.site_header = 'Traffic Offence Doc System'

class OfficerProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'description', 'phone', 'location')
	search_fields = ['user', 'location']

admin.site.register(OfficerProfile, OfficerProfileAdmin)
