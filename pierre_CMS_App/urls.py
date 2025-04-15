from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('customerPage/', views.customers, name='customersPage'),
    path('orderPage/', views.orders, name='ordersPage'),
    path('settingsPage/', views.setting, name='settingsPage'),

    path('addCustomer/', views.addCustomer, name='addCustomer'),

]
