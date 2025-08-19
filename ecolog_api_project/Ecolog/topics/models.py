from django.db import models
from django.conf import settings
from categories.models import Category

class Topic(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='topics', null=True)
    related_topics = models.ManyToManyField('self', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='favorites')
    favorited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'topic')

    def __str__(self):
        return f"{self.user.username} liked {self.topic.title}"

# Create your models here.
