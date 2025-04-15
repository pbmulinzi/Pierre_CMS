from django import forms
from django.forms import ModelForm

from . models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'membership_status']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class SettingsForm(ModelForm):
    class Meta:
        model = AccountSettings
        fields = "__all__"
