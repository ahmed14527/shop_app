from django.urls import path, include
from rest_framework import routers
from .views import (CategoryViewSet, 
                    ProductViewSet,
                    favoriteListAPIView,
                    favoriteViewSet,
                    ProductListAPIView,
                   OrderListAPIView,
                   OrderViewSet,
                    CategoryListAPIView
                    )

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'favorites', favoriteViewSet)



urlpatterns = [
    path('categories/list/',CategoryListAPIView.as_view(), name='category-list'),
    path('products/list/',ProductListAPIView.as_view(), name='product-list'),
    path('orders/list/',OrderListAPIView.as_view(), name='order-list'),
    path('favorites/list/',favoriteListAPIView.as_view(), name='favorite-list'),

    path('', include(router.urls)),

]