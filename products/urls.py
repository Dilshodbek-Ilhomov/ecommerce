from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, CategoryViewSet, CartViewSet
from .services.flash_sale import FlashSaleListCreateView, check_flash_sale
from .services.product_view_history import ProductViewHistoryCreate

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('flash-sales/', FlashSaleListCreateView.as_view(), name='flash-sale-list'),
    path('flash-sales/check/<int:product_id>/', check_flash_sale, name='check-flash-sale'),
    path('history/', ProductViewHistoryCreate.as_view(), name='product-view-history'),
]