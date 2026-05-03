from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import F
from rest_framework import serializers

from products.models import Order, Product


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']

    def get_total_price(self, obj):
        # Note: Optimization with select_related should be done in the ViewSet
        return obj.product.price * obj.quantity

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def validate(self, data):
        product = data.get('product')
        quantity = data.get('quantity')

        if product and quantity > product.stock:
            raise serializers.ValidationError({"quantity": "Not enough items in stock."})

        return data

    @transaction.atomic
    def create(self, validated_data):
        quantity = validated_data['quantity']
        product = validated_data['product']

        # Create the order
        order = Order.objects.create(**validated_data)

        # Atomically reduce stock
        Product.objects.filter(id=product.id).update(stock=F('stock') - quantity)

        self.send_confirmation_email(order)
        return order

    def send_confirmation_email(self, order):
        # Here you would send an email. For this example, we'll just print
        print(f"Sent confirmation email for Order {order.id}")