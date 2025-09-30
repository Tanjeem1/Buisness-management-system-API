from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('staff', 'Staff')], default='staff')

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    wholesale_cost = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    min_stock = models.PositiveIntegerField(default=10)
    max_stock = models.PositiveIntegerField(default=100)
    last_purchase = models.DateTimeField(null=True, blank=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    specialties = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    status = models.CharField(max_length=50, default='active')
    total_purchases = models.PositiveIntegerField(default=0)
    last_purchase = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    shop_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    shop_type = models.CharField(max_length=50)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)
    outstanding_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_purchases = models.PositiveIntegerField(default=0)
    last_purchase = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='active')

    def __str__(self):
        return self.shop_name

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"Sale #{self.id} - {self.customer.shop_name}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class Invoice(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return self.invoice_number

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for {self.invoice.invoice_number}"

class WholesalePurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    def __str__(self):
        return f"Purchase of {self.product.name} from {self.vendor.name}"