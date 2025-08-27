from django.contrib import admin
from .models import Topic, RelatedTopic, Favorite

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')

@admin.register(RelatedTopic)
class RelatedTopicAdmin(admin.ModelAdmin):
    list_display = ('from_topic', 'to_topic', 'category')
    search_fields = ('from_topic__title', 'to_topic__title')
    list_filter = ('category',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'favorited_at')
    search_fields = ('user__username', 'topic__title')
    list_filter = ('favorited_at',)
