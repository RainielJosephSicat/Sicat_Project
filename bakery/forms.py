# bakery/forms.py

from django import forms
from .models import CustomerInfo, CustomerMessage

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['name', 'contact_number', 'email']

class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = ['message']
