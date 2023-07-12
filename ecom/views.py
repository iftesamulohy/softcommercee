from django.shortcuts import render
from requests import Response
from rest_framework.response import Response as Response2
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from ecom.models import Address, Cart, Order, Product,Category, ProductReviews,SubCategory,SubsubCategory,Brand,Size,Images,Color, Wishlist
from ecom.serializers import BrandSerializer, CartSerializer, CategorySerializer, ColorSerializer, ImagesSerializer, OrderSerializer, ProductReviewSerializer, ProductSerializer, SizeSerializer, SubCategorySerializer, SubsubCategorySerializer, WishlistSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from ecom.models import Product
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
class ColorViews(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

class ImageViews(viewsets.ModelViewSet):
    serializer_class = ImagesSerializer
    queryset = Images.objects.all()

class SizeViews(viewsets.ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

class SubsubCategoryViews(viewsets.ModelViewSet):
    serializer_class = SubsubCategorySerializer
    queryset = SubsubCategory.objects.all()

class SubCategoryViews(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class CategoryViews(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BrandViews(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ProductViews(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
class ProductReviewViews(viewsets.ModelViewSet):
    serializer_class = ProductReviewSerializer
    queryset = ProductReviews.objects.all()
class CartViews(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        user = User.objects.get(id=user_id)
        print(Address.objects.get(user=user))
        return Cart.objects.filter(user=user_id)
    def create(self, request):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        cart = Cart.objects.filter(user=user_id,product=request.data['product'])
        if cart:
            return Response2({"Error": False,"message":"Product already added"})
        serializer = CartSerializer(data={'product':request.data['product'],'user':user_id,'quantity':request.data['quantity']})
        print(request.data['product'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response2({"success": True,"data":serializer.data})
    
class WishlistViews(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
class OrderViews(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()



#admin
@login_required
def api_counts(request):
    total_products = Product.objects.count()
    total_users = User.objects.count()

    data = {
        'total_products': total_products,
        'total_users': total_users,
    }

    return JsonResponse(data)
