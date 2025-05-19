import django_filters
from django_filters import CharFilter

from django_filters import FilterSet

from .models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['membership_status']