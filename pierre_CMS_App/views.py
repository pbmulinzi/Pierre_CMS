#SUPERUSER IS "peter" and password is "0000"

from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . forms import *

from .filters import CustomerFilter

# Create your views here.


def dashboard(request): 
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_basic_customers = Customer.objects.filter(membership_status = 'Basic').count()
    total_premium_customers = Customer.objects.filter(membership_status = 'Premium').count()
    form = CustomerForm(request.POST)

    myFilter = CustomerFilter(request.GET, queryset=customers)
    customers = myFilter.qs

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        form = CustomerForm()
        
    context = {
        'customers': customers,
        'total_customers': total_customers,
        'total_basic_customers': total_basic_customers,
        'total_premium_customers': total_premium_customers,
        'form': form,

        'myFilter': myFilter,
    }
    return render(request, 'pierre_CMS_App/dashboardPage.html', context)

def customers(request):
    customers = Customer.objects.all()
    cust_form = CustomerForm(request.POST)
    if request.method == 'POST' and cust_form.is_valid():
        cust_form.save()
        return redirect('dashboard')
    else:
        cust_form = CustomerForm()
    context = {
        'customers': customers,
        'cust_form': cust_form,
    }
    return render(request, 'pierre_CMS_App/customerPage.html', context)

def addCustomer(request):
    form = CustomerForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')
    else:
        form = CustomerForm()
    context = {
        'form': form
    }
    return render(request, 'pierre_CMS_App/addCustomer.html', context)

def updateCustomer(request, pk):
    customers = Customer.objects.get(id=pk)
    updateForm = CustomerForm(instance=customers)

    if request.method == 'POST':
        updateForm = CustomerForm(request.POST, instance=customers)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('dashboard')
    context = {
        'updateForm': updateForm,
    }
    return render(request, 'pierre_CMS_App/updateCustomer.html', context)


def deleteCustomer(request, pk):
    customers = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('/')
    context = {
        'item': customers,
    }
    return render(request, 'pierre_CMS_App/delete.html', context)

# Particularly for the customers page...such that the redirection can be towards the customersPage
def deleteCustomerrr(request, pk):
    customers = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customers.delete()
        return redirect('/')
    context = {
        'item': customers,
    }
    return render(request, 'pierre_CMS_App/deleteCustomer.html', context)


def products(request):
    products = Product.objects.all()
    prodPageForm = ProductForm(request)
    context = {
        'products': products,
        'prodPageForm': prodPageForm,
    }
    return render(request, 'pierre_CMS_App/productsPage.html', context)

def addProduct(request):
    prodForm = ProductForm(request.POST)
    if request.method == 'POST' and prodForm.is_valid():
        prodForm.save()
        return redirect('productsPage')
    else:
        prodForm = ProductForm()
    context = {
        'prodForm': prodForm,
    }
    return render(request, 'pierre_CMS_App/addProduct.html', context)

def updateProduct(request, pk):
    products = Product.objects.get(id=pk)
    updateProductForm = ProductForm(instance=products)
    if request.method == 'POST':
        updateProductForm = ProductForm(request.POST, instance=products)
        if updateProductForm.is_valid():
            updateProductForm.save()
            return redirect('productsPage')

    context = {
        'updateProductForm': updateProductForm,
    }
    return render(request, 'pierre_CMS_App/updateProduct.html', context)

def deleteProduct(request, pk):
    products = Product.objects.get(id=pk)
    if request.method == 'POST':
        products.delete()
        return redirect('productsPage')
    context = {
        'item': products,
    }
    return render(request, 'pierre_CMS_App/deleteProduct.html', context)


def orders(request): 
    orders = Order.objects.all()
    total_orders = orders.count()
    pending = Order.objects.filter(order_status = "Pending").count()
    completed = Order.objects.filter(order_status='Completed').count()
    cancelled = Order.objects.filter(order_status='Cancelled').count()

    context = {
        'orders': orders,
        'total_orders': total_orders,
        'pending': pending,
        'completed': completed,
        'cancelled': cancelled,
    }
    
    return render(request, 'pierre_CMS_App/orderPage.html', context)

def createOrder(request):
    ordForm = OrderForm(request.POST)
    if request.method == "POST" and ordForm.is_valid():
        ordForm.save()
        return redirect('ordersPage')
    else:
        ordForm = OrderForm()
    context = {
        'ordForm': ordForm,
    }
    return render(request, 'pierre_CMS_App/createOrder.html', context)

def updateOrder(request, pk):
    orders = Order.objects.get(id=pk)
    updateOrderForm = OrderForm(instance=orders)

    if request.method == "POST":
        updateOrderForm = OrderForm(request.POST, instance=orders)
        if updateOrderForm.is_valid():
            updateOrderForm.save()
            return redirect('ordersPage')
    
    context = {
        'updateOrderForm': updateOrderForm,
    }
    return render(request, 'pierre_CMS_App/updateOrder.html', context)

def deleteOrder(request, pk):
    orders = Order.objects.get(id=pk)
    if request.method == 'POST':
        orders.delete()
        return redirect('/')
    context = {
        'item': orders,
    }
    return render(request, 'pierre_CMS_App/deleteOrder.html', context)


def CompanyAccountSettings(request):
    settings = AccountSettings.objects.all()
    context = {
        'settings': settings,
    }
    return render(request, 'pierre_CMS_App/settingsPage.html', context)

def updateSettings(request):
    settingForm = SettingsForm(request.POST, request.FILES)
    if request.method == "POST" and settingForm.is_valid():
        settingForm.save()
        return redirect('settingsPage')
    else:
        settingForm = SettingsForm()
    context = {
        'settingForm': settingForm,
    }
    return render(request, 'pierre_CMS_App/updateSettings.html', context)

