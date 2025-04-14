#UNRELATED --- inbox carl for the templates' link.....luzzecarl@gmail.com....@mtn.com. Also, look for coat of many colors by Dolly Parton.
#SUPERUSER IS "peter" and password is "0000"

from django.shortcuts import render

# Create your views here.


def dashboard(request):  
    context = {

    }
    return render(request, 'pierre_CMS_App/dashboardPage.html', context)

def customers(request):
    context = {

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