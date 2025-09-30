from rest_framework import serializers
from core.models import Sale, Product, Vendor, Customer, Invoice, Payment, WholesalePurchase, SaleItem, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_superuser', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False),
            is_superuser=validated_data.get('is_superuser', False),
            role=validated_data.get('role', 'staff')
        )
        return user

class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity', 'unit_price', 'line_total']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = ['id', 'customer', 'user', 'sale_date', 'total_amount', 'is_paid', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        sale = Sale.objects.create(**validated_data)
        for item_data in items_data:
            SaleItem.objects.create(sale=sale, **item_data)
        return sale

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.user = validated_data.get('user', instance.user)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.is_paid = validated_data.get('is_paid', instance.is_paid)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if items_data:
            instance.items.all().delete()  # Remove existing items
            for item_data in items_data:
                SaleItem.objects.create(sale=instance, **item_data)

        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'retail_price', 'wholesale_cost', 'stock_quantity', 'min_stock', 'max_stock', 'last_purchase', 'vendor']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_person', 'phone_number', 'email', 'address', 'specialties', 'rating', 'status', 'total_purchases', 'last_purchase']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'shop_name', 'contact_person', 'phone_number', 'address', 'email', 'shop_type', 'credit_limit', 'outstanding_amount', 'total_purchases', 'last_purchase', 'status']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'sale', 'invoice_number', 'due_date', 'status']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'amount_paid', 'payment_date', 'payment_method']

class WholesalePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholesalePurchase
        fields = ['id', 'product', 'vendor', 'quantity', 'cost_per_unit', 'purchase_date']