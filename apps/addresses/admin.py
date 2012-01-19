from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street1', 'street2', 'zipcode', 'city', 'lat', 'long')
    ordering = ('city',)
    exclude = ('lat', 'long')
admin.site.register(Address, AddressAdmin)
