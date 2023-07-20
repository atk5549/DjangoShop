from django.contrib import admin
from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)


# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'created_timestamp')
#     fields = ('user', 'product', 'quantity', 'created_timestamp')
#     search_fields = ('user',)
#     ordering = ('user',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp', )
    exxtra = 0
