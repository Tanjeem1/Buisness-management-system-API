from django.contrib import admin
from .models import User, Product, Vendor, WholesalePurchase, Customer, Sale, SaleItem, Invoice, Payment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'is_staff', 'is_superuser']
    list_filter = ['role', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'retail_price', 'wholesale_cost', 'stock_quantity', 'min_stock', 'max_stock', 'vendor']
    list_filter = ['vendor']
    search_fields = ['name', 'description']

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'phone_number', 'email', 'rating', 'status']
    list_filter = ['status']
    search_fields = ['name', 'contact_person', 'email']

@admin.register(WholesalePurchase)
class WholesalePurchaseAdmin(admin.ModelAdmin):
    list_display = ['product', 'vendor', 'quantity', 'cost_per_unit', 'purchase_date']
    list_filter = ['purchase_date', 'vendor']
    search_fields = ['product__name', 'vendor__name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'contact_person', 'phone_number', 'email', 'shop_type', 'credit_limit', 'outstanding_amount', 'status']
    list_filter = ['shop_type', 'status']
    search_fields = ['shop_name', 'contact_person', 'email']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'user', 'sale_date', 'total_amount', 'is_paid', 'status']
    list_filter = ['sale_date', 'is_paid', 'status']
    search_fields = ['customer__shop_name', 'user__username']

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['sale', 'product', 'quantity', 'unit_price', 'line_total']
    list_filter = ['sale']
    search_fields = ['product__name']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'sale', 'due_date', 'status']
    list_filter = ['status', 'due_date']
    search_fields = ['invoice_number', 'sale__customer__shop_name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'amount_paid', 'payment_date', 'payment_method']
    list_filter = ['payment_date', 'payment_method']
    search_fields = ['invoice__invoice_number']