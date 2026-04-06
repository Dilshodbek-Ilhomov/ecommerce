from rest_framework import status, viewsets
from products.models import Product, Review, Category
from products.serializers import ProductSerializer, ReviewSerializer, CategorySerializer

class ReviewViewSet(viewsets. ModelViewSet):
    queryset = Review.objects. all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects. all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects. all()
    serializer_class = ProductSerializer