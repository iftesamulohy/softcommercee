from django.contrib import admin

from ecom.models import Address, Product,Category,SubCategory,SubsubCategory,Brand,Size,Images,Color,Unit,ProductReviews,Cart,Wishlist,OrderedProduct,Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(SubsubCategory)
class SubsubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['filename']
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Address)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']

#test another





#test code
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
class MyAdminSite(AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['user_count'] = User.objects.count()
        return context

