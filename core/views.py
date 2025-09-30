from django.views.generic import ListView
from django.utils import timezone
from django.db.models import Sum, Avg, F
from rest_framework import viewsets
from core.models import (
    Sale, Product, Vendor, Customer, Invoice, Payment, WholesalePurchase, User, SaleItem
)
from core.serializers import (
    SaleItem, SaleSerializer, ProductSerializer, VendorSerializer, CustomerSerializer,
    InvoiceSerializer, PaymentSerializer, WholesalePurchaseSerializer, UserSerializer
)



# DRF ViewSets (API)
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class WholesalePurchaseViewSet(viewsets.ModelViewSet):
    queryset = WholesalePurchase.objects.all()
    serializer_class = WholesalePurchaseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer