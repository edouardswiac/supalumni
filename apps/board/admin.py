from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'content',)
    ordering = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)