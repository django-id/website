from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """
    Author in Admin
    """
    model = Profile
    list_display = (
        'user',
        'slug',
        'profile_name',
        'profile_email',
        'profile_location',
        'profile_github',
        'is_moderator'
    )

admin.site.register(Profile, ProfileAdmin)
