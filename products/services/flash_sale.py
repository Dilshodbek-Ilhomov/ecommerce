from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, serializers
from products.models import Product, ProductViewHistory, FlashSale

class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer

@api_view(['GET'])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has viewed this product before
    user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()

    # Check if the product is or will be on a flash sale within the next 24 hours
    now = timezone.now()
    upcoming_flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte = now + timedelta(hours=24),
        end_time__gte = now
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