from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Author Form
    """
    class Meta:
        model = Profile
        fields = [
            'profile_picture',
            'profile_name',
            'profile_email',
            'profile_location',
            'profile_github'
        ]
        exclude = ['user']
        widgets = {'user': forms.HiddenInput()}
