from django.contrib import admin

from data.models import Item, Category, Manufacturer, Shop


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    search_fields = ('name', )
    list_filter = ('category__name', 'manufacturer__name')
    list_display = ('name', 'category', 'price', 'rating')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):

    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):

    pass
