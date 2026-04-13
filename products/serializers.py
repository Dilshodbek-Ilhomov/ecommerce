from rest_framework import serializers
from django.db.models import Avg
from .models import Category, Product, Review, CartItem, ProductViewHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_name', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.reviews.aggregate(Avg('rating'))['rating__avg']


class ProductViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewHistory
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'