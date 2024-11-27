from django.contrib import admin
from .models import TripPreferences, DriverPreference
# Register your models here.

admin.site.register(TripPreferences)
admin.site.register(DriverPreference)

