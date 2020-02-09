from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class ProfileAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']
    list_editable = ['is_staff', 'is_superuser']
    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(Profile, ProfileAdmin)
