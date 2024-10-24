from rest_framework import serializers
from .models import Customer, Item, ItemHasOrder, ItemType, Order, PaymentMethod, SalaryHistory, SalaryType, Sale, TableInRestaurant, Waiter, WaiterHasOrder

class CustomerSerializer(serializers.ModelSerializer):
    sale = serializers.StringRelatedField()

    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    item_type = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = '__all__'

class ItemHasOrderSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()
    item = serializers.StringRelatedField()

    class Meta:
        model = ItemHasOrder
        fields = '__all__'

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    table = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()
    payment_method = serializers.StringRelatedField()
    waiters = serializers.StringRelatedField(many=True)
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class SalaryHistorySerializer(serializers.ModelSerializer):
    waiter = serializers.StringRelatedField()
    salary_type = serializers.StringRelatedField()

    class Meta:
        model = SalaryHistory
        fields = '__all__'

class SalaryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryType
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class TableInRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInRestaurant
        fields = '__all__'

class WaiterSerializer(serializers.ModelSerializer):
    salary_type = serializers.StringRelatedField()

    class Meta:
        model = Waiter
        fields = '__all__'

class WaiterHasOrderSerializer(serializers.ModelSerializer):
    waiter = serializers.StringRelatedField()
    order = serializers.StringRelatedField()

    class Meta:
        model = WaiterHasOrder
        fields = '__all__'