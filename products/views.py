from rest_framework import status, viewsets
from products.models import Product, Review, Category, CartItem
from products.serializers import ProductSerializer, ReviewSerializer, CategorySerializer, CartItemSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        # Swagger schema generatsiyasi vaqtida AnonymousUser xatosining oldini olish
        if getattr(self, 'swagger_fake_view', False):
            return CartItem.objects.none()
        
        if self.request.user.is_authenticated:
            return CartItem.objects.filter(cart__user=self.request.user)
        return CartItem.objects.none()