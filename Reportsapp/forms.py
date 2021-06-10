from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model =User
        fields = ['order_id', 'name', 'email', 'date', 'response', 'resolve']
        widgets = {
            'order_id': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'date': forms.TextInput(attrs={'class':'form-control'}),
            'response': forms.TextInput(attrs={'class':'form-control'}),
            'resolve': forms.TextInput(attrs={'class':'form-control'}),
        }