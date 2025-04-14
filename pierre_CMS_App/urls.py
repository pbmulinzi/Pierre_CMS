from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('orders/', views.orders, name='orders'),
    path('settings/', views.setting, name='settings'),

]
