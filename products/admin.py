from django.contrib import admin
from .models import Category, Product, Review, FlashSale, ProductViewHistory, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'date_posted')
    list_filter = ('rating', 'date_posted')

@admin.register(FlashSale)
class FlashSaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'discount_percentage', 'start_time', 'end_time', 'is_active')

@admin.register(ProductViewHistory)
class ProductViewHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'timestamp')

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = [CartItemInline]
