from django.contrib import admin
from .models import Topic, Favorite

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')
    filter_horizontal = ('related_topics',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'favorited_at')
    search_fields = ('user__username', 'topic__title')
    list_filter = ('favorited_at',)
    




# Register your models here.
