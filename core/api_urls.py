from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'sales', views.SaleViewSet, basename='sales')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'vendors', views.VendorViewSet, basename='vendors')
router.register(r'customers', views.CustomerViewSet, basename='customers')
router.register(r'invoices', views.InvoiceViewSet, basename='invoices')
router.register(r'payments', views.PaymentViewSet, basename='payments')
router.register(r'wholesalepurchases', views.WholesalePurchaseViewSet, basename='wholesalepurchases')

urlpatterns = [
    path('', include(router.urls)),
]