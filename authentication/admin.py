from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Doctor

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Fix fieldsets type issues
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Additional Info', {
            'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')
        }),
    ]
    
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ('Additional Info', {
            'fields': ('user_type', 'first_name', 'last_name', 'email')
        }),
    ]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'get_email')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    
    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_name.admin_order_field = 'user__first_name'  # Allows column order sorting
    get_name.short_description = 'Name'  # Sets column title
    
    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'get_email')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    
    def get_name(self, obj):
        return f"Dr. {obj.user.first_name} {obj.user.last_name}"
    get_name.admin_order_field = 'user__first_name'
    get_name.short_description = 'Name'
    
    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

admin.site.register(User, CustomUserAdmin)
