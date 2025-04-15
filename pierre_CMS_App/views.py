#UNRELATED --- inbox carl for the templates' link.....luzzecarl@gmail.com....@mtn.com. Also, look for coat of many colors by Dolly Parton.
#SUPERUSER IS "peter" and password is "0000"

from django.shortcuts import render, redirect
from . models import *
from . forms import *

# Create your views here.


def dashboard(request): 
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_basic_customers = Customer.objects.filter(membership_status = 'Basic').count()
    total_premium_customers = Customer.objects.filter(membership_status = 'Premium').count()

    form = CustomerForm(request.POST)
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
        'form': form
    }
    return render(request, 'pierre_CMS_App/dashboardPage.html', context)

def customers(request):
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'pierre_CMS_App/customerPage.html', context)

def orders(request): 
    context = {

    }
    return render(request, 'pierre_CMS_App/orderPage.html', context)

def setting(request):
    context = {

    }
    return render(request, 'pierre_CMS_App/settingsPage.html', context)

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