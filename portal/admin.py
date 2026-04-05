from django.contrib import admin
from .models import Product
from django.utils.html import format_html


# ==========================================================
# PRODUCT ADMIN (Marketplace)
# ==========================================================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # 🔥 SHOW IMAGE PREVIEW IN ADMIN
    def image_preview(self, obj):
        if obj.image_main:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:5px;" />',
                obj.image_main.url
            )
        return "No Image"

    def gif_preview(self, obj):
        if obj.image_animated:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:5px;" />',
                obj.image_animated.url
            )
        return "No GIF"

    image_preview.short_description = "Image"
    gif_preview.short_description = "GIF"

    # 📋 DISPLAY
    list_display = (
        'image_preview',
        'gif_preview',
        'name',
        'brand',
        'category',
        'price',
        'is_available',
        'in_stock',
        'created_at',
    )

    # 🔍 FILTERS
    list_filter = (
        'category',
        'is_available',
        'in_stock',
    )

    # 🔎 SEARCH
    search_fields = (
        'name',
        'brand',
    )

    # ⬇ ORDER
    ordering = (
        '-created_at',
    )

    # ✏ EDIT FROM LIST
    list_editable = (
        'is_available',
        'in_stock',
    )