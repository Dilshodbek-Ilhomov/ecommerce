from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from products.models import FlashSale, Product
# We will add FlashSaleSerializer to serializers.misc later
from products.serializers.misc import FlashSaleSerializer


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer


@api_view(['GET'])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        sale = FlashSale.objects.filter(product=product).first()
        
        if sale and sale.is_active():
            return Response({
                "is_on_sale": True,
                "discount": sale.discount_percentage,
                "end_time": sale.end_time
            })
        
        return Response({"is_on_sale": False})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
