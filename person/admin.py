from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('status', 'user', 'name', 'phone_number', 'location',  'timestamp',)

    class Meta:
        model = Person


admin.site.register(Person, PersonAdmin)

