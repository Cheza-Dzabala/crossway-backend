from django.contrib import admin
from django.utils.html import format_html
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'role', 'is_active',)
    list_filter = ('role',)
    search_fields = ('name', 'phone_number', 'email')
    exclude = ('password', 'avatar') 
    
    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.avatar.url)
        return "No Image"
    avatar_preview.short_description = "Avatar Preview"

    readonly_fields = ('name', 'phone_number','avatar_preview', )  
