from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "in_stock", "inventory", "created_at")
    list_editable = ("price", "in_stock", "inventory")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
