from django.contrib import admin
from .models import *



class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductPropertiesInline(admin.TabularInline):
    model = ProductProperties

class ProductUsageInline(admin.TabularInline):
    model = ProductUsage

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImagesInline, ProductPropertiesInline, ProductUsageInline)
    list_display = ['code', 'cat', 'name', 'price', 'quanty', 'size']
