from django.db import models

# Create your models here.
class Customer(models.Model): 

    STATUS = (
        ('Premium', 'Premium'),
        ('Basic', 'Basic'),
    )

    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    membership_status = models.CharField(max_length=200, choices=STATUS, default='Basic')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    CURRENCY = (
        ("UGX.", "UGX."),
        ("USD.", "USD."),
        ("EUR.", "EUR."),
        ("KSH.", "KSH."),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True) #decimal field coz of currency/ monetary nature.
    product_model = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY, default='UGX.')

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    UNITS = (
        ('--select--', '--select--'),
        ('cars', 'cars'),
        ('pieces', 'pieces'),
        ('kgs', 'kgs'),
        ('tins', 'tins'),
        ('bags', 'bags'),
        ('trucks', 'trucks'),
        ('litres', 'litres'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order_number = models.PositiveIntegerField(auto_created=True, unique=True)
    Quantity = models.PositiveIntegerField(auto_created=True)
    Units = models.CharField(max_length=200, choices=UNITS, default='--Select--')
    order_status = models.CharField(max_length=200, choices=ORDER_STATUS, default='--Select--')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=200, null=True)
    notes = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.customer}'s order. Order number: {self.order_number} " 
    
class AccountSettings(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(null=True, blank=True, default='', help_text="Upload your company logo")
    company_email = models.EmailField(max_length=200, null=True)
    company_phone = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)  

    def __str__(self):
        return self.company_name  