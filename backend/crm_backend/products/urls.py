from django.urls import path, include
from pycparser.c_ast import Default
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSetMixin

from products.views import ProductsViewSet, ProductCategoryViewSet, ProductLeadViewSet

router = DefaultRouter()
router.register('products',ProductsViewSet,basename='products')
router.register('product-category',ProductCategoryViewSet,basename='products-category')
router.register('lead-products',ProductLeadViewSet,basename='lead-products')

urlpatterns = [
   path('',include(router.urls))
]