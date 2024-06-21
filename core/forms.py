from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'city', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }