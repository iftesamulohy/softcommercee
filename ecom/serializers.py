from rest_framework import serializers
from ecom.models import Product,Category,SubCategory,SubsubCategory,Brand,Size,Images,Color,ProductReviews,Cart,OrderedProduct,Wishlist,Order
from django.contrib.auth.models import User
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth=2

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
        depth=2

class SubsubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubsubCategory
        fields = "__all__"
        depth=2

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        depth=2

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"
        depth=2

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"
        depth=2

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        depth=2
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth=3
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviews
        fields = "__all__"
        depth=2
class CartSerializer(serializers.ModelSerializer):
    productinfo = serializers.SerializerMethodField()
    colorinfo = serializers.SerializerMethodField()
    sizeinfo = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField()
    
   
    def get_productinfo(self, obj):
        product = obj.product
        return ProductSerializer(product).data
    def get_sizeinfo(self, obj):
        size = obj.size
        return SizeSerializer(size).data
    def get_colorinfo(self, obj):
        color = obj.color
        return ColorSerializer(color).data
    def get_total_price(self, obj):
        # Calculate the total price of the cart item by multiplying the product price with the quantity
        total_price = obj.product.offer_price * obj.quantity
        return total_price
    def get_discount_price(self, obj):
        # Calculate the total price of the cart item by multiplying the product price with the quantity
        discount_price = obj.product.price - obj.product.offer_price
        return discount_price
    class Meta:
        model = Cart
        fields = "__all__"
        #depth=2
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
        depth=2
class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = "__all__"
        depth=2
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        depth=3

