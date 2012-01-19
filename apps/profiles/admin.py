from django.contrib import admin
from .models import Profile, Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('from_profile', 'to_profile')
    ordering = ('from_profile', 'to_profile')
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_booster',)
    ordering = ('id_booster',)

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Profile, ProfileAdmin)