from django.contrib import admin
from .models import Company, Position

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name', )

class PositionAdmin(admin.ModelAdmin):
    list_display = ('profile', 'company')

admin.site.register(Position, PositionAdmin)
admin.site.register(Company, CompanyAdmin)
