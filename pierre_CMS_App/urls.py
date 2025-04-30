from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('customerPage/', views.customers, name='customersPage'),
    path('orderPage/', views.orders, name='ordersPage'),
    path('productsPage/', views.products, name ='productsPage'),
    path('settingsPage/', views.CompanyAccountSettings, name='settingsPage'),

    path('addCustomer/', views.addCustomer, name='addCustomer'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('createOrder/', views.createOrder, name='createOrder'),
    path('updateSettings/', views.updateSettings, name='updateSettings'),

    path('updateCustomer/<str:pk>/', views.updateCustomer, name='updateCustomer'),
    path('deleteCustomer/<str:pk>/', views.deleteCustomer, name='deleteCustomer'),
    path('deleteCustomerrr/<str:pk>/', views.deleteCustomerrr, name='deleteCustomerrr'), #Explanation is in the views.
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>./', views.deleteOrder, name='deleteOrder'),
    path('updateProduct/<str:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<str:pk>/', views.deleteProduct, name='deleteProduct'),

]
