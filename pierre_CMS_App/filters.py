import django_filters
from django_filters import CharFilter

from django_filters import FilterSet

from .models import *

class CustomerFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name= 'first_name', lookup_expr='icontains')
    # icontains = ignore case sensitivity!
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'membership_status']