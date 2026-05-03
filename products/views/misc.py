from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Order
from products.models import Review, Category
from products.permissions import IsOwnerOrReadOnly
from products.serializers import OrderSerializer
from products.serializers import ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Users should only see their own orders. Staff can see all.
        if self.request.user.is_staff:
            return Order.objects.all().select_related('product')
        return Order.objects.filter(customer=self.request.user).select_related('product')

    def perform_create(self, serializer):
        # Automatically set the customer to the current user
        serializer.save(customer=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] # Added authentication check


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer