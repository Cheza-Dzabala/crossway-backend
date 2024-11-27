from django.contrib import admin
from .models import Vehicle, VehicleImage
from django.utils.html import format_html

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('driver', 'make', 'model', 'year', 'color', 'license_plate', 'capacity', 'mileage_at_registration', 'mileage_at_last_service', 'condition', 'is_approved', 'is_active')
    search_fields = ('make', 'model', 'year', 'color', 'license_plate', 'capacity', 'mileage_at_registration', 'mileage_at_last_service', 'condition')
    exclude = ('blue_book',)
    
    def blue_book_preview(self, obj):
        if obj.blue_book:
            return format_html('<img src="{}" style="width: 150px; height: 150px;" />', obj.blue_book.url)
        return "No Image"
    blue_book_preview.short_description = "Blue Book"
    
    readonly_fields = ('driver', 'make', 'model', 'year', 'color', 'license_plate', 'capacity', 'mileage_at_registration', 'mileage_at_last_service', 'condition', 'blue_book_preview')
    
    
@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'image_preview', 'uploaded_at')
    search_fields = ('vehicle',)
    exclude = ('image',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image"
    
    
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: 150px;" />', obj.image.url)
        return "No Image"
    image_preview_large.short_description = "Image"
    
    readonly_fields = ('image_preview_large','vehicle',  'uploaded_at')
