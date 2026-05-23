from django.contrib import admin
from .models import Idea, Favorite

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'idea', 'added_at')