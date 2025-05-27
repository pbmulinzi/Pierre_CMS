import django_filters
from django_filters import CharFilter

from django_filters import FilterSet

from .models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['membership_status']

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['order_status']

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name']