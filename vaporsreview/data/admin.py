from django.contrib import admin

from data.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    search_fields = ('name', 'summary', 'specifications')
    list_filter = ('category', 'manufacturer', 'rating')
    list_display = ('name', 'source_url', 'price', 'currency', 'comment')
