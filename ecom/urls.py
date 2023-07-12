from django.urls import path
from ecom import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'color',views.ColorViews,basename="color")
router.register(r'image',views.ImageViews,basename="image")
router.register(r'size',views.SizeViews,basename="size")
router.register(r'sub-sub-category',views.SubsubCategoryViews,basename="sub-sub-category")
router.register(r'sub-category',views.SubCategoryViews,basename="sub-category")
router.register(r'category',views.CategoryViews,basename="category")
router.register(r'brand',views.BrandViews,basename="brand")
router.register(r'product',views.ProductViews,basename="product")
router.register(r'product-review',views.ProductReviewViews,basename="product-review")
router.register(r'cart',views.CartViews,basename="cart")
router.register(r'wishlist',views.WishlistViews,basename="wishlist")
router.register(r'order',views.OrderViews,basename="order")

urlpatterns = [
    path('api/counts/', views.api_counts, name='api_counts'),
]
urlpatterns+= router.urls