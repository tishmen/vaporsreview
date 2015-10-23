from django.contrib import admin

from data.models import Item, Category, Manufacturer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):

    search_fields = ('name', 'description')
    list_filter = ('rating', )
    list_display = ('name', 'description')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    search_fields = ('name', 'summary')
    list_filter = ('category__name', 'manufacturer__name', 'rating')
    list_display = ('name', 'summary', 'price', 'currency')
