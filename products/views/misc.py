from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Order, Review, Category, Product, ProductViewHistory, FlashSale
from products.permissions import IsOwnerOrReadOnly
from products.serializers import OrderSerializer, ReviewSerializer, CategorySerializer, FlashSaleSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer


@api_view(['GET'])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has viewed this product before
    user_viewed = False
    if request.user.is_authenticated:
        user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()

    # Check if the product is or will be on a flash sale within the next 24 hours
    now = timezone.now()
    upcoming_flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte=now + timedelta(hours=24),
        end_time__gte=now
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time = upcoming_flash_sale.start_time
        end_time = upcoming_flash_sale.end_time
        return Response({
            "message": f"This product will be on a {discount}% off flash sale!",
            "start_time": start_time,
            "end_time": end_time
        })
    else:
        return Response({
            "message": "No upcoming flash sales for this product."
        })