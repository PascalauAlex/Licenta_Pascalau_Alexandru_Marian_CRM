from django.contrib import admin

from products.models import Product, ProductCategory, LeadProductInterest

# Register your models here.

admin.register(Product)
admin.register(ProductCategory)
admin.register(LeadProductInterest)
