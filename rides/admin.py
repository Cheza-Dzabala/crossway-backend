from django.contrib import admin
from .models import Ride
import mapwidgets
from django.contrib.gis.db import models

# Register your models here.

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'departure', 'estimated_duration', 'estimated_arrival')
    search_fields = ('vehicle', 'departure', 'estimated_duration', 'estimated_arrival')
    
    formfield_overrides = {
        models.PointField: {"widget": mapwidgets.GoogleMapPointFieldInlineWidget}
    }
