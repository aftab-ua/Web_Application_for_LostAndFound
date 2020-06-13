from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):

    list_display = ('status', 'user', 'phone_number', 'timestamp',)

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)

