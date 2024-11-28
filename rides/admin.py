from django.contrib import admin
from .models import Ride
import mapwidgets
from django.contrib.gis.db import models
from trip_preferences.models import RidePreference

# Register your models here.

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'departure', 'estimated_duration', 'estimated_arrival', 'get_preferences')
    search_fields = ('vehicle', 'departure', 'estimated_duration', 'estimated_arrival', 'get_preferences')
    readonly_fields = ('get_preferences',)
    formfield_overrides = {
        models.PointField: {"widget": mapwidgets.GoogleMapPointFieldInlineWidget}
    }

    def get_preferences(self, obj):
        # Fetch preferences related to the ride
        preferences = RidePreference.objects.filter(ride=obj).select_related('preference')
        return ", ".join([pref.preference.name for pref in preferences])
    
    get_preferences.short_description = "Preferences"